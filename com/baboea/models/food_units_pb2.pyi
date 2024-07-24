from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import matching_pb2 as _matching_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FoodUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRAM: _ClassVar[FoodUnits]
    KILOGRAM: _ClassVar[FoodUnits]
    MILLILITER: _ClassVar[FoodUnits]
    DECILITER: _ClassVar[FoodUnits]
    LITER: _ClassVar[FoodUnits]
    TEASPOON: _ClassVar[FoodUnits]
    TABLESPOON: _ClassVar[FoodUnits]
    FLUID_OUNCE: _ClassVar[FoodUnits]
    CUP: _ClassVar[FoodUnits]
    PINT: _ClassVar[FoodUnits]
    QUART: _ClassVar[FoodUnits]
    GALLON: _ClassVar[FoodUnits]
    OUNCE: _ClassVar[FoodUnits]
    POUND: _ClassVar[FoodUnits]
    PIECE: _ClassVar[FoodUnits]
    CLOVES: _ClassVar[FoodUnits]
    SPRIG: _ClassVar[FoodUnits]
    SLICE: _ClassVar[FoodUnits]
    BUNCH: _ClassVar[FoodUnits]
    INCH: _ClassVar[FoodUnits]
    SMALL: _ClassVar[FoodUnits]
    MEDIUM: _ClassVar[FoodUnits]
    LARGE: _ClassVar[FoodUnits]
    PINCH: _ClassVar[FoodUnits]
    HEAPED_TABLESPOON: _ClassVar[FoodUnits]
    SERVING: _ClassVar[FoodUnits]
    UNKNOWN: _ClassVar[FoodUnits]
GRAM: FoodUnits
KILOGRAM: FoodUnits
MILLILITER: FoodUnits
DECILITER: FoodUnits
LITER: FoodUnits
TEASPOON: FoodUnits
TABLESPOON: FoodUnits
FLUID_OUNCE: FoodUnits
CUP: FoodUnits
PINT: FoodUnits
QUART: FoodUnits
GALLON: FoodUnits
OUNCE: FoodUnits
POUND: FoodUnits
PIECE: FoodUnits
CLOVES: FoodUnits
SPRIG: FoodUnits
SLICE: FoodUnits
BUNCH: FoodUnits
INCH: FoodUnits
SMALL: FoodUnits
MEDIUM: FoodUnits
LARGE: FoodUnits
PINCH: FoodUnits
HEAPED_TABLESPOON: FoodUnits
SERVING: FoodUnits
UNKNOWN: FoodUnits

class FoodUnit(_message.Message):
    __slots__ = ("id", "localizations", "handle", "matchSets")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    MATCHSETS_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[FoodUnitLocalized]
    handle: str
    matchSets: _containers.RepeatedCompositeFieldContainer[_matching_pb2.MatchSet]
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[FoodUnitLocalized, _Mapping]]] = ..., handle: _Optional[str] = ..., matchSets: _Optional[_Iterable[_Union[_matching_pb2.MatchSet, _Mapping]]] = ...) -> None: ...

class FoodUnitLocalized(_message.Message):
    __slots__ = ("locale", "name", "description", "abbreviation")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ABBREVIATION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    abbreviation: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., abbreviation: _Optional[str] = ...) -> None: ...

class FoodUnitRef(_message.Message):
    __slots__ = ("id", "name", "abbreviation")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABBREVIATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    abbreviation: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., abbreviation: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class ConversionRef(_message.Message):
    __slots__ = ("id", "unitFrom", "unitTo")
    ID_FIELD_NUMBER: _ClassVar[int]
    UNITFROM_FIELD_NUMBER: _ClassVar[int]
    UNITTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    unitFrom: FoodUnitRef
    unitTo: FoodUnitRef
    def __init__(self, id: _Optional[str] = ..., unitFrom: _Optional[_Union[FoodUnitRef, _Mapping]] = ..., unitTo: _Optional[_Union[FoodUnitRef, _Mapping]] = ...) -> None: ...

class Conversion(_message.Message):
    __slots__ = ("id", "unitFrom", "unitTo", "factor")
    ID_FIELD_NUMBER: _ClassVar[int]
    UNITFROM_FIELD_NUMBER: _ClassVar[int]
    UNITTO_FIELD_NUMBER: _ClassVar[int]
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    unitFrom: FoodUnitRef
    unitTo: FoodUnitRef
    factor: float
    def __init__(self, id: _Optional[str] = ..., unitFrom: _Optional[_Union[FoodUnitRef, _Mapping]] = ..., unitTo: _Optional[_Union[FoodUnitRef, _Mapping]] = ..., factor: _Optional[float] = ...) -> None: ...

class ConversionList(_message.Message):
    __slots__ = ("conversions",)
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    conversions: _containers.RepeatedCompositeFieldContainer[Conversion]
    def __init__(self, conversions: _Optional[_Iterable[_Union[Conversion, _Mapping]]] = ...) -> None: ...
