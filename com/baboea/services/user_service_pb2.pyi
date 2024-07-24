from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_users_pb2.UserRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_users_pb2.UserRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class UserUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _users_pb2.User
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_users_pb2.User, _Mapping]] = ...) -> None: ...

class UserQuery(_message.Message):
    __slots__ = ("name", "page", "limit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class FindByRemoteIdRequest(_message.Message):
    __slots__ = ("remoteId",)
    REMOTEID_FIELD_NUMBER: _ClassVar[int]
    remoteId: str
    def __init__(self, remoteId: _Optional[str] = ...) -> None: ...

class FindByRemoteIdResponse(_message.Message):
    __slots__ = ("user", "firstLogin")
    USER_FIELD_NUMBER: _ClassVar[int]
    FIRSTLOGIN_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    firstLogin: bool
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., firstLogin: bool = ...) -> None: ...
