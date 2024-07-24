from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptCache(_message.Message):
    __slots__ = ("concept",)
    class ConceptEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _concepts_pb2.ConceptRef
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ...) -> None: ...
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    concept: _containers.MessageMap[str, _concepts_pb2.ConceptRef]
    def __init__(self, concept: _Optional[_Mapping[str, _concepts_pb2.ConceptRef]] = ...) -> None: ...

class Test(_message.Message):
    __slots__ = ("id", "name", "lastname", "age", "country", "hellos", "foods")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    HELLOS_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    lastname: str
    age: int
    country: str
    hellos: _containers.RepeatedScalarFieldContainer[str]
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., lastname: _Optional[str] = ..., age: _Optional[int] = ..., country: _Optional[str] = ..., hellos: _Optional[_Iterable[str]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ...) -> None: ...

class TestRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class TestQuery(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
