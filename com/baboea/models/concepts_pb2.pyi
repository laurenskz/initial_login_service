from com.baboea.models import matching_pb2 as _matching_pb2
from com.baboea.models import weights_pb2 as _weights_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import concept_tag_pb2 as _concept_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConceptRef(_message.Message):
    __slots__ = ("id", "name", "emoji")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    emoji: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., emoji: _Optional[str] = ...) -> None: ...

class Concept(_message.Message):
    __slots__ = ("id", "localizations", "matchSets", "parent", "children", "path", "emoji", "tags", "handle", "hasDiscretePortions", "minPortion", "maxPortion")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    MATCHSETS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    HASDISCRETEPORTIONS_FIELD_NUMBER: _ClassVar[int]
    MINPORTION_FIELD_NUMBER: _ClassVar[int]
    MAXPORTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[ConceptLocalized]
    matchSets: _containers.RepeatedCompositeFieldContainer[_matching_pb2.MatchSet]
    parent: ConceptRef
    children: _containers.RepeatedCompositeFieldContainer[ConceptRef]
    path: _containers.RepeatedScalarFieldContainer[int]
    emoji: str
    tags: _containers.RepeatedCompositeFieldContainer[_concept_tag_pb2.ConceptTagRef]
    handle: str
    hasDiscretePortions: bool
    minPortion: float
    maxPortion: float
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[ConceptLocalized, _Mapping]]] = ..., matchSets: _Optional[_Iterable[_Union[_matching_pb2.MatchSet, _Mapping]]] = ..., parent: _Optional[_Union[ConceptRef, _Mapping]] = ..., children: _Optional[_Iterable[_Union[ConceptRef, _Mapping]]] = ..., path: _Optional[_Iterable[int]] = ..., emoji: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[_concept_tag_pb2.ConceptTagRef, _Mapping]]] = ..., handle: _Optional[str] = ..., hasDiscretePortions: bool = ..., minPortion: _Optional[float] = ..., maxPortion: _Optional[float] = ...) -> None: ...

class ConceptLocalized(_message.Message):
    __slots__ = ("locale", "name", "description", "alsoKnownAs")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALSOKNOWNAS_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    alsoKnownAs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., alsoKnownAs: _Optional[_Iterable[str]] = ...) -> None: ...

class WeightConstraint(_message.Message):
    __slots__ = ("conceptOne", "conceptTwo", "isCrucial", "minRatioFromOneToTwo", "maxRatioFromOneToTwo", "conceptTwoScale")
    CONCEPTONE_FIELD_NUMBER: _ClassVar[int]
    CONCEPTTWO_FIELD_NUMBER: _ClassVar[int]
    ISCRUCIAL_FIELD_NUMBER: _ClassVar[int]
    MINRATIOFROMONETOTWO_FIELD_NUMBER: _ClassVar[int]
    MAXRATIOFROMONETOTWO_FIELD_NUMBER: _ClassVar[int]
    CONCEPTTWOSCALE_FIELD_NUMBER: _ClassVar[int]
    conceptOne: ConceptRef
    conceptTwo: ConceptRef
    isCrucial: bool
    minRatioFromOneToTwo: float
    maxRatioFromOneToTwo: float
    conceptTwoScale: float
    def __init__(self, conceptOne: _Optional[_Union[ConceptRef, _Mapping]] = ..., conceptTwo: _Optional[_Union[ConceptRef, _Mapping]] = ..., isCrucial: bool = ..., minRatioFromOneToTwo: _Optional[float] = ..., maxRatioFromOneToTwo: _Optional[float] = ..., conceptTwoScale: _Optional[float] = ...) -> None: ...

class FixedWeights(_message.Message):
    __slots__ = ("weights",)
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    weights: _containers.RepeatedCompositeFieldContainer[_weights_pb2.ModifiableFreeFormWeight]
    def __init__(self, weights: _Optional[_Iterable[_Union[_weights_pb2.ModifiableFreeFormWeight, _Mapping]]] = ...) -> None: ...

class QuantifiedConcept(_message.Message):
    __slots__ = ("concept", "isDiscrete", "range", "freeForm")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    ISDISCRETE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    FREEFORM_FIELD_NUMBER: _ClassVar[int]
    concept: ConceptRef
    isDiscrete: bool
    range: _weights_pb2.RangeWeight
    freeForm: FixedWeights
    def __init__(self, concept: _Optional[_Union[ConceptRef, _Mapping]] = ..., isDiscrete: bool = ..., range: _Optional[_Union[_weights_pb2.RangeWeight, _Mapping]] = ..., freeForm: _Optional[_Union[FixedWeights, _Mapping]] = ...) -> None: ...
