from com.baboea.models import food_source_pb2 as _food_source_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FoodSourceList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_food_source_pb2.FoodSourceRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_food_source_pb2.FoodSourceRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class FoodSourceUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _food_source_pb2.FoodSource
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_food_source_pb2.FoodSource, _Mapping]] = ...) -> None: ...

class FoodSourceQuery(_message.Message):
    __slots__ = ("name", "page", "limit", "locale")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    locale: _localized_pb2.LocaleRef
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...
