from com.baboea.models import matching_pb2 as _matching_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class Concept(_message.Message):
    __slots__ = ("id", "localizations", "matchSets", "parent", "children", "path")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    MATCHSETS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[ConceptLocalized]
    matchSets: _containers.RepeatedCompositeFieldContainer[_matching_pb2.MatchSet]
    parent: ConceptRef
    children: _containers.RepeatedCompositeFieldContainer[ConceptRef]
    path: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[ConceptLocalized, _Mapping]]] = ..., matchSets: _Optional[_Iterable[_Union[_matching_pb2.MatchSet, _Mapping]]] = ..., parent: _Optional[_Union[ConceptRef, _Mapping]] = ..., children: _Optional[_Iterable[_Union[ConceptRef, _Mapping]]] = ..., path: _Optional[_Iterable[int]] = ...) -> None: ...

class ConceptLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
