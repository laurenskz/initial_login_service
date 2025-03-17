from com.baboea import requirement_pb2 as _requirement_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import meal_components_pb2 as _meal_components_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea import concept_pb2 as _concept_pb2
from com.baboea.models import days_pb2 as _days_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectiveGroupRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SpecializedRequirementRef(_message.Message):
    __slots__ = ("id", "numerator")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    numerator: _property_pb2.PropertyRef
    def __init__(self, id: _Optional[str] = ..., numerator: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ...) -> None: ...

class SpecializedRequirement(_message.Message):
    __slots__ = ("id", "min", "max", "useMin", "useMax", "numerator", "denominator", "useRatio", "applicationLevel", "numeratorMeals", "denominatorMeals", "scaleNumerator", "scaleDenominator", "numeratorConcepts", "denominatorConcepts", "reward")
    ID_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    USEMIN_FIELD_NUMBER: _ClassVar[int]
    USEMAX_FIELD_NUMBER: _ClassVar[int]
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    USERATIO_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONLEVEL_FIELD_NUMBER: _ClassVar[int]
    NUMERATORMEALS_FIELD_NUMBER: _ClassVar[int]
    DENOMINATORMEALS_FIELD_NUMBER: _ClassVar[int]
    SCALENUMERATOR_FIELD_NUMBER: _ClassVar[int]
    SCALEDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    NUMERATORCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    DENOMINATORCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    min: float
    max: float
    useMin: bool
    useMax: bool
    numerator: _property_pb2.PropertyRef
    denominator: _property_pb2.PropertyRef
    useRatio: bool
    applicationLevel: ApplicationLevelRef
    numeratorMeals: MealSelection
    denominatorMeals: MealSelection
    scaleNumerator: float
    scaleDenominator: float
    numeratorConcepts: RequirementConcepts
    denominatorConcepts: RequirementConcepts
    reward: float
    def __init__(self, id: _Optional[str] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., useMin: bool = ..., useMax: bool = ..., numerator: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., denominator: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., useRatio: bool = ..., applicationLevel: _Optional[_Union[ApplicationLevelRef, _Mapping]] = ..., numeratorMeals: _Optional[_Union[MealSelection, _Mapping]] = ..., denominatorMeals: _Optional[_Union[MealSelection, _Mapping]] = ..., scaleNumerator: _Optional[float] = ..., scaleDenominator: _Optional[float] = ..., numeratorConcepts: _Optional[_Union[RequirementConcepts, _Mapping]] = ..., denominatorConcepts: _Optional[_Union[RequirementConcepts, _Mapping]] = ..., reward: _Optional[float] = ...) -> None: ...

class RequirementConcepts(_message.Message):
    __slots__ = ("concepts", "useAllConcepts")
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    USEALLCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _concept_pb2.BoolConceptValues
    useAllConcepts: bool
    def __init__(self, concepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., useAllConcepts: bool = ...) -> None: ...

class MealSelection(_message.Message):
    __slots__ = ("meals", "useAllMeals", "days", "useAllDays", "components", "useAllComponents")
    MEALS_FIELD_NUMBER: _ClassVar[int]
    USEALLMEALS_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    USEALLDAYS_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    USEALLCOMPONENTS_FIELD_NUMBER: _ClassVar[int]
    meals: _containers.RepeatedCompositeFieldContainer[_meal_pb2.MealRef]
    useAllMeals: bool
    days: _containers.RepeatedCompositeFieldContainer[_days_pb2.MealPlanDayRef]
    useAllDays: bool
    components: _containers.RepeatedCompositeFieldContainer[_meal_components_pb2.MealComponentRef]
    useAllComponents: bool
    def __init__(self, meals: _Optional[_Iterable[_Union[_meal_pb2.MealRef, _Mapping]]] = ..., useAllMeals: bool = ..., days: _Optional[_Iterable[_Union[_days_pb2.MealPlanDayRef, _Mapping]]] = ..., useAllDays: bool = ..., components: _Optional[_Iterable[_Union[_meal_components_pb2.MealComponentRef, _Mapping]]] = ..., useAllComponents: bool = ...) -> None: ...

class ApplicationLevelRef(_message.Message):
    __slots__ = ("id", "name", "handle", "emoji")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    handle: str
    emoji: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., handle: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class ApplicationLevel(_message.Message):
    __slots__ = ("id", "localizations", "handle", "emoji")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[ApplicationLevelLocalized]
    handle: str
    emoji: str
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[ApplicationLevelLocalized, _Mapping]]] = ..., handle: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class ApplicationLevelLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ObjectiveGroup(_message.Message):
    __slots__ = ("id", "name", "description", "objectives", "owner", "reward")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    objectives: _containers.RepeatedCompositeFieldContainer[SpecializedRequirement]
    owner: _users_pb2.UserRef
    reward: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., objectives: _Optional[_Iterable[_Union[SpecializedRequirement, _Mapping]]] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., reward: _Optional[float] = ...) -> None: ...
