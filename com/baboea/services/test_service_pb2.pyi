from com.baboea.models import test_pb2 as _test_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_test_pb2.TestRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_test_pb2.TestRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class TestUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _test_pb2.Test
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_test_pb2.Test, _Mapping]] = ...) -> None: ...
