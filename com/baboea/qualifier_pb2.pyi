from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Query(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALL: _ClassVar[Query]
ALL: Query

class Ids(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Qualifier(_message.Message):
    __slots__ = ("query", "id", "selection")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SELECTION_FIELD_NUMBER: _ClassVar[int]
    query: Query
    id: str
    selection: Ids
    def __init__(self, query: _Optional[_Union[Query, str]] = ..., id: _Optional[str] = ..., selection: _Optional[_Union[Ids, _Mapping]] = ...) -> None: ...
