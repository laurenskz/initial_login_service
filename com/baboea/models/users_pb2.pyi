from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "externalId", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    externalId: str
    name: str
    def __init__(self, id: _Optional[str] = ..., externalId: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UserRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
