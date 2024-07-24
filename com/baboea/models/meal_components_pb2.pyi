from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MealComponent(_message.Message):
    __slots__ = ("id", "localizations", "handle")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[MealComponentLocalized]
    handle: str
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[MealComponentLocalized, _Mapping]]] = ..., handle: _Optional[str] = ...) -> None: ...

class MealComponentLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class MealComponentRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...
