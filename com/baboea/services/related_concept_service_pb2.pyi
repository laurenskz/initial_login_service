from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import culinary_groups_pb2 as _culinary_groups_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import weights_pb2 as _weights_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RelatedConceptQuery(_message.Message):
    __slots__ = ("base", "forbidden", "categories", "minSupport")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FORBIDDEN_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    MINSUPPORT_FIELD_NUMBER: _ClassVar[int]
    base: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    forbidden: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    categories: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategoryRef]
    minSupport: float
    def __init__(self, base: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., forbidden: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., categories: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., minSupport: _Optional[float] = ...) -> None: ...

class RelatedConceptResponse(_message.Message):
    __slots__ = ("relatedConcepts",)
    RELATEDCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    relatedConcepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    def __init__(self, relatedConcepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ...) -> None: ...
