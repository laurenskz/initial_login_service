from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name", "bab")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BAB_FIELD_NUMBER: _ClassVar[int]
    name: str
    bab: int
    def __init__(self, name: _Optional[str] = ..., bab: _Optional[int] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("message", "version")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    message: str
    version: int
    def __init__(self, message: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
