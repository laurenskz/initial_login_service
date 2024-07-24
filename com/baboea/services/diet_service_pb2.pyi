from com.baboea.models import diet_pb2 as _diet_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserDietDefinitionList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_diet_pb2.UserDietDefinitionRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_diet_pb2.UserDietDefinitionRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class UserDietDefinitionUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _diet_pb2.UserDietDefinition
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_diet_pb2.UserDietDefinition, _Mapping]] = ...) -> None: ...

class UserDietDefinitionQuery(_message.Message):
    __slots__ = ("owner", "page", "limit")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    owner: _containers.RepeatedCompositeFieldContainer[_users_pb2.UserRef]
    page: str
    limit: int
    def __init__(self, owner: _Optional[_Iterable[_Union[_users_pb2.UserRef, _Mapping]]] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...
