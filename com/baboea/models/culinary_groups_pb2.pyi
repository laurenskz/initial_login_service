from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CulinaryGroup(_message.Message):
    __slots__ = ("id", "localizations", "concepts", "emoji", "importance")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[CulinaryGroupLocalized]
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    emoji: str
    importance: float
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[CulinaryGroupLocalized, _Mapping]]] = ..., concepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., emoji: _Optional[str] = ..., importance: _Optional[float] = ...) -> None: ...

class CulinaryGroupRef(_message.Message):
    __slots__ = ("id", "name", "emoji", "importance")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    emoji: str
    importance: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., emoji: _Optional[str] = ..., importance: _Optional[float] = ...) -> None: ...

class CulinaryGroupLocalized(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
