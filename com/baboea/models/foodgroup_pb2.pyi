from com.baboea.models import food_pb2 as _food_pb2
from com.baboea import concept_pb2 as _concept_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FoodGroupRef(_message.Message):
    __slots__ = ("id", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class FoodGroup(_message.Message):
    __slots__ = ("id", "name", "foods", "concepts", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    concepts: _concept_pb2.BoolConceptValues
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ..., concepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class FoodGroupQuery(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
