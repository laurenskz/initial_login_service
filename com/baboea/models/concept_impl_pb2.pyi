from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptImplementation(_message.Message):
    __slots__ = ("id", "localizations", "handle")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[ConceptImplementationLocalized]
    handle: str
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[ConceptImplementationLocalized, _Mapping]]] = ..., handle: _Optional[str] = ...) -> None: ...

class ConceptImplementationLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ConceptImplementationRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class ConceptImplementationNodeRef(_message.Message):
    __slots__ = ("id", "concept", "implementation")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    concept: _concepts_pb2.ConceptRef
    implementation: ConceptImplementationRef
    def __init__(self, id: _Optional[str] = ..., concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., implementation: _Optional[_Union[ConceptImplementationRef, _Mapping]] = ...) -> None: ...

class ConceptImplementationNode(_message.Message):
    __slots__ = ("id", "concept", "foods", "implementation", "owner")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    id: str
    concept: _concepts_pb2.ConceptRef
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    implementation: ConceptImplementationRef
    owner: _users_pb2.UserRef
    def __init__(self, id: _Optional[str] = ..., concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ..., implementation: _Optional[_Union[ConceptImplementationRef, _Mapping]] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class ConceptImplementationData(_message.Message):
    __slots__ = ("nodes", "implementation")
    NODES_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ConceptImplementationNodeFull]
    implementation: ConceptImplementationRef
    def __init__(self, nodes: _Optional[_Iterable[_Union[ConceptImplementationNodeFull, _Mapping]]] = ..., implementation: _Optional[_Union[ConceptImplementationRef, _Mapping]] = ...) -> None: ...

class ConceptImplementationNodeFull(_message.Message):
    __slots__ = ("concept", "foods")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.Food]
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.Food, _Mapping]]] = ...) -> None: ...
