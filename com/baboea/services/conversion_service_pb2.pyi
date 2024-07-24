from com.baboea.models import food_units_pb2 as _food_units_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversionList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_food_units_pb2.ConversionRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_food_units_pb2.ConversionRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class ConversionUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _food_units_pb2.Conversion
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_food_units_pb2.Conversion, _Mapping]] = ...) -> None: ...

class ConversionQuery(_message.Message):
    __slots__ = ("units", "page", "limit")
    UNITS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedCompositeFieldContainer[_food_units_pb2.FoodUnitRef]
    page: str
    limit: int
    def __init__(self, units: _Optional[_Iterable[_Union[_food_units_pb2.FoodUnitRef, _Mapping]]] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...
