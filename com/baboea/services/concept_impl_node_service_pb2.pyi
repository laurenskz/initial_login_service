from com.baboea.models import concept_impl_pb2 as _concept_impl_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptImplementationNodeList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_concept_impl_pb2.ConceptImplementationNodeRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_concept_impl_pb2.ConceptImplementationNodeRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class ConceptImplementationNodeUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _concept_impl_pb2.ConceptImplementationNode
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_concept_impl_pb2.ConceptImplementationNode, _Mapping]] = ...) -> None: ...

class ConceptImplementationNodeQuery(_message.Message):
    __slots__ = ("implementation", "page", "limit", "locale", "conceptName", "owner")
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CONCEPTNAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    implementation: _concept_impl_pb2.ConceptImplementationRef
    page: str
    limit: int
    locale: _localized_pb2.LocaleRef
    conceptName: str
    owner: _users_pb2.UserRef
    def __init__(self, implementation: _Optional[_Union[_concept_impl_pb2.ConceptImplementationRef, _Mapping]] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., conceptName: _Optional[str] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class CreateOrUpdateRequest(_message.Message):
    __slots__ = ("user", "concept", "food")
    USER_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    FOOD_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    concept: _concepts_pb2.ConceptRef
    food: _food_pb2.FoodRef
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ...) -> None: ...
