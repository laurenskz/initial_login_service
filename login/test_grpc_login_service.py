import unittest
from unittest.mock import MagicMock, patch, Mock
from dataclasses import dataclass

from com.baboea.concept_pb2 import BoolConceptValues, ConceptTagStatus
from com.baboea.models.concept_tag_pb2 import ConceptTagRef
# Import the classes and methods to be tested
from com.baboea.models.concepts_pb2 import ConceptRef
from com.baboea.models.curated_diet_pb2 import CuratedDiet
from com.baboea.models.diet_pb2 import UserDietDefinition
from com.baboea.models.food_pb2 import FoodRef, Tag
from com.baboea.models.localized_pb2 import LocalizedString, LocalizedStringValue
from com.baboea.models.meal_pb2 import MealRef, SmartRecipePreferences, SmartRecipeAccuracyPreference
from com.baboea.models.objectivegroup_pb2 import ObjectiveGroupRef, ApplicationLevelRef
from com.baboea.models.property_pb2 import PropertyRef
from com.baboea.models.recipes_pb2 import QuantifiedRecipeIngredient, RecipeCategoryRef, RecipeCuisineRef, RecipeRef
from com.baboea.models.users_pb2 import UserRef, User
from com.baboea.services.base_pb2 import AddResponse, OperationResponse
from com.baboea.services.login_service_pb2 import InitialLoginForm, MealInit, MealStructurePreference, MealSize
from com.baboea.services.objective_group_service_pb2_grpc import ObjectiveGroupServiceStub
from com.baboea.services.meal_service_pb2_grpc import MealServiceStub
from com.baboea.services.user_service_pb2_grpc import UserServiceStub
from com.baboea.services.meal_plan_day_service_pb2_grpc import MealPlanDayServiceStub
from com.baboea.services.diet_service_pb2_grpc import UserDietServiceStub
from com.baboea.services.curated_diet_service_pb2_grpc import CuratedDietServiceStub
from com.baboea.services.application_level_service_pb2_grpc import ApplicationLevelServiceStub
from com.baboea.services.recipe_service_pb2_grpc import RecipeServiceStub
from com.baboea.services.concept_service_pb2_grpc import ConceptServiceStub

from login.bmr import BmrUseCase, UserReqs  # Assuming these are defined in login.bmr
from login.dependencies import (
    Concepts,
    ConceptTags,
    InitProperties,
    ApplicationLevels,
    PropertyByHandleResolver,
    UnitTestPropertyResolver
)
from login.impl import GrpcLoginService


# Mock definitions
class MockBmrUseCase(BmrUseCase):
    def calculate(self, form: InitialLoginForm) -> UserReqs:
        return UserReqs(
            minKcal=2000,
            maxKcal=2500,
            minProtein=50,
            maxProtein=150,
            minFiber=25,
            maxFiber=35,
            minCarbPercentage=45,
            maxCarbPercentage=65,
            minFatPercentage=20,
            maxFatPercentage=35
        )


# Begin unit tests
class TestGrpcLoginService(unittest.TestCase):

    def setUp(self):
        # Mock channels and services
        self.localized_kcal_string = LocalizedString(languages=[LocalizedStringValue(value="kcal")])
        self.channel = MagicMock()
        self.use_case = MockBmrUseCase()
        self.concepts = Concepts(
            root=ConceptRef(id="root_concept_id"),
            water=ConceptRef(id="water_concept_id"),
            pantry=ConceptRef(id="pantry_concept_id"),
            fat=ConceptRef(id="fat_concept_id")
        )
        self.tags = ConceptTags(
            common_item=ConceptTagRef(id="common_item_tag_id"),
            side_dish=ConceptTagRef(id="side_dish_tag_id")
        )
        self.application_levels = ApplicationLevels(
            meal=ApplicationLevelRef(id="meal_level_id"),
            day=ApplicationLevelRef(id="day_level_id")
        )
        self.properties = InitProperties(
            kcal=PropertyRef(id="kcal_property_id"),
            fat=PropertyRef(id="fat_property_id"),
            protein=PropertyRef(id="protein_property_id"),
            fiber=PropertyRef(id="fiber_property_id"),
            net_carbs=PropertyRef(id="net_carbs_property_id"),
            recipe_count=PropertyRef(id="recipe_count_property_id")
        )
        self.property_resolver = UnitTestPropertyResolver()

        # Mock gRPC service stubs
        self.meal_service = Mock()
        self.recipe_service = Mock()
        self.concept_service = Mock()
        self.day_service = Mock()
        self.user_service = Mock()
        self.objective_group_service = Mock()
        self.diet_service = Mock()
        self.application_service = Mock()
        self.curated_diet_service = Mock()

        # Initialize the GrpcLoginService with mocks
        self.login_service = GrpcLoginService(
            channel=self.channel,
            use_case=self.use_case,
            concepts=self.concepts,
            tags=self.tags,
            application_levels=self.application_levels,
            properties=self.properties,
            property_resolver=self.property_resolver,
            meal_service=self.meal_service,
            quantified_recipes=self.recipe_service,
            concept_service=self.concept_service,
            day_service=self.day_service,
            user_service=self.user_service,
            objective_group_service=self.objective_group_service,
            diet_service=self.diet_service,
            application_service=self.application_service,
            curated_diet=self.curated_diet_service
        )

    def test_setup_user(self):
        mock_diet_service = Mock()
        mock_objective_service = Mock()
        mock_user_service = Mock()
        mock_meal_service = Mock()
        # Mock responses
        self.user_service.Add.return_value = UserRef(id="user_id")
        self.meal_service.Add.return_value = MealRef(id="meal_id")
        self.recipe_service.Add.return_value = RecipeRef(id="recipe_id")
        self.objective_group_service.Add.return_value = ObjectiveGroupRef(id="objective_group_id")
        self.diet_service.Add.return_value = AddResponse(operation=OperationResponse())
        self.diet_service.ByUser.return_value = UserDietDefinition()
        self.user_service.FindByHandle.return_value = User()
        self.curated_diet_service.Get.return_value = CuratedDiet()
        # Prepare the request
        request = InitialLoginForm(
            remoteUserId="remote_user_id",
            meals=[
                MealInit(
                    name="Breakfast",
                    mealPref=MealStructurePreference.ownRecipe,
                    ownRecipeIngredients=[],
                    useKcal=True,
                    mealKcalMin=500,
                    mealKcalMax=700,
                    mealSize=MealSize.normal
                )
            ]
        )

        # Call the method under test
        response = self.login_service.SetupUser(request, context=MagicMock())

        # Assertions
        self.user_service.Add.assert_called_once()
        self.meal_service.Add.assert_called()
        self.objective_group_service.Add.assert_called()
        self.diet_service.Add.assert_called_once()
        self.assertIsNotNone(response)

    def test_create_own_recipe(self):
        # Prepare a meal with own recipe
        own_recipe_ingredients = [
            QuantifiedRecipeIngredient(food=FoodRef(properties=[Tag(name=self.localized_kcal_string, value=150)]),
                                       quantity=250),
            QuantifiedRecipeIngredient(food=FoodRef(properties=[Tag(name=self.localized_kcal_string, value=100)]),
                                       quantity=200),
        ]
        meal = MealInit(
            name="Lunch",
            mealPref=MealStructurePreference.ownRecipe,
            ownRecipeIngredients=own_recipe_ingredients,  # Add mock ingredients if needed
            useKcal=False,
            mealSize=MealSize.big
        )

        # Call the method under test
        recipe = GrpcLoginService.construct_own_recipe(meal, UserRef(id="bab"))
        self.assertAlmostEqual(recipe.quantified.min, 450 * 0.99)
        self.assertAlmostEqual(recipe.quantified.max, 450 * 1.01)
        self.assertEqual(recipe.name, "My standard lunch")
        self.assertEqual(recipe.quantified.ingredients, own_recipe_ingredients)

    def test_should_use_kcal(self):
        # Test cases
        meal_own_recipe = MealInit(
            name="Dinner",
            mealPref=MealStructurePreference.ownRecipe,
            useKcal=False
        )
        meal_use_kcal = MealInit(
            name="Snack",
            mealPref=MealStructurePreference.generated,
            useKcal=True
        )
        meal_no_kcal = MealInit(
            name="Dessert",
            mealPref=MealStructurePreference.generated,
            useKcal=False
        )

        # Assertions
        self.assertTrue(GrpcLoginService.should_use_kcal(meal_own_recipe))
        self.assertTrue(GrpcLoginService.should_use_kcal(meal_use_kcal))
        self.assertFalse(GrpcLoginService.should_use_kcal(meal_no_kcal))

    def test_kcal_bounds_for_meal(self):
        # Meal with own recipe
        meal_own_recipe = MealInit(
            name="Dinner",
            mealPref=MealStructurePreference.ownRecipe,
            ownRecipeIngredients=[
                QuantifiedRecipeIngredient(food=FoodRef(properties=[
                    Tag(name=self.localized_kcal_string, value=84)
                ]), quantity=17)
            ],  # Mock ingredients with kcal values if needed
            useKcal=False
        )

        # Meal with kcal specified
        meal_with_kcal = MealInit(
            name="Snack",
            mealPref=MealStructurePreference.generated,
            useKcal=True,
            mealKcalMin=200,
            mealKcalMax=300
        )

        # Meal without kcal (should raise ValueError)
        meal_no_kcal = MealInit(
            name="Dessert",
            mealPref=MealStructurePreference.generated,
            useKcal=False
        )

        # Call the method under test
        min_kcal, max_kcal = self.login_service.kcal_bounds_for_meal(meal_own_recipe)
        self.assertAlmostEqual(min_kcal, .17 * 84 * 0.99)
        self.assertAlmostEqual(max_kcal, .17 * 84 * 1.01)

        min_kcal, max_kcal = self.login_service.kcal_bounds_for_meal(meal_with_kcal)
        self.assertEqual(min_kcal, 200)
        self.assertEqual(max_kcal, 300)

        with self.assertRaises(ValueError):
            self.login_service.kcal_bounds_for_meal(meal_no_kcal)

    def test_infer_meal_sides(self):
        meal = MealInit(
            name="Lunch",
            sideDishes=BoolConceptValues(
                conceptValues={
                    "salad_concept_id": True,
                    "bread_concept_id": False
                }
            )
        )
        sides = GrpcLoginService.infer_meal_sides(meal, self.concepts, self.tags)
        expected_concept_values = {
            self.concepts.root.id: False,
            "salad_concept_id": True,
            "bread_concept_id": False
        }
        self.assertEqual(sides.conceptValues, expected_concept_values)
        self.assertEqual(sides.tagPreferences[0].tag, self.tags.side_dish)
        self.assertEqual(len(sides.tagPreferences), 1)
        self.assertTrue(sides.tagPreferences[0].status)

    def test_create_smart_meal(self):
        meal = MealInit(
            name="Dinner",
            mealPref=MealStructurePreference.generated,
            smart=SmartRecipePreferences(
                enabled=True,
                categories=[RecipeCategoryRef(id="Category1")],
                cuisines=[RecipeCuisineRef(id="Cuisine1")],
                minTime=10,
                maxTime=30,
                accuracy=SmartRecipeAccuracyPreference(exact=True),
                concepts=BoolConceptValues(
                    tagPreferences=[ConceptTagStatus(tag=ConceptTagRef(id="2"), status=True)],
                    conceptValues={"x": True}
                )
            ),
            sideDishes=BoolConceptValues(
                conceptValues={
                    "vegetable_concept_id": True
                }
            ),
            mealSize=MealSize.normal
        )

        user_ref = UserRef(id="user_id")
        created_meal = GrpcLoginService.create_smart_meal(meal, user_ref, self.concepts, self.tags)

        # Assertions
        self.assertEqual(created_meal.name, "Dinner")
        self.assertEqual(created_meal.owner, user_ref)
        self.assertTrue(created_meal.balanced)
        self.assertIsNotNone(created_meal.smartRecipes)
        smart_concepts = created_meal.smartRecipes.concepts.conceptValues
        self.assertFalse(smart_concepts[self.concepts.root.id])
        self.assertTrue(smart_concepts[self.concepts.pantry.id])
        self.assertTrue(smart_concepts[self.concepts.fat.id])
        self.assertTrue(smart_concepts[self.concepts.water.id])
        side_concepts = created_meal.concepts.conceptValues
        self.assertFalse(side_concepts[self.concepts.root.id])
        self.assertTrue(side_concepts["vegetable_concept_id"])

    def test_create_all_objective_groups(self):
        request = InitialLoginForm(
            remoteUserId="remote_user_id",
            meals=[
                MealInit(useKcal=False),
                MealInit(useKcal=True),
            ]
        )
        all_meal_refs = [MealRef(id="meal1"), MealRef(id="meal2")]
        user_ref = UserRef(id="user_id")
        reqs = self.use_case.calculate(request)

        objective_groups = GrpcLoginService.create_all_objective_groups(
            request,
            all_meal_refs,
            reqs,
            self.properties,
            self.application_levels,
            user_ref,
            self.property_resolver
        )

        # Assertions
        self.assertIsInstance(objective_groups, list)
        self.assertGreater(len(objective_groups), 3)

    def test_create_diet(self):
        request = InitialLoginForm(
            meals=[
                MealInit(
                    name="Breakfast",
                    mealPref=MealStructurePreference.generated,
                    useKcal=False,
                    mealSize=MealSize.small
                )
            ]
        )
        curated_diet = CuratedDiet()
        admin_diet = UserDietDefinition()
        user_ref = UserRef(id="user_id")
        all_meal_refs = [MealRef(id="meal_id")]
        target_objective_groups = [ObjectiveGroupRef(id="objective_group_id")]
        meal_balancing_properties = [PropertyRef(id="property_id")]

        user_diet = GrpcLoginService.create_diet(
            request,
            curated_diet,
            admin_diet,
            user_ref,
            all_meal_refs,
            target_objective_groups,
            meal_balancing_properties
        )

        # Assertions
        self.assertEqual(user_diet.owner, user_ref)
        self.assertEqual(user_diet.objectiveGroups, target_objective_groups)
        self.assertEqual(user_diet.mealSizes.sizes[0].meal, all_meal_refs[0])
        self.assertEqual(user_diet.mealSizes.sizes[0].size, 0.5)

    # Additional tests for methods like create_absolute_requirement, create_kcal_ratio_requirement, etc.,
    # can be added similarly, ensuring thorough coverage of the GrpcLoginService class.


if __name__ == '__main__':
    unittest.main()
