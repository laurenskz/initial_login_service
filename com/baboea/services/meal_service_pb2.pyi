from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MealList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_meal_pb2.MealRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_meal_pb2.MealRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class MealUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _meal_pb2.Meal
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_meal_pb2.Meal, _Mapping]] = ...) -> None: ...

class MealQuery(_message.Message):
    __slots__ = ("name", "page", "limit", "owner")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    owner: _users_pb2.UserRef
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...
