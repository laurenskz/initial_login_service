from typing import Iterable, List

from injector import inject

from com.baboea.concept_pb2 import BoolConceptValues
from com.baboea.models.curated_diet_pb2 import CuratedDiet
from com.baboea.models.diet_pb2 import ClientMealSize, UserDietDefinition, MealSizes
from com.baboea.models.objectivegroup_pb2 import ObjectiveGroupRef
from com.baboea.models.property_pb2 import PropertyRef
from com.baboea.models.users_pb2 import User, UserRef
from com.baboea.services.base_pb2 import AddResponse, GetRequest
from com.baboea.services.curated_diet_service_pb2_grpc import CuratedDietServiceStub
from com.baboea.services.diet_service_pb2_grpc import UserDietServiceStub
from com.baboea.services.login_service_pb2 import InitialLoginForm
from com.baboea.services.login_service_pb2_grpc import UserInitServiceServicer
from com.baboea.services.user_service_pb2_grpc import UserServiceStub
from login.dependencies import InitProperties
from login.simplified_setup import ObjectiveGroupCreator, MealCreator, DayCreator


class GrpcSimplifiedLoginService(UserInitServiceServicer):
    @inject
    def __init__(self,
                 objective_creator: ObjectiveGroupCreator,
                 meal_creator: MealCreator,
                 day_creator: DayCreator,
                 user_service: UserServiceStub,
                 user_diet_service: UserDietServiceStub,
                 curated_diet_service: CuratedDietServiceStub,
                 admin_diet: UserDietDefinition,
                 props: InitProperties
                 ):
        super().__init__()
        self.user_diet_service = user_diet_service
        self.user_service = user_service
        self.objective_creator = objective_creator
        self.meal_creator = meal_creator
        self.day_creator = day_creator
        self.curated_diet_service = curated_diet_service
        self.admin_diet = admin_diet
        self.props = props

    def SetupUser(self, request: InitialLoginForm, context):
        print("Adding first user")
        try:
            self.create_user(request)
        except:
            print("Error while setting up user")

    def create_user(self, request):
        response: AddResponse = self.user_service.Add(
            User(externalId=request.remoteUserId, name=request.personal.name))
        user: UserRef = UserRef(id=response.id)
        meals_with_size = self.meal_creator.create_meals(user, request)
        objective_groups = self.objective_creator.create_user(user, request)
        days = self.day_creator.create_meals(user, request, [m.meal for m in meals_with_size])
        self.user_diet_service.Add(
            self.create_diet(
                request,
                self.curated_diet_service.Get(GetRequest(id=request.diet.id)),
                admin_diet=self.admin_diet,
                user=user,
                all_meals=meals_with_size,
                target_objective_groups=objective_groups,
                meal_balancing_properties=self.get_meal_balancing_properties(self.props)
            )
        )

    def create_diet(
            self,
            request: InitialLoginForm,
            curated: CuratedDiet,
            admin_diet: UserDietDefinition,
            user: UserRef,
            all_meals: Iterable[ClientMealSize],
            target_objective_groups: Iterable[ObjectiveGroupRef],
            meal_balancing_properties: Iterable[PropertyRef]
    ) -> UserDietDefinition:
        # Add diet definition
        return UserDietDefinition(
            owner=user,
            objectiveGroups=target_objective_groups,
            portionSizes=admin_diet.portionSizes,
            concepts=BoolConceptValues(
                conceptValues={
                    **{food: not b for food, b in request.hatedFoods.conceptValues.items() if b},
                    **curated.concepts.conceptValues
                }, tagPreferences=curated.concepts.tagPreferences
            ),
            mealSizes=MealSizes(sizes=all_meals),
            mealBalancingProperties=meal_balancing_properties
        )

    def get_meal_balancing_properties(self, properties: InitProperties) -> List[PropertyRef]:
        return [
            properties.kcal,
            properties.protein,
            properties.fiber,
            properties.fat,
            properties.net_carbs
        ]

    def StreamWithMe(self, request_iterator, context):
        return super().StreamWithMe(request_iterator, context)
