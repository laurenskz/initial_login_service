from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocaleList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_localized_pb2.LocaleRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_localized_pb2.LocaleRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class LocaleUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _localized_pb2.Locale
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_localized_pb2.Locale, _Mapping]] = ...) -> None: ...

class LocaleQuery(_message.Message):
    __slots__ = ("name", "page", "limit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...
