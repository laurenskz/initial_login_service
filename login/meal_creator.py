from typing import Iterable, Dict

from injector import inject

from com.baboea.concept_pb2 import BoolConceptValues
from com.baboea.models.curated_diet_pb2 import CuratedDiet
from com.baboea.models.diet_pb2 import ClientMealSize, UserDietDefinition
from com.baboea.models.localized_pb2 import LocaleRef
from com.baboea.models.meal_pb2 import MealRef, Meal
from com.baboea.models.template_recipe_data_pb2 import ImprovedTemplateRecipe, TemplateRecipeLocalized, \
    ImprovedTemplateRecipeRef
from com.baboea.models.users_pb2 import UserRef
from com.baboea.services.base_pb2 import GetRequest, AddResponse
from com.baboea.services.curated_diet_service_pb2_grpc import CuratedDietServiceStub
from com.baboea.services.login_service_pb2 import InitialLoginForm, MealStructurePreference, MealInit, MealSize
from com.baboea.services.meal_service_pb2_grpc import MealServiceStub
from com.baboea.services.template_recipe_service_pb2_grpc import ImprovedTemplateRecipeServiceStub
from login.dependencies import Concepts
from login.simplified_setup import MealCreator


class BaseMealCreator(MealCreator):
    meal_sizes = {
        MealSize.big: 1.5,
        MealSize.normal: 1.0,
        MealSize.small: 0.5
    }

    @inject
    def __init__(self,
                 meal_service: MealServiceStub,
                 admin_diet: UserDietDefinition,
                 template_recipe_service: ImprovedTemplateRecipeServiceStub,
                 concepts: Concepts
                 ):
        super().__init__()
        self.template_recipe_service = template_recipe_service
        self.admin_diet = admin_diet
        self.meal_service = meal_service
        self.concepts = concepts
        self.admin_meal_ref_map: Dict[str, MealRef] = {
            x.meal.name.lower(): x.meal
            for x in admin_diet.mealSizes.sizes
        }

    def copy_meal_from_admin_diet(self, user: UserRef, admin_meal_ref: MealRef) -> MealRef:
        admin_meal: Meal = self.meal_service.Get(GetRequest(id=admin_meal_ref.id))
        meal = Meal()
        meal.CopyFrom(admin_meal)
        meal.owner.CopyFrom(user)
        meal.id = ""
        our_meal: AddResponse = self.meal_service.Add(meal)
        return MealRef(id=our_meal.id)

    def meal_based_on_template(self, user: UserRef, init: MealInit) -> MealRef:
        if init.templateRecipe.groups:
            user_meal = self.meal_based_on_template_recipe(user, init)
        else:
            user_meal = self.meal_based_on_side_dishes(user, init)
        meal_res: AddResponse = self.meal_service.Add(user_meal)
        return MealRef(id=meal_res.id)

    def meal_based_on_side_dishes(self, user: UserRef, init: MealInit):
        return Meal(
            name=init.name,
            owner=user,
            balanced=True,
            enableSides=True,
            maxSideKcalPercentage=100,
            simplifiedSides=init.sideDishes,
            maxSideFoods=init.maxSideFoods
        )

    def meal_based_on_template_recipe(self, user: UserRef, init: MealInit):
        template_recipe = ImprovedTemplateRecipe()
        template_recipe.CopyFrom(init.templateRecipe)
        template_recipe.owner.CopyFrom(user)
        while len(template_recipe.localizations) > 0:
            template_recipe.localizations.pop()
        template_recipe.localizations.append(TemplateRecipeLocalized(
            name=f"My standard {init.name}",
            locale=LocaleRef(id="en"),
        ))
        res: AddResponse = self.template_recipe_service.Add(template_recipe)
        user_meal = Meal(
            name=init.name,
            owner=user,
            templateRecipes=[ImprovedTemplateRecipeRef(id=res.id)],
            balanced=True,
            enableSides=False,
            maxSideKcalPercentage=30,
            concepts=BoolConceptValues(
                conceptValues={self.concepts.root.id: False}
            )
        )
        return user_meal

    def create_meals(self, user: UserRef, login: InitialLoginForm) -> Iterable[ClientMealSize]:
        result = []
        for m in login.meals:
            result_meal = None
            if m.mealPref == MealStructurePreference.disable:
                continue
            if m.mealPref == MealStructurePreference.generated and m.name.lower() in self.admin_meal_ref_map:
                result_meal = self.copy_meal_from_admin_diet(user, self.admin_meal_ref_map[m.name.lower()])
            if m.mealPref == MealStructurePreference.ownRecipe:
                result_meal = self.meal_based_on_template(user, m)
            if result_meal:
                result.append(ClientMealSize(
                    meal=result_meal,
                    size=self.meal_sizes[m.mealSize]
                ))
        return result
