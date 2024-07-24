from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalizedString(_message.Message):
    __slots__ = ("languages",)
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    languages: _containers.RepeatedCompositeFieldContainer[LocalizedStringValue]
    def __init__(self, languages: _Optional[_Iterable[_Union[LocalizedStringValue, _Mapping]]] = ...) -> None: ...

class LocaleRef(_message.Message):
    __slots__ = ("id", "iso6391", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    ISO6391_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    iso6391: str
    name: str
    def __init__(self, id: _Optional[str] = ..., iso6391: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Locale(_message.Message):
    __slots__ = ("id", "iso6391", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    ISO6391_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    iso6391: str
    name: str
    def __init__(self, id: _Optional[str] = ..., iso6391: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class LocalizedStringValue(_message.Message):
    __slots__ = ("locale", "value")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    locale: LocaleRef
    value: str
    def __init__(self, locale: _Optional[_Union[LocaleRef, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...
