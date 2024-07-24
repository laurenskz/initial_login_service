from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea import foodgroup_pb2 as _foodgroup_pb2
from com.baboea import concept_pb2 as _concept_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea import selector_pb2 as _selector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DistributeFoods(_message.Message):
    __slots__ = ("food", "meals")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    MEALS_FIELD_NUMBER: _ClassVar[int]
    food: _containers.RepeatedScalarFieldContainer[str]
    meals: _containers.RepeatedCompositeFieldContainer[_foodgroup_pb2.FoodGroupIdentifier]
    def __init__(self, food: _Optional[_Iterable[str]] = ..., meals: _Optional[_Iterable[_Union[_foodgroup_pb2.FoodGroupIdentifier, _Mapping]]] = ...) -> None: ...

class MealSize(_message.Message):
    __slots__ = ("meal", "size")
    MEAL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    meal: _foodgroup_pb2.FoodGroupIdentifier
    size: float
    def __init__(self, meal: _Optional[_Union[_foodgroup_pb2.FoodGroupIdentifier, _Mapping]] = ..., size: _Optional[float] = ...) -> None: ...

class DistributeNutrient(_message.Message):
    __slots__ = ("property", "sizes", "margin")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    property: _property_pb2.PropertyRef
    sizes: _containers.RepeatedCompositeFieldContainer[MealSize]
    margin: float
    def __init__(self, property: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., sizes: _Optional[_Iterable[_Union[MealSize, _Mapping]]] = ..., margin: _Optional[float] = ...) -> None: ...

class AddMealComponent(_message.Message):
    __slots__ = ("meal", "sides", "recipe", "smart")
    MEAL_FIELD_NUMBER: _ClassVar[int]
    SIDES_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    SMART_FIELD_NUMBER: _ClassVar[int]
    meal: _foodgroup_pb2.FoodGroupIdentifier
    sides: SideDishes
    recipe: _recipes_pb2.ParsedRemoteRecipeRef
    smart: _meal_pb2.SmartRecipePreferences
    def __init__(self, meal: _Optional[_Union[_foodgroup_pb2.FoodGroupIdentifier, _Mapping]] = ..., sides: _Optional[_Union[SideDishes, _Mapping]] = ..., recipe: _Optional[_Union[_recipes_pb2.ParsedRemoteRecipeRef, _Mapping]] = ..., smart: _Optional[_Union[_meal_pb2.SmartRecipePreferences, _Mapping]] = ...) -> None: ...

class SideDishes(_message.Message):
    __slots__ = ("concepts",)
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[_concept_pb2.BoolConceptValues]
    def __init__(self, concepts: _Optional[_Iterable[_Union[_concept_pb2.BoolConceptValues, _Mapping]]] = ...) -> None: ...
