import grpc
from prometheus_client import Counter, Histogram
from loguru import logger
from typing import List, Dict, Tuple, Optional, Iterable
from com.baboea.concept_pb2 import PortionConceptValues, PortionSize, BoolConceptValues, ConceptTagStatus
from com.baboea.models.concepts_pb2 import Concept, ConceptRef
from com.baboea.models.curated_diet_pb2 import CuratedDiet
from com.baboea.models.days_pb2 import MealPlanDay
from com.baboea.models.diet_pb2 import UserDietDefinition, ClientMealSize, MealSizes
from com.baboea.models.meal_pb2 import Meal, MealRef, SmartRecipePreferences
from com.baboea.models.objectivegroup_pb2 import SpecializedRequirement, MealSelection, RequirementConcepts, \
    ObjectiveGroup, ObjectiveGroupRef
from com.baboea.models.property_pb2 import PropertyRef
from com.baboea.models.recipes_pb2 import QuantifiedRecipe, Recipe, RecipeRef, QuantifiedRecipeIngredient
from com.baboea.models.users_pb2 import UserRef, User
from com.baboea.services.application_level_service_pb2_grpc import ApplicationLevelServiceStub
from com.baboea.services.base_pb2 import OperationResponse, AddResponse, FindSingleHandleRequest, GetRequest
from com.baboea.services.concept_service_pb2_grpc import ConceptServiceStub
from com.baboea.services.curated_diet_service_pb2_grpc import CuratedDietServiceStub
from com.baboea.services.diet_service_pb2_grpc import UserDietServiceStub
from com.baboea.services.login_service_pb2 import InitialLoginForm, LoginRequest, LoginResponse, MealSize, \
    MealStructurePreference, MealInit
from com.baboea.services.login_service_pb2_grpc import UserInitServiceServicer, LoginServiceStub
from com.baboea.services.meal_plan_day_service_pb2_grpc import MealPlanDayServiceStub
from com.baboea.services.meal_service_pb2_grpc import MealServiceStub
from com.baboea.services.objective_group_service_pb2_grpc import ObjectiveGroupServiceStub
from com.baboea.services.property_service_pb2_grpc import PropertyServiceStub
from com.baboea.services.recipe_service_pb2_grpc import RecipeServiceStub
from com.baboea.services.user_service_pb2_grpc import UserServiceStub
from login.bmr import BmrUseCase, UserReqs
from login.dependencies import Concepts, ConceptTags, InitProperties, ApplicationLevels, PropertyByHandleResolver
from login.nutrients import NUTRIENT_DATA, VitaminsAndMinerals


class GrpcLoginService(UserInitServiceServicer):
    # Define Prometheus metrics
    users_setup_counter = Counter('users_setup_total', 'Total number of users set up')
    setup_user_duration_histogram = Histogram('setup_user_duration_seconds', 'Time spent setting up a user')

    def __init__(
            self,
            channel: grpc.Channel,
            use_case: BmrUseCase,
            concepts: Concepts,
            tags: ConceptTags,
            application_levels: ApplicationLevels,
            properties: InitProperties,
            property_resolver: PropertyByHandleResolver,
            meal_service: Optional[MealServiceStub] = None,
            quantified_recipes: Optional[RecipeServiceStub] = None,
            concept_service: Optional[ConceptServiceStub] = None,
            day_service: Optional[MealPlanDayServiceStub] = None,
            user_service: Optional[UserServiceStub] = None,
            objective_group_service: Optional[ObjectiveGroupServiceStub] = None,
            diet_service: Optional[UserDietServiceStub] = None,
            application_service: Optional[ApplicationLevelServiceStub] = None,
            curated_diet: Optional[CuratedDietServiceStub] = None,

    ):
        self.property_resolver = property_resolver
        self.concepts = concepts
        self.tags = tags
        self.properties = properties
        self.application_levels = application_levels
        self.use_case = use_case
        self.meal_service = meal_service or MealServiceStub(channel)
        self.quantified_recipes = quantified_recipes or RecipeServiceStub(channel)
        self.concept_service = concept_service or ConceptServiceStub(channel)
        self.day_service = day_service or MealPlanDayServiceStub(channel)
        self.user_service = user_service or UserServiceStub(channel)
        self.objective_group_service = objective_group_service or ObjectiveGroupServiceStub(channel)
        self.diet_service = diet_service or UserDietServiceStub(channel)
        self.application_service = application_service or ApplicationLevelServiceStub(channel)
        self.curated_diet = curated_diet or CuratedDietServiceStub(channel)

    def SetupUser(self, request: InitialLoginForm, context) -> OperationResponse:
        response: AddResponse = self.user_service.Add(
            User(externalId=request.remoteUserId, name=request.personal.name))
        user: UserRef = UserRef(id=response.id)
        logger.bind(user=user).info(f"User created with ID: {user.id}")
        with GrpcLoginService.setup_user_duration_histogram.time():
            try:
                operation_response = self.initialize_user(request, user)
                logger.bind(user=user).info("Successfully setup user")
            except Exception:
                logger.bind(user=user).exception("Failed to setup user")
        GrpcLoginService.users_setup_counter.inc()
        return operation_response

    def initialize_user(self, request: InitialLoginForm, user: UserRef) -> OperationResponse:
        all_meal_refs = self.create_meals(request, user)
        self.create_days(user, all_meal_refs)
        target_objective_groups = self.create_objectives(request, all_meal_refs, user)
        # Get portion sizes from admin user
        user_diet = self.create_diet(request, self.load_curated_diet(request), self.load_admin_diet(), user,
                                     all_meal_refs, target_objective_groups,
                                     GrpcLoginService.get_meal_balancing_properties(self.properties))
        operation_response: AddResponse = self.diet_service.Add(user_diet)
        return operation_response.operation

    def load_admin_diet(self) -> UserDietDefinition:
        admin_user: User = self.user_service.FindByHandle(FindSingleHandleRequest(handle="admin"))
        return self.diet_service.ByUser(UserRef(id=admin_user.id))

    def load_curated_diet(self, request: InitialLoginForm) -> CuratedDiet:
        return self.curated_diet.Get(GetRequest(id=request.diet.id))

    def create_meals(self, request: InitialLoginForm, user: UserRef) -> List[MealRef]:
        all_meal_refs = []
        for idx, meal in enumerate(request.meals):
            if meal.mealPref == MealStructurePreference.ownRecipe:
                recipe_ref = self.create_own_recipe(meal)
                created_meal = Meal(
                    name=meal.name,
                    recipes=[recipe_ref],
                    balanced=False,
                )
            else:
                created_meal = self.create_smart_meal(meal, user, self.concepts, self.tags)
            add_response = self.meal_service.Add(created_meal)
            all_meal_refs.append(MealRef(id=add_response.id))

        return all_meal_refs

    @staticmethod
    def calculate_own_recipe_kcal(ingredients: Iterable[QuantifiedRecipeIngredient]) -> float:
        return sum(
            prop.value * ingredient.quantity / 100
            for ingredient in ingredients
            for prop in ingredient.food.properties
            if any("kcal" == x.value.lower() for x in prop.name.languages)
        )

    @staticmethod
    def calculate_own_recipe_weight(ingredients: Iterable[QuantifiedRecipeIngredient]) -> float:
        return sum(i.quantity for i in ingredients)

    @staticmethod
    def construct_own_recipe(meal: MealInit) -> Recipe:
        total_weight = GrpcLoginService.calculate_own_recipe_weight(meal.ownRecipeIngredients)
        quantified_recipe = QuantifiedRecipe(
            ingredients=meal.ownRecipeIngredients,
            min=total_weight * 0.99,
            max=total_weight * 1.01
        )
        return Recipe(
            name=f"My standard {meal.name.lower()}",
            quantified=quantified_recipe
        )

    def create_own_recipe(self, meal: MealInit) -> RecipeRef:
        recipe_response = self.quantified_recipes.Add(
            GrpcLoginService.construct_own_recipe(meal)
        )
        return RecipeRef(id=recipe_response.id)

    @staticmethod
    def should_use_kcal(meal: MealInit) -> bool:
        return meal.useKcal or meal.mealPref == MealStructurePreference.ownRecipe

    @staticmethod
    def kcal_bounds_for_meal(meal: MealInit) -> Tuple[float, float]:
        if meal.mealPref == MealStructurePreference.ownRecipe:
            return GrpcLoginService.infer_kcal_from_user_recipe(meal)
        if not meal.useKcal:
            raise ValueError(f"Trying to compute bounds for a meal that should not use bounds {meal.name}")
        return meal.mealKcalMin, meal.mealKcalMax

    @staticmethod
    def infer_kcal_from_user_recipe(meal: MealInit) -> Tuple[float, float]:
        kcal = GrpcLoginService.calculate_own_recipe_kcal(meal.ownRecipeIngredients)
        return kcal * 0.99, kcal * 1.01

    @staticmethod
    def selected_concepts_without_root(meal: MealInit, concepts: Concepts) -> Dict[str, bool]:
        selected_items = {k: v for k, v in meal.sideDishes.conceptValues.items()}
        return {concepts.root.id: False, **selected_items}

    @staticmethod
    def infer_meal_sides(meal: MealInit, concepts: Concepts, tags: ConceptTags) -> BoolConceptValues:
        return BoolConceptValues(
            tagPreferences=[ConceptTagStatus(tag=tags.side_dish, status=True)],
            conceptValues=GrpcLoginService.selected_concepts_without_root(meal, concepts)
        )

    @staticmethod
    def infer_meal_smart_recipe(meal: MealInit, concepts: Concepts) -> SmartRecipePreferences:
        return SmartRecipePreferences(
            enabled=meal.smart.enabled,
            categories=meal.smart.categories,
            cuisines=meal.smart.cuisines,
            minTime=meal.smart.minTime,
            maxTime=meal.smart.maxTime,
            accuracy=meal.smart.accuracy,
            concepts=BoolConceptValues(
                conceptValues={concepts.water.id: True, concepts.pantry.id: True, concepts.fat.id: True,
                               **GrpcLoginService.selected_concepts_without_root(meal, concepts)},
                tagPreferences=meal.smart.concepts.tagPreferences
            )
        )

    @staticmethod
    def create_smart_meal(meal: MealInit, user: UserRef, concepts: Concepts, tags: ConceptTags) -> Meal:
        return Meal(
            name=meal.name,
            description="",
            owner=user,
            smartRecipes=GrpcLoginService.infer_meal_smart_recipe(meal, concepts),
            concepts=GrpcLoginService.infer_meal_sides(meal, concepts, tags),
            balanced=meal.name in ["Breakfast", "Lunch", "Dinner"]
        )

    def create_days(self, user: UserRef, all_meal_refs: List[MealRef]):
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            self.day_service.Add(MealPlanDay(
                name=day,
                meals=all_meal_refs,
                owner=user,
                description=""
            ))

    @staticmethod
    def create_all_objective_groups(
            request: InitialLoginForm,
            all_meal_refs: List[MealRef],
            reqs: UserReqs,
            properties: InitProperties,
            application_levels: ApplicationLevels,
            user: UserRef,
            resolver: PropertyByHandleResolver
    ) -> List[ObjectiveGroup]:
        macros = ObjectiveGroup(
            name="Macros",
            description="Applies your desired macros to every day",
            owner=user,
            objectives=[
                GrpcLoginService.create_fat_requirement(reqs, properties, application_levels),
                GrpcLoginService.create_fiber_requirement(reqs, properties, application_levels),
                GrpcLoginService.create_kcal_requirement(reqs, properties, application_levels),
                GrpcLoginService.create_protein_requirement(reqs, properties, application_levels),
                GrpcLoginService.create_carb_requirement(reqs, properties, application_levels),
            ]
        )
        objective_groups = [
            macros,
            GrpcLoginService.create_nutrient_targets(NUTRIENT_DATA, resolver, application_levels, user),
            GrpcLoginService.create_recipe_preferences_objective(properties, application_levels, user)
        ]
        custom_meal_sizes = GrpcLoginService.maybe_create_custom_meal_sizes(request, all_meal_refs, user, properties,
                                                                            application_levels)
        if custom_meal_sizes:
            objective_groups.append(custom_meal_sizes)
        return objective_groups

    def create_objectives(
            self,
            request: InitialLoginForm,
            all_meal_refs: List[MealRef],
            user: UserRef,
    ) -> List[ObjectiveGroupRef]:
        return [
            ObjectiveGroupRef(id=self.objective_group_service.Add(x).id)
            for x in GrpcLoginService.create_all_objective_groups(
                request,
                all_meal_refs,
                self.use_case.calculate(request),
                self.properties,
                self.application_levels,
                user,
                self.property_resolver)
        ]

    @staticmethod
    def create_meal_kcal_bound_req(meal: MealInit, meal_ref: MealRef,
                                   application_levels: ApplicationLevels,
                                   properties: InitProperties) -> SpecializedRequirement:
        min_kcal, max_kcal = GrpcLoginService.kcal_bounds_for_meal(meal)
        return SpecializedRequirement(
            min=min_kcal,
            max=max_kcal,
            numeratorMeals=MealSelection(
                useAllDays=True,
                useAllComponents=True,
                meals=[meal_ref]
            ),
            scaleNumerator=1.0,
            applicationLevel=application_levels.day,
            useRatio=False,
            useMax=True,
            useMin=True,
            numerator=properties.kcal,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True)
        )

    @staticmethod
    def maybe_create_custom_meal_sizes(request: InitialLoginForm,
                                       all_meal_refs: List[MealRef],
                                       user: UserRef,
                                       properties: InitProperties,
                                       application_levels: ApplicationLevels) -> Optional[ObjectiveGroup]:
        if any(GrpcLoginService.should_use_kcal(m) for m in request.meals):
            return ObjectiveGroup(
                name="Custom meal sizes",
                description="Applies specific calories to some (or all) of your meals",
                owner=user,
                objectives=GrpcLoginService.create_meal_kcal_overrides(request, all_meal_refs, properties,
                                                                       application_levels)
            )
        return None

    @staticmethod
    def create_meal_kcal_overrides(
            request: InitialLoginForm,
            all_meal_refs: List[MealRef],
            properties: InitProperties,
            application_levels: ApplicationLevels
    ) -> List[SpecializedRequirement]:
        meal_kcal_overrides = []
        for index, meal in enumerate(request.meals):
            if GrpcLoginService.should_use_kcal(meal):
                meal_kcal_override = GrpcLoginService.create_meal_kcal_bound_req(meal, all_meal_refs[index],
                                                                                 application_levels, properties)
                meal_kcal_overrides.append(meal_kcal_override)
        return meal_kcal_overrides

    @staticmethod
    def create_diet(
            request: InitialLoginForm,
            curated: CuratedDiet,
            admin_diet: UserDietDefinition,
            user: UserRef,
            all_meal_refs: List[MealRef],
            target_objective_groups: List[ObjectiveGroupRef],
            meal_balancing_properties: List[PropertyRef]
    ) -> UserDietDefinition:
        sizes = {
            MealSize.big: 1.5,
            MealSize.normal: 1.0,
            MealSize.small: 0.5
        }
        meal_sizes = [
            ClientMealSize(
                meal=all_meal_refs[index],
                size=sizes[meal.mealSize]
            ) for index, meal in enumerate(request.meals) if not GrpcLoginService.should_use_kcal(meal)
        ]

        # Add diet definition
        return UserDietDefinition(
            owner=user,
            objectiveGroups=target_objective_groups,
            portionSizes=admin_diet.portionSizes,
            concepts=curated.concepts,
            mealSizes=MealSizes(sizes=meal_sizes),
            mealBalancingProperties=meal_balancing_properties
        )

    @staticmethod
    def create_recipe_preferences_objective(properties: InitProperties,
                                            application_levels: ApplicationLevels, user: UserRef) -> ObjectiveGroup:
        return ObjectiveGroup(
            name="Recipe preferences",
            description="We have set the maximum number of recipes you have to make per meal to 1. Feel free to adjust",
            owner=user,
            objectives=[GrpcLoginService.create_recipe_count_requirement(properties, application_levels)]
        )

    @staticmethod
    def create_recipe_count_requirement(properties: InitProperties,
                                        application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.meal,
            numerator=properties.recipe_count,
            useRatio=False,
            useMax=True,
            useMin=True,
            min=0,
            max=1,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True)
        )

    @staticmethod
    def create_kcal_requirement(targets: UserReqs, properties: InitProperties,
                                application_levels: ApplicationLevels) -> SpecializedRequirement:
        return GrpcLoginService.create_absolute_requirement(min_value=targets.minKcal, max_value=targets.maxKcal,
                                                            selected_property=properties.kcal,
                                                            application_levels=application_levels)

    @staticmethod
    def create_fiber_requirement(targets: UserReqs, properties: InitProperties,
                                 application_levels: ApplicationLevels) -> SpecializedRequirement:
        return GrpcLoginService.create_absolute_requirement(min_value=targets.minFiber, max_value=targets.maxFiber,
                                                            selected_property=properties.fiber,
                                                            application_levels=application_levels)

    @staticmethod
    def create_protein_requirement(targets: UserReqs, properties: InitProperties,
                                   application_levels: ApplicationLevels) -> SpecializedRequirement:
        return GrpcLoginService.create_absolute_requirement(min_value=targets.minProtein, max_value=targets.maxProtein,
                                                            selected_property=properties.protein,
                                                            application_levels=application_levels)

    @staticmethod
    def create_absolute_requirement(min_value: Optional[float], max_value: Optional[float],
                                    selected_property: PropertyRef,
                                    application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.day,
            numerator=selected_property,
            denominator=selected_property,
            useRatio=False,
            useMax=max_value is not None,
            useMin=min_value is not None,
            min=min_value or 0,
            max=max_value or 10000,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True),
        )

    @staticmethod
    def create_kcal_ratio_requirement(min_percentage: float, max_percentage: float, selected_property: PropertyRef,
                                      kcal_per_unit: float,
                                      properties: InitProperties,
                                      application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.day,
            numerator=selected_property,
            denominator=properties.kcal,
            useRatio=True,
            useMax=True,
            useMin=True,
            min=min_percentage,
            max=max_percentage,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            denominatorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=kcal_per_unit,
            scaleDenominator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True),
            denominatorConcepts=RequirementConcepts(useAllConcepts=True)
        )

    @staticmethod
    def create_fat_requirement(targets: UserReqs, properties: InitProperties,
                               application_levels: ApplicationLevels) -> SpecializedRequirement:
        return GrpcLoginService.create_kcal_ratio_requirement(min_percentage=targets.minFatPercentage,
                                                              max_percentage=targets.maxFatPercentage,
                                                              selected_property=properties.net_carbs, kcal_per_unit=9,
                                                              properties=properties,
                                                              application_levels=application_levels)

    @staticmethod
    def create_carb_requirement(targets: UserReqs, properties: InitProperties,
                                application_levels: ApplicationLevels) -> SpecializedRequirement:
        return GrpcLoginService.create_kcal_ratio_requirement(min_percentage=targets.minCarbPercentage,
                                                              max_percentage=targets.maxCarbPercentage,
                                                              selected_property=properties.net_carbs, kcal_per_unit=4,
                                                              properties=properties,
                                                              application_levels=application_levels)

    @staticmethod
    def create_nutrient_targets(data: VitaminsAndMinerals, property_resolver: PropertyByHandleResolver,
                                application_levels: ApplicationLevels, owner: UserRef) -> ObjectiveGroup:
        nutrient_targets = [
            GrpcLoginService.create_absolute_requirement(
                min_value=x.min,
                max_value=x.max,
                selected_property=property_resolver.resolve(x.nutrient1),
                application_levels=application_levels
            ) for x in data.objectives
        ]
        return ObjectiveGroup(name=data.name, description=data.description, objectives=nutrient_targets, owner=owner)

    @staticmethod
    def get_meal_balancing_properties(properties: InitProperties) -> List[PropertyRef]:
        return [
            properties.kcal,
            properties.protein,
            properties.fiber,
            properties.fat,
            properties.net_carbs
        ]
