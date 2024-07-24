from com.baboea.models import objectivegroup_pb2 as _objectivegroup_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea import concept_pb2 as _concept_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppInitialization(_message.Message):
    __slots__ = ("meals", "objectives")
    MEALS_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    meals: _meal_pb2.Meal
    objectives: _containers.RepeatedCompositeFieldContainer[_objectivegroup_pb2.ObjectiveGroup]
    def __init__(self, meals: _Optional[_Union[_meal_pb2.Meal, _Mapping]] = ..., objectives: _Optional[_Iterable[_Union[_objectivegroup_pb2.ObjectiveGroup, _Mapping]]] = ...) -> None: ...
