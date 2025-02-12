from com.baboea.services import base_pb2 as _base_pb2
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

class FlavourSuggestionQuery(_message.Message):
    __slots__ = ("base", "locale", "category", "user")
    BASE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    base: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    locale: _localized_pb2.LocaleRef
    category: _recipes_pb2.RecipeCategoryRef
    user: _users_pb2.UserRef
    def __init__(self, base: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., category: _Optional[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class RecipeSuggestionQuery(_message.Message):
    __slots__ = ("base", "canNotInclude", "locale", "categories", "cuisines", "minSupport")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CANNOTINCLUDE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    MINSUPPORT_FIELD_NUMBER: _ClassVar[int]
    base: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    canNotInclude: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    locale: _localized_pb2.LocaleRef
    categories: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategoryRef]
    cuisines: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategoryRef]
    minSupport: float
    def __init__(self, base: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., canNotInclude: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., categories: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., minSupport: _Optional[float] = ...) -> None: ...

class SuggestedFlavourGroup(_message.Message):
    __slots__ = ("culinaryGroup", "concepts")
    CULINARYGROUP_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    culinaryGroup: _culinary_groups_pb2.CulinaryGroupRef
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.QuantifiedConcept]
    def __init__(self, culinaryGroup: _Optional[_Union[_culinary_groups_pb2.CulinaryGroupRef, _Mapping]] = ..., concepts: _Optional[_Iterable[_Union[_concepts_pb2.QuantifiedConcept, _Mapping]]] = ...) -> None: ...

class FlavourGroupRelation(_message.Message):
    __slots__ = ("sourceGroup", "targetGroup", "minCount", "maxCount")
    SOURCEGROUP_FIELD_NUMBER: _ClassVar[int]
    TARGETGROUP_FIELD_NUMBER: _ClassVar[int]
    MINCOUNT_FIELD_NUMBER: _ClassVar[int]
    MAXCOUNT_FIELD_NUMBER: _ClassVar[int]
    sourceGroup: _culinary_groups_pb2.CulinaryGroupRef
    targetGroup: _culinary_groups_pb2.CulinaryGroupRef
    minCount: int
    maxCount: int
    def __init__(self, sourceGroup: _Optional[_Union[_culinary_groups_pb2.CulinaryGroupRef, _Mapping]] = ..., targetGroup: _Optional[_Union[_culinary_groups_pb2.CulinaryGroupRef, _Mapping]] = ..., minCount: _Optional[int] = ..., maxCount: _Optional[int] = ...) -> None: ...

class FlavourSuggestionResponse(_message.Message):
    __slots__ = ("groups", "constraints", "relations", "uncategorized")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    UNCATEGORIZED_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[SuggestedFlavourGroup]
    constraints: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.WeightConstraint]
    relations: _containers.RepeatedCompositeFieldContainer[FlavourGroupRelation]
    uncategorized: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.QuantifiedConcept]
    def __init__(self, groups: _Optional[_Iterable[_Union[SuggestedFlavourGroup, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[_concepts_pb2.WeightConstraint, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[FlavourGroupRelation, _Mapping]]] = ..., uncategorized: _Optional[_Iterable[_Union[_concepts_pb2.QuantifiedConcept, _Mapping]]] = ...) -> None: ...
