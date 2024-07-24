from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea import concept_pb2 as _concept_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MealPlanDay(_message.Message):
    __slots__ = ("id", "meals", "owner", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    MEALS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    meals: _containers.RepeatedCompositeFieldContainer[_meal_pb2.MealRef]
    owner: _users_pb2.UserRef
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., meals: _Optional[_Iterable[_Union[_meal_pb2.MealRef, _Mapping]]] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class MealPlanDayRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
