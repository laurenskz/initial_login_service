from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScrapeDomain(_message.Message):
    __slots__ = ("id", "name", "home", "locale", "allowedDomains")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDDOMAINS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    home: str
    locale: str
    allowedDomains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., home: _Optional[str] = ..., locale: _Optional[str] = ..., allowedDomains: _Optional[_Iterable[str]] = ...) -> None: ...

class UrlScrapeNode(_message.Message):
    __slots__ = ("id", "url", "visited")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VISITED_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    visited: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., visited: bool = ...) -> None: ...
