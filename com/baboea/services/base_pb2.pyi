from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindSingleHandleRequest(_message.Message):
    __slots__ = ("handle",)
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    handle: str
    def __init__(self, handle: _Optional[str] = ...) -> None: ...

class OperationResponse(_message.Message):
    __slots__ = ("success", "error_message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("operation",)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: OperationResponse
    def __init__(self, operation: _Optional[_Union[OperationResponse, _Mapping]] = ...) -> None: ...

class RemoveRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RemoveResponse(_message.Message):
    __slots__ = ("operation",)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: OperationResponse
    def __init__(self, operation: _Optional[_Union[OperationResponse, _Mapping]] = ...) -> None: ...

class GetAllRequest(_message.Message):
    __slots__ = ("page", "limit")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    page: str
    limit: int
    def __init__(self, page: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ("id", "operation")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    operation: OperationResponse
    def __init__(self, id: _Optional[str] = ..., operation: _Optional[_Union[OperationResponse, _Mapping]] = ...) -> None: ...
