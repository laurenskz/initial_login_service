from com.baboea.models import concept_impl_pb2 as _concept_impl_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptImplementationList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_concept_impl_pb2.ConceptImplementationRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_concept_impl_pb2.ConceptImplementationRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class ConceptImplementationUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _concept_impl_pb2.ConceptImplementation
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_concept_impl_pb2.ConceptImplementation, _Mapping]] = ...) -> None: ...

class ConceptImplementationQuery(_message.Message):
    __slots__ = ("name", "page", "limit", "locale")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    locale: _localized_pb2.LocaleRef
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...

class GetPropertiesForDefaultImplRequest(_message.Message):
    __slots__ = ("concept",)
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ...) -> None: ...

class FoodWithProperties(_message.Message):
    __slots__ = ("foodId", "properties")
    FOODID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    foodId: str
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, foodId: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class GetPropertiesForDefaultImplResponse(_message.Message):
    __slots__ = ("foods",)
    FOODS_FIELD_NUMBER: _ClassVar[int]
    foods: _containers.RepeatedCompositeFieldContainer[FoodWithProperties]
    def __init__(self, foods: _Optional[_Iterable[_Union[FoodWithProperties, _Mapping]]] = ...) -> None: ...
