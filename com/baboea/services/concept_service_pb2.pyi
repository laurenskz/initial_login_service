from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import concept_tag_pb2 as _concept_tag_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class ConceptUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _concepts_pb2.Concept
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_concepts_pb2.Concept, _Mapping]] = ...) -> None: ...

class ConceptQuery(_message.Message):
    __slots__ = ("name", "page", "limit", "locale", "tags", "tagHandles")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TAGHANDLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    locale: _localized_pb2.LocaleRef
    tags: _containers.RepeatedCompositeFieldContainer[_concept_tag_pb2.ConceptTagRef]
    tagHandles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[_concept_tag_pb2.ConceptTagRef, _Mapping]]] = ..., tagHandles: _Optional[_Iterable[str]] = ...) -> None: ...

class ShoppingListQuery(_message.Message):
    __slots__ = ("locale", "foods")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ...) -> None: ...

class ShoppingListResponse(_message.Message):
    __slots__ = ("mapping",)
    class MappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _concepts_pb2.ConceptRef
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ...) -> None: ...
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    mapping: _containers.MessageMap[str, _concepts_pb2.ConceptRef]
    def __init__(self, mapping: _Optional[_Mapping[str, _concepts_pb2.ConceptRef]] = ...) -> None: ...

class ConceptPath(_message.Message):
    __slots__ = ("id", "path")
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., path: _Optional[_Iterable[str]] = ...) -> None: ...

class ConceptPathResponse(_message.Message):
    __slots__ = ("paths",)
    PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedCompositeFieldContainer[ConceptPath]
    def __init__(self, paths: _Optional[_Iterable[_Union[ConceptPath, _Mapping]]] = ...) -> None: ...
