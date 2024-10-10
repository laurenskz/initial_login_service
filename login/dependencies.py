from abc import ABC
from dataclasses import dataclass
from typing import Dict

from com.baboea.models.concept_tag_pb2 import ConceptTagRef
from com.baboea.models.concepts_pb2 import ConceptRef
from com.baboea.models.meal_pb2 import Meal, MealRef
from com.baboea.models.objectivegroup_pb2 import ApplicationLevelRef, ObjectiveGroup, ObjectiveGroupRef
from com.baboea.models.property_pb2 import PropertyRef
from com.baboea.models.users_pb2 import UserRef, User
from com.baboea.services.base_pb2 import FindSingleHandleRequest
from com.baboea.services.property_service_pb2_grpc import PropertyServiceStub


@dataclass
class InitProperties:
    kcal: PropertyRef
    fat: PropertyRef
    protein: PropertyRef
    fiber: PropertyRef
    net_carbs: PropertyRef
    recipe_count: PropertyRef
    food_weight: PropertyRef


@dataclass
class ApplicationLevels:
    meal: ApplicationLevelRef
    day: ApplicationLevelRef


@dataclass
class Concepts:
    root: ConceptRef
    water: ConceptRef
    pantry: ConceptRef
    fat: ConceptRef
    fruit: ConceptRef
    vegetable: ConceptRef


@dataclass
class ConceptTags:
    common_item: ConceptTagRef
    side_dish: ConceptTagRef


class PropertyByHandleResolver(ABC):

    def resolve(self, handle: str) -> PropertyRef:
        pass


class GrpcPropertyByHandleResolver(PropertyByHandleResolver):

    def __init__(self, service: PropertyServiceStub):
        self.service = service
        self.cache: Dict[str, PropertyRef] = {}

    def resolve(self, handle: str) -> PropertyRef:
        if handle in self.cache:
            return self.cache[handle]
        prop = self.service.ByHandleOrCreate(FindSingleHandleRequest(handle=handle))
        self.cache[handle] = prop
        return prop


class UnitTestPropertyResolver(PropertyByHandleResolver):

    def resolve(self, handle: str) -> PropertyRef:
        return PropertyRef(id=handle)
