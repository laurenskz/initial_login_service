import os
from dataclasses import dataclass

from grpc import insecure_channel
from injector import Module, singleton, provider

from com.baboea.models.concepts_pb2 import ConceptRef
from com.baboea.models.diet_pb2 import UserDietDefinition
from com.baboea.models.users_pb2 import User, UserRef
from com.baboea.services.application_level_service_pb2_grpc import ApplicationLevelServiceStub
from com.baboea.services.base_pb2 import FindSingleHandleRequest, GetRequest
from com.baboea.services.concept_service_pb2_grpc import ConceptServiceStub
from com.baboea.services.concept_tag_service_pb2_grpc import ConceptTagServiceStub
from com.baboea.services.curated_diet_service_pb2_grpc import CuratedDietServiceStub
from com.baboea.services.diet_service_pb2_grpc import UserDietServiceStub
from com.baboea.services.login_service_pb2_grpc import UserInitServiceServicer
from com.baboea.services.meal_plan_day_service_pb2_grpc import MealPlanDayServiceStub
from com.baboea.services.meal_service_pb2_grpc import MealServiceStub
from com.baboea.services.objective_group_service_pb2_grpc import ObjectiveGroupServiceStub
from com.baboea.services.property_service_pb2_grpc import PropertyServiceStub
from com.baboea.services.recipe_service_pb2_grpc import RecipeServiceStub
from com.baboea.services.template_recipe_service_pb2_grpc import ImprovedTemplateRecipeServiceStub
from com.baboea.services.user_service_pb2_grpc import UserServiceStub
from login.GrpcSimplifiedLoginService import GrpcSimplifiedLoginService
from login.bmr import BaseBmrUseCase
from login.bmr import BmrUseCase
from login.day_creator import BaseDayCreator
from login.dependencies import Concepts, ConceptTags, InitProperties, ApplicationLevels, PropertyByHandleResolver
from login.dependencies import GrpcPropertyByHandleResolver
from login.impl import GrpcLoginService
from login.meal_creator import BaseMealCreator
from login.nutrients import VitaminsAndMinerals, NUTRIENT_DATA
from login.objective_group_creator import BaseObjectiveGroupCreator
from login.simplified_setup import ObjectiveGroupCreator, MealCreator, DayCreator


class CreatorModule(Module):
    @singleton
    @provider
    def provide_objective_creator(self, b: BaseObjectiveGroupCreator) -> ObjectiveGroupCreator:
        return b

    @singleton
    @provider
    def provide_meal_creator(self, b: BaseMealCreator) -> MealCreator:
        return b

    @singleton
    @provider
    def provide_day_creator(self, b: BaseDayCreator) -> DayCreator:
        return b


class ObjectiveModule(Module):

    @singleton
    @provider
    def provide_vitamins_and_minerals(self) -> VitaminsAndMinerals:
        return NUTRIENT_DATA


@dataclass
class Locations:
    crud_address: str


class UseCaseModule(Module):

    @provider
    @singleton
    def provide_bmr(self, bmr: BaseBmrUseCase) -> BmrUseCase:
        return bmr

    @provider
    @singleton
    def provide_user_init_servicer(self, login: GrpcSimplifiedLoginService) -> UserInitServiceServicer:
        return login


class DataModule(Module):
    @provider
    @singleton
    def provide_init_properties(self, prop_service: PropertyServiceStub) -> InitProperties:
        return InitProperties(
            kcal=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="kcal")),
            protein=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="protein")),
            net_carbs=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="net_carbs")),
            fat=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="fat")),
            fiber=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="fiber")),
            recipe_count=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="recipe_count")),
            food_weight=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="food_weight"))
        )

    @provider
    @singleton
    def provide_concepts(self, concept_service: ConceptServiceStub) -> Concepts:
        return Concepts(
            root=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="root")).id),
            fat=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="fat")).id),
            pantry=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="pantry")).id),
            water=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="water")).id),
            fruit=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="fruit")).id),
            vegetable=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="vegetable")).id),
        )

    @provider
    @singleton
    def provide_tags(self, tag_service: ConceptTagServiceStub) -> ConceptTags:
        return ConceptTags(
            common_item=tag_service.ByHandleOrCreate(FindSingleHandleRequest(handle="common_supermarket")),
            side_dish=tag_service.ByHandleOrCreate(FindSingleHandleRequest(handle="normal_side_food")),
        )

    @provider
    @singleton
    def provide_application_levels(self, application_service: ApplicationLevelServiceStub) -> ApplicationLevels:
        return ApplicationLevels(
            meal=application_service.ByHandleOrCreate(FindSingleHandleRequest(handle="meal")),
            day=application_service.ByHandleOrCreate(FindSingleHandleRequest(handle="day")),
        )

    @provider
    @singleton
    def provide_admin_diet(self, user_service: UserServiceStub,
                           diet_service: UserDietServiceStub) -> UserDietDefinition:
        admin_user: User = user_service.FindByHandle(FindSingleHandleRequest(handle="admin"))
        return diet_service.ByUser(UserRef(id=admin_user.id))


class NetworkingModule(Module):

    @provider
    @singleton
    def property_resolver(self, resolver: GrpcPropertyByHandleResolver) -> PropertyByHandleResolver:
        return resolver

    @provider
    @singleton
    def provide_property_stub(self, locations: Locations) -> PropertyServiceStub:
        return PropertyServiceStub(insecure_channel(locations.crud_address))

    @singleton
    @provider
    def provide_template_recipe_stub(self, locations: Locations) -> ImprovedTemplateRecipeServiceStub:
        return ImprovedTemplateRecipeServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_concept_stub(self, locations: Locations) -> ConceptServiceStub:
        return ConceptServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_concept_tag_stub(self, locations: Locations) -> ConceptTagServiceStub:
        return ConceptTagServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_application_stub(self, locations: Locations) -> ApplicationLevelServiceStub:
        return ApplicationLevelServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_locations(self) -> Locations:
        return Locations(
            crud_address=os.getenv("CRUD_SERVICE_URL") or "localhost:50052"
        )

    @provider
    @singleton
    def provide_meal_service(self, locations: Locations) -> MealServiceStub:
        return MealServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_quantified_recipes(self, locations: Locations) -> RecipeServiceStub:
        return RecipeServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_day_service(self, locations: Locations) -> MealPlanDayServiceStub:
        return MealPlanDayServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_user_service(self, locations: Locations) -> UserServiceStub:
        return UserServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_objective_group_service(self, locations: Locations) -> ObjectiveGroupServiceStub:
        return ObjectiveGroupServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_diet_service(self, locations: Locations) -> UserDietServiceStub:
        return UserDietServiceStub(insecure_channel(locations.crud_address))

    @provider
    @singleton
    def provide_curated_diet(self, locations: Locations) -> CuratedDietServiceStub:
        return CuratedDietServiceStub(insecure_channel(locations.crud_address))
