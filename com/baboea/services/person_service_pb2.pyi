from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Person(_message.Message):
    __slots__ = ("id", "name", "age", "todos")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    TODOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    age: int
    todos: _containers.RepeatedCompositeFieldContainer[TodoItem]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., age: _Optional[int] = ..., todos: _Optional[_Iterable[_Union[TodoItem, _Mapping]]] = ...) -> None: ...

class TodoItem(_message.Message):
    __slots__ = ("name", "priority")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    priority: int
    def __init__(self, name: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class PersonRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class PersonList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PersonRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[PersonRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class PersonUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: Person
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[Person, _Mapping]] = ...) -> None: ...

class PersonQuery(_message.Message):
    __slots__ = ("name", "page", "limit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...
