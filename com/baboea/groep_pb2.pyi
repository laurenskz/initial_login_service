from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Baboea(_message.Message):
    __slots__ = ("name", "age")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class SuperBab(_message.Message):
    __slots__ = ("bab", "fire", "babstatus")
    BAB_FIELD_NUMBER: _ClassVar[int]
    FIRE_FIELD_NUMBER: _ClassVar[int]
    BABSTATUS_FIELD_NUMBER: _ClassVar[int]
    bab: Baboea
    fire: int
    babstatus: str
    def __init__(self, bab: _Optional[_Union[Baboea, _Mapping]] = ..., fire: _Optional[int] = ..., babstatus: _Optional[str] = ...) -> None: ...
