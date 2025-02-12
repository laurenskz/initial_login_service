from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import culinary_groups_pb2 as _culinary_groups_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptAffinity(_message.Message):
    __slots__ = ("id", "to", "affinity", "groupOfTo", "category")
    ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_FIELD_NUMBER: _ClassVar[int]
    GROUPOFTO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    to: _concepts_pb2.ConceptRef
    affinity: float
    groupOfTo: _culinary_groups_pb2.CulinaryGroupRef
    category: _recipes_pb2.RecipeCategoryRef
    def __init__(self, id: _Optional[str] = ..., to: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., affinity: _Optional[float] = ..., groupOfTo: _Optional[_Union[_culinary_groups_pb2.CulinaryGroupRef, _Mapping]] = ..., category: _Optional[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]] = ..., **kwargs) -> None: ...

class ConceptAffinityRef(_message.Message):
    __slots__ = ("id", "to")
    ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    id: str
    to: _concepts_pb2.ConceptRef
    def __init__(self, id: _Optional[str] = ..., to: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., **kwargs) -> None: ...
