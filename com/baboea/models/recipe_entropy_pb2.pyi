from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimplifiedCaseConditionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALL: _ClassVar[SimplifiedCaseConditionType]
    ANY: _ClassVar[SimplifiedCaseConditionType]
    DISJUNCTIVE_ANTECEDENTS: _ClassVar[SimplifiedCaseConditionType]
    DISJUNCTIVE_CONSEQUENTS: _ClassVar[SimplifiedCaseConditionType]
ALL: SimplifiedCaseConditionType
ANY: SimplifiedCaseConditionType
DISJUNCTIVE_ANTECEDENTS: SimplifiedCaseConditionType
DISJUNCTIVE_CONSEQUENTS: SimplifiedCaseConditionType

class EntropicValueRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class EntropicValue(_message.Message):
    __slots__ = ("id", "localizations")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[EntropicValueLocalized]
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[EntropicValueLocalized, _Mapping]]] = ...) -> None: ...

class EntropicValueLocalized(_message.Message):
    __slots__ = ("locale", "name", "userInputName")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERINPUTNAME_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    userInputName: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., userInputName: _Optional[str] = ...) -> None: ...

class EntropicFeatureOrDimensionRef(_message.Message):
    __slots__ = ("id", "name", "emoji")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    emoji: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., emoji: _Optional[str] = ...) -> None: ...

class SimplifiedBaseCondition(_message.Message):
    __slots__ = ("concept", "includeChildren", "negate")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    INCLUDECHILDREN_FIELD_NUMBER: _ClassVar[int]
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    includeChildren: bool
    negate: bool
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., includeChildren: bool = ..., negate: bool = ...) -> None: ...

class SimplifiedCase(_message.Message):
    __slots__ = ("all", "any", "value", "disjunctiveAntecedent", "disjunctiveConsequent")
    ALL_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DISJUNCTIVEANTECEDENT_FIELD_NUMBER: _ClassVar[int]
    DISJUNCTIVECONSEQUENT_FIELD_NUMBER: _ClassVar[int]
    all: _containers.RepeatedCompositeFieldContainer[SimplifiedBaseCondition]
    any: _containers.RepeatedCompositeFieldContainer[SimplifiedBaseCondition]
    value: EntropicValueRef
    disjunctiveAntecedent: _containers.RepeatedCompositeFieldContainer[SimplifiedBaseCondition]
    disjunctiveConsequent: _containers.RepeatedCompositeFieldContainer[SimplifiedBaseCondition]
    def __init__(self, all: _Optional[_Iterable[_Union[SimplifiedBaseCondition, _Mapping]]] = ..., any: _Optional[_Iterable[_Union[SimplifiedBaseCondition, _Mapping]]] = ..., value: _Optional[_Union[EntropicValueRef, _Mapping]] = ..., disjunctiveAntecedent: _Optional[_Iterable[_Union[SimplifiedBaseCondition, _Mapping]]] = ..., disjunctiveConsequent: _Optional[_Iterable[_Union[SimplifiedBaseCondition, _Mapping]]] = ...) -> None: ...

class SimplifiedFunction(_message.Message):
    __slots__ = ("cases",)
    CASES_FIELD_NUMBER: _ClassVar[int]
    cases: _containers.RepeatedCompositeFieldContainer[SimplifiedCase]
    def __init__(self, cases: _Optional[_Iterable[_Union[SimplifiedCase, _Mapping]]] = ...) -> None: ...

class EntropicFeatureOrDimension(_message.Message):
    __slots__ = ("id", "isFeature", "isDimension", "localizations", "defaultValue", "domain", "classificationCases", "emoji", "weight")
    ID_FIELD_NUMBER: _ClassVar[int]
    ISFEATURE_FIELD_NUMBER: _ClassVar[int]
    ISDIMENSION_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATIONCASES_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    id: str
    isFeature: bool
    isDimension: bool
    localizations: _containers.RepeatedCompositeFieldContainer[EntropicFeatureOrDimensionLocalized]
    defaultValue: EntropicValueRef
    domain: _containers.RepeatedCompositeFieldContainer[EntropicValueRef]
    classificationCases: _containers.RepeatedCompositeFieldContainer[SimplifiedCase]
    emoji: str
    weight: float
    def __init__(self, id: _Optional[str] = ..., isFeature: bool = ..., isDimension: bool = ..., localizations: _Optional[_Iterable[_Union[EntropicFeatureOrDimensionLocalized, _Mapping]]] = ..., defaultValue: _Optional[_Union[EntropicValueRef, _Mapping]] = ..., domain: _Optional[_Iterable[_Union[EntropicValueRef, _Mapping]]] = ..., classificationCases: _Optional[_Iterable[_Union[SimplifiedCase, _Mapping]]] = ..., emoji: _Optional[str] = ..., weight: _Optional[float] = ...) -> None: ...

class EntropicFeatureOrDimensionLocalized(_message.Message):
    __slots__ = ("locale", "name")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
