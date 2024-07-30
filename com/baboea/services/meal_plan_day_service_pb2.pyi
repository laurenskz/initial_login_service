from com.baboea.models import days_pb2 as _days_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MealPlanDayList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_days_pb2.MealPlanDayRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_days_pb2.MealPlanDayRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class MealPlanDayUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _days_pb2.MealPlanDay
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_days_pb2.MealPlanDay, _Mapping]] = ...) -> None: ...

class MealPlanDayQuery(_message.Message):
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