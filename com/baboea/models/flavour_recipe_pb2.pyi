from com.baboea.models import culinary_groups_pb2 as _culinary_groups_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlavourRecipeVariable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COUNT: _ClassVar[FlavourRecipeVariable]
    REPETITIONS: _ClassVar[FlavourRecipeVariable]
    WEIGHT: _ClassVar[FlavourRecipeVariable]
COUNT: FlavourRecipeVariable
REPETITIONS: FlavourRecipeVariable
WEIGHT: FlavourRecipeVariable

class FlavourGroup(_message.Message):
    __slots__ = ("culinaryGroup", "concepts", "groupId")
    CULINARYGROUP_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    culinaryGroup: _culinary_groups_pb2.CulinaryGroupRef
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.QuantifiedConcept]
    groupId: str
    def __init__(self, culinaryGroup: _Optional[_Union[_culinary_groups_pb2.CulinaryGroupRef, _Mapping]] = ..., concepts: _Optional[_Iterable[_Union[_concepts_pb2.QuantifiedConcept, _Mapping]]] = ..., groupId: _Optional[str] = ...) -> None: ...

class ConstraintTarget(_message.Message):
    __slots__ = ("concept", "groupId", "variable")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    groupId: str
    variable: FlavourRecipeVariable
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., groupId: _Optional[str] = ..., variable: _Optional[_Union[FlavourRecipeVariable, str]] = ...) -> None: ...

class ConstraintData(_message.Message):
    __slots__ = ("between", "exactly")
    BETWEEN_FIELD_NUMBER: _ClassVar[int]
    EXACTLY_FIELD_NUMBER: _ClassVar[int]
    between: BetweenConstraint
    exactly: float
    def __init__(self, between: _Optional[_Union[BetweenConstraint, _Mapping]] = ..., exactly: _Optional[float] = ...) -> None: ...

class BetweenConstraint(_message.Message):
    __slots__ = ("minRatio", "maxRatio")
    MINRATIO_FIELD_NUMBER: _ClassVar[int]
    MAXRATIO_FIELD_NUMBER: _ClassVar[int]
    minRatio: float
    maxRatio: float
    def __init__(self, minRatio: _Optional[float] = ..., maxRatio: _Optional[float] = ...) -> None: ...

class GlobalConstraint(_message.Message):
    __slots__ = ("source", "data")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    source: ConstraintTarget
    data: ConstraintData
    def __init__(self, source: _Optional[_Union[ConstraintTarget, _Mapping]] = ..., data: _Optional[_Union[ConstraintData, _Mapping]] = ...) -> None: ...

class PerServingConstraint(_message.Message):
    __slots__ = ("source", "data")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    source: ConstraintTarget
    data: ConstraintData
    def __init__(self, source: _Optional[_Union[ConstraintTarget, _Mapping]] = ..., data: _Optional[_Union[ConstraintData, _Mapping]] = ...) -> None: ...

class RatioConstraint(_message.Message):
    __slots__ = ("source", "target", "data", "target_scale")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TARGET_SCALE_FIELD_NUMBER: _ClassVar[int]
    source: ConstraintTarget
    target: ConstraintTarget
    data: ConstraintData
    target_scale: float
    def __init__(self, source: _Optional[_Union[ConstraintTarget, _Mapping]] = ..., target: _Optional[_Union[ConstraintTarget, _Mapping]] = ..., data: _Optional[_Union[ConstraintData, _Mapping]] = ..., target_scale: _Optional[float] = ...) -> None: ...

class FlavourRecipe(_message.Message):
    __slots__ = ("base", "groups", "globalConstraints", "perServingConstraints", "ratioConstraints")
    BASE_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    GLOBALCONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    PERSERVINGCONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    RATIOCONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    base: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.QuantifiedConcept]
    groups: _containers.RepeatedCompositeFieldContainer[FlavourGroup]
    globalConstraints: _containers.RepeatedCompositeFieldContainer[GlobalConstraint]
    perServingConstraints: _containers.RepeatedCompositeFieldContainer[PerServingConstraint]
    ratioConstraints: _containers.RepeatedCompositeFieldContainer[RatioConstraint]
    def __init__(self, base: _Optional[_Iterable[_Union[_concepts_pb2.QuantifiedConcept, _Mapping]]] = ..., groups: _Optional[_Iterable[_Union[FlavourGroup, _Mapping]]] = ..., globalConstraints: _Optional[_Iterable[_Union[GlobalConstraint, _Mapping]]] = ..., perServingConstraints: _Optional[_Iterable[_Union[PerServingConstraint, _Mapping]]] = ..., ratioConstraints: _Optional[_Iterable[_Union[RatioConstraint, _Mapping]]] = ...) -> None: ...
