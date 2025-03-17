from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import food_units_pb2 as _food_units_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnitSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIZE: _ClassVar[UnitSource]
    PARSED_UNIT: _ClassVar[UnitSource]
    IMPLICIT: _ClassVar[UnitSource]

class QuantitySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPLICIT_QUANTITY: _ClassVar[QuantitySource]
    PARSED: _ClassVar[QuantitySource]
SIZE: UnitSource
PARSED_UNIT: UnitSource
IMPLICIT: UnitSource
IMPLICIT_QUANTITY: QuantitySource
PARSED: QuantitySource

class Recipe2mRecipe(_message.Message):
    __slots__ = ("id", "name", "ingredients")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    ingredients: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., ingredients: _Optional[_Iterable[str]] = ...) -> None: ...

class Recipe2mSet(_message.Message):
    __slots__ = ("recipes",)
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    recipes: _containers.RepeatedCompositeFieldContainer[Recipe2mRecipe]
    def __init__(self, recipes: _Optional[_Iterable[_Union[Recipe2mRecipe, _Mapping]]] = ...) -> None: ...

class RawUnit(_message.Message):
    __slots__ = ("name", "quantity", "confidence", "quantity_max")
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_MAX_FIELD_NUMBER: _ClassVar[int]
    name: str
    quantity: float
    confidence: float
    quantity_max: float
    def __init__(self, name: _Optional[str] = ..., quantity: _Optional[float] = ..., confidence: _Optional[float] = ..., quantity_max: _Optional[float] = ...) -> None: ...

class RawRecipeIngredient(_message.Message):
    __slots__ = ("name", "confidence", "units", "fulltext", "size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    FULLTEXT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    confidence: float
    units: _containers.RepeatedCompositeFieldContainer[RawUnit]
    fulltext: str
    size: str
    def __init__(self, name: _Optional[str] = ..., confidence: _Optional[float] = ..., units: _Optional[_Iterable[_Union[RawUnit, _Mapping]]] = ..., fulltext: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...

class RawRecipe(_message.Message):
    __slots__ = ("id", "name", "ingredients")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    ingredients: _containers.RepeatedCompositeFieldContainer[RawRecipeIngredient]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., ingredients: _Optional[_Iterable[_Union[RawRecipeIngredient, _Mapping]]] = ...) -> None: ...

class ParsedConcept(_message.Message):
    __slots__ = ("concept", "confidence")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    confidence: float
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., confidence: _Optional[float] = ...) -> None: ...

class ParsedWeight(_message.Message):
    __slots__ = ("confidence", "gramQuantity", "unitSource", "quantitySource", "parsedUnit", "parsedQuantity", "sourceText")
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    GRAMQUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNITSOURCE_FIELD_NUMBER: _ClassVar[int]
    QUANTITYSOURCE_FIELD_NUMBER: _ClassVar[int]
    PARSEDUNIT_FIELD_NUMBER: _ClassVar[int]
    PARSEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    SOURCETEXT_FIELD_NUMBER: _ClassVar[int]
    confidence: float
    gramQuantity: float
    unitSource: UnitSource
    quantitySource: QuantitySource
    parsedUnit: _food_units_pb2.FoodUnitRef
    parsedQuantity: float
    sourceText: str
    def __init__(self, confidence: _Optional[float] = ..., gramQuantity: _Optional[float] = ..., unitSource: _Optional[_Union[UnitSource, str]] = ..., quantitySource: _Optional[_Union[QuantitySource, str]] = ..., parsedUnit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ..., parsedQuantity: _Optional[float] = ..., sourceText: _Optional[str] = ...) -> None: ...

class ParsedIngredient(_message.Message):
    __slots__ = ("concept", "weight", "sourceText")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SOURCETEXT_FIELD_NUMBER: _ClassVar[int]
    concept: ParsedConcept
    weight: ParsedWeight
    sourceText: str
    def __init__(self, concept: _Optional[_Union[ParsedConcept, _Mapping]] = ..., weight: _Optional[_Union[ParsedWeight, _Mapping]] = ..., sourceText: _Optional[str] = ...) -> None: ...

class ParsedRecipe(_message.Message):
    __slots__ = ("name", "id", "ingredients")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    ingredients: _containers.RepeatedCompositeFieldContainer[ParsedIngredient]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., ingredients: _Optional[_Iterable[_Union[ParsedIngredient, _Mapping]]] = ...) -> None: ...
