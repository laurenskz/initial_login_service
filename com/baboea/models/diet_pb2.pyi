from com.baboea.models import objectivegroup_pb2 as _objectivegroup_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea import concept_pb2 as _concept_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import property_pb2 as _property_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserDietDefinition(_message.Message):
    __slots__ = ("id", "owner", "objectiveGroups", "portionSizes", "concepts", "mealSizes", "mealBalancingProperties")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVEGROUPS_FIELD_NUMBER: _ClassVar[int]
    PORTIONSIZES_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    MEALSIZES_FIELD_NUMBER: _ClassVar[int]
    MEALBALANCINGPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner: _users_pb2.UserRef
    objectiveGroups: _containers.RepeatedCompositeFieldContainer[_objectivegroup_pb2.ObjectiveGroupRef]
    portionSizes: _concept_pb2.PortionConceptValues
    concepts: _concept_pb2.BoolConceptValues
    mealSizes: MealSizes
    mealBalancingProperties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyRef]
    def __init__(self, id: _Optional[str] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., objectiveGroups: _Optional[_Iterable[_Union[_objectivegroup_pb2.ObjectiveGroupRef, _Mapping]]] = ..., portionSizes: _Optional[_Union[_concept_pb2.PortionConceptValues, _Mapping]] = ..., concepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., mealSizes: _Optional[_Union[MealSizes, _Mapping]] = ..., mealBalancingProperties: _Optional[_Iterable[_Union[_property_pb2.PropertyRef, _Mapping]]] = ...) -> None: ...

class UserDietDefinitionRef(_message.Message):
    __slots__ = ("id", "owner")
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner: _users_pb2.UserRef
    def __init__(self, id: _Optional[str] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class ConceptOverride(_message.Message):
    __slots__ = ("concept", "foods")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ...) -> None: ...

class ClientMealSize(_message.Message):
    __slots__ = ("meal", "size")
    MEAL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    meal: _meal_pb2.MealRef
    size: float
    def __init__(self, meal: _Optional[_Union[_meal_pb2.MealRef, _Mapping]] = ..., size: _Optional[float] = ...) -> None: ...

class MealSizes(_message.Message):
    __slots__ = ("sizes",)
    SIZES_FIELD_NUMBER: _ClassVar[int]
    sizes: _containers.RepeatedCompositeFieldContainer[ClientMealSize]
    def __init__(self, sizes: _Optional[_Iterable[_Union[ClientMealSize, _Mapping]]] = ...) -> None: ...
