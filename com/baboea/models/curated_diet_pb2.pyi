from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea import concept_pb2 as _concept_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CuratedDiet(_message.Message):
    __slots__ = ("id", "concepts", "localizations")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    concepts: _concept_pb2.BoolConceptValues
    localizations: _containers.RepeatedCompositeFieldContainer[CuratedDietLocalized]
    def __init__(self, id: _Optional[str] = ..., concepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., localizations: _Optional[_Iterable[_Union[CuratedDietLocalized, _Mapping]]] = ...) -> None: ...

class CuratedDietRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class CuratedDietLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
