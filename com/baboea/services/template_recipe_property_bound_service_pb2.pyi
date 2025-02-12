from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptOptions(_message.Message):
    __slots__ = ("concept", "foods")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ...) -> None: ...

class FoodProperties(_message.Message):
    __slots__ = ("food", "properties")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class ComputeTemplateRecipeBoundRequest(_message.Message):
    __slots__ = ("recipe", "desiredProperties")
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    DESIREDPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    recipe: _template_recipe_data_pb2.ImprovedTemplateRecipe
    desiredProperties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyRef]
    def __init__(self, recipe: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipe, _Mapping]] = ..., desiredProperties: _Optional[_Iterable[_Union[_property_pb2.PropertyRef, _Mapping]]] = ...) -> None: ...

class PropertyBound(_message.Message):
    __slots__ = ("property", "minPer100Kcal", "maxPer100Kcal")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    MINPER100KCAL_FIELD_NUMBER: _ClassVar[int]
    MAXPER100KCAL_FIELD_NUMBER: _ClassVar[int]
    property: _property_pb2.PropertyRef
    minPer100Kcal: float
    maxPer100Kcal: float
    def __init__(self, property: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., minPer100Kcal: _Optional[float] = ..., maxPer100Kcal: _Optional[float] = ...) -> None: ...

class ComputeTemplateRecipeBoundResponse(_message.Message):
    __slots__ = ("bounds", "minKcal", "maxKcal")
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    MINKCAL_FIELD_NUMBER: _ClassVar[int]
    MAXKCAL_FIELD_NUMBER: _ClassVar[int]
    bounds: _containers.RepeatedCompositeFieldContainer[PropertyBound]
    minKcal: float
    maxKcal: float
    def __init__(self, bounds: _Optional[_Iterable[_Union[PropertyBound, _Mapping]]] = ..., minKcal: _Optional[float] = ..., maxKcal: _Optional[float] = ...) -> None: ...
