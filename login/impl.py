import grpc

from com.baboea.concept_pb2 import PortionConceptValues, PortionSize
from com.baboea.models.curated_diet_pb2 import CuratedDiet
from com.baboea.models.days_pb2 import MealPlanDay
from com.baboea.models.diet_pb2 import UserDietDefinition, ClientMealSize, MealSizes
from com.baboea.models.meal_pb2 import Meal, MealRef
from com.baboea.models.objectivegroup_pb2 import SpecializedRequirement, MealSelection, RequirementConcepts, \
    ObjectiveGroup, ObjectiveGroupRef
from com.baboea.models.users_pb2 import UserRef, User
from com.baboea.services.application_level_service_pb2_grpc import ApplicationLevelServiceStub
from com.baboea.services.base_pb2 import OperationResponse, AddResponse, FindSingleHandleRequest, GetRequest
from com.baboea.services.curated_diet_service_pb2_grpc import CuratedDietServiceStub
from com.baboea.services.diet_service_pb2_grpc import UserDietServiceStub
from com.baboea.services.login_service_pb2 import InitialLoginForm, LoginRequest, LoginResponse, MealSize
from com.baboea.services.login_service_pb2_grpc import UserInitServiceServicer, LoginServiceStub
from com.baboea.services.meal_plan_day_service_pb2_grpc import MealPlanDayServiceStub
from com.baboea.services.meal_service_pb2_grpc import MealServiceStub
from com.baboea.services.objective_group_service_pb2_grpc import ObjectiveGroupServiceStub
from com.baboea.services.property_service_pb2_grpc import PropertyServiceStub
from com.baboea.services.user_service_pb2_grpc import UserServiceStub
from login.bmr import BmrUseCase
from login.nutrients import NUTRIENT_DATA


class GrpcLoginService(UserInitServiceServicer):

    def __init__(self, channel: grpc.Channel, use_case: BmrUseCase):
        self.use_case = use_case
        self.meal_service: MealServiceStub = MealServiceStub(channel)
        self.day_service: MealPlanDayServiceStub = MealPlanDayServiceStub(channel)
        self.user_service: UserServiceStub = UserServiceStub(channel)
        self.objective_group_service: ObjectiveGroupServiceStub = ObjectiveGroupServiceStub(channel)
        self.diet_service: UserDietServiceStub = UserDietServiceStub(channel)
        self.property_service: PropertyServiceStub = PropertyServiceStub(channel)
        self.application_service: ApplicationLevelServiceStub = ApplicationLevelServiceStub(channel)
        self.curated_diet: CuratedDietServiceStub = CuratedDietServiceStub(channel)

    def SetupUser(self, request: InitialLoginForm, context) -> OperationResponse:
        print("Adding user:)")
        response: AddResponse = self.user_service.Add(
            User(externalId=request.remoteUserId, name=request.personal.name))
        user: UserRef = UserRef(id=response.id)
        #         Create meals
        print("User id is", user)
        all_meal_refs = []
        for meal in request.meals:
            created_meal = Meal(
                name=meal.name,
                description="",
                owner=user,
                smartRecipes=meal.smart,
                concepts=meal.sideDishes
            )
            add: AddResponse = self.meal_service.Add(created_meal)
            all_meal_refs.append(MealRef(id=add.id))
        #         Create days

        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            self.day_service.Add(MealPlanDay(
                name=day,
                meals=all_meal_refs,
                owner=user,
                description=""
            ))
        #         Create objectives
        targets = self.use_case.calculate(request)
        kcal_prop = self.property_service.ByHandleOrCreate(FindSingleHandleRequest(handle="kcal"))
        carb_prop = self.property_service.ByHandleOrCreate(FindSingleHandleRequest(handle="net_carbs"))
        protein_prop = self.property_service.ByHandleOrCreate(FindSingleHandleRequest(handle="protein"))
        application_level_day = self.application_service.ByHandleOrCreate(FindSingleHandleRequest(handle="day"))
        kcal_req = SpecializedRequirement(
            applicationLevel=application_level_day,
            numerator=kcal_prop,
            useRatio=False,
            useMax=True,
            useMin=True,
            min=targets.minKcal,
            max=targets.maxKcal,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True)
        )
        protein_req = SpecializedRequirement(
            applicationLevel=application_level_day,
            numerator=protein_prop,
            useRatio=False,
            useMax=True,
            useMin=True,
            min=targets.minProtein,
            max=targets.maxProtein,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True)
        )
        carb_req = SpecializedRequirement(
            applicationLevel=application_level_day,
            numerator=carb_prop,
            denominator=kcal_prop,
            useRatio=True,
            useMax=True,
            useMin=True,
            min=targets.minCarbPercentage,
            max=targets.maxCarbPercentage,
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
            scaleNumerator=4,
            scaleDenominator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True),
            denominatorConcepts=RequirementConcepts(useAllConcepts=True)
        )
        macro_response: AddResponse = self.objective_group_service.Add(
            ObjectiveGroup(name="Macros", description="Applies your desired macros to every day", owner=user,
                           objectives=[kcal_req, protein_req, carb_req]))
        diet: CuratedDiet = self.curated_diet.Get(GetRequest(id=request.diet.id))
        sizes = {
            MealSize.big: 1.5,
            MealSize.normal: 1.0,
            MealSize.small: 0.5
        }
        meal_sizes = [ClientMealSize(meal=all_meal_refs[index], size=sizes[meal.mealSize]) for index, meal in
                      enumerate(request.meals) if not meal.useKcal]
        target_objective_groups = [ObjectiveGroupRef(id=macro_response.id)]
        if meal_sizes:
            meal_kcal_overrides = [SpecializedRequirement(
                min=meal.mealKcalMin,
                max=meal.mealKcalMax,
                numeratorMeals=MealSelection(
                    useAllDays=True,
                    useAllComponents=True,
                    meals=[all_meal_refs[index]]
                ),
                scaleNumerator=1.0,
                applicationLevel=application_level_day,
                useRatio=False,
                useMax=True,
                useMin=True,
                numerator=kcal_prop,
                numeratorConcepts=RequirementConcepts(useAllConcepts=True)
            ) for index, meal in
                enumerate(request.meals) if meal.useKcal]
            meal_add_response = self.objective_group_service.Add(
                ObjectiveGroup(name="Custom meal sizes",
                               description="Applies specific calories to some (or all) of your meals", owner=user,
                               objectives=meal_kcal_overrides))
            target_objective_groups.append(ObjectiveGroupRef(id=meal_add_response.id))
        nutrient_targets = [SpecializedRequirement(
            applicationLevel=application_level_day,
            min=x.min,
            max=x.max,
            useMin=True,
            useMax=x.max is not None,
            numerator=self.property_service.ByHandleOrCreate(FindSingleHandleRequest(handle=x.nutrient1)),
            denominator=kcal_prop,
            useRatio=False,
            numeratorMeals=MealSelection(useAllMeals=True, useAllDays=True, useAllComponents=True),
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True)
        ) for x in NUTRIENT_DATA.objectives]
        nutrient_targets.append(SpecializedRequirement(
            applicationLevel=application_level_day,
            min=targets.minFiber,
            max=targets.maxFiber,
            useMin=True,
            useMax=False,
            numerator=self.property_service.ByHandleOrCreate(FindSingleHandleRequest(handle="fiber")),
            denominator=kcal_prop,
            useRatio=False,
            numeratorMeals=MealSelection(useAllMeals=True, useAllDays=True, useAllComponents=True),
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True)
        ))
        nutrient_add: AddResponse = self.objective_group_service.Add(ObjectiveGroup(
            name=NUTRIENT_DATA.name,
            description=NUTRIENT_DATA.description,
            objectives=nutrient_targets,
            owner=user
        ))
        target_objective_groups.append(ObjectiveGroupRef(id=nutrient_add.id))
        target_portions: User = self.user_service.FindByHandle(FindSingleHandleRequest(handle="admin"))
        by_user: UserDietDefinition = self.diet_service.ByUser(UserRef(id=target_portions.id))
        result: AddResponse = self.diet_service.Add(UserDietDefinition(
            owner=user,
            objectiveGroups=target_objective_groups,
            portionSizes=by_user.portionSizes,
            concepts=diet.concepts, mealSizes=MealSizes(sizes=meal_sizes)
        ))
        return result.operation
