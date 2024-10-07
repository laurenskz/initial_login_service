from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import food_source_pb2 as _food_source_pb2
from com.baboea.models import food_units_pb2 as _food_units_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tag(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: _localized_pb2.LocalizedString
    value: float
    def __init__(self, name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class FoodRef(_message.Message):
    __slots__ = ("id", "name", "properties", "emoji")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    properties: _containers.RepeatedCompositeFieldContainer[Tag]
    emoji: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., properties: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., emoji: _Optional[str] = ...) -> None: ...

class FoodWeight(_message.Message):
    __slots__ = ("unit", "weightForOneUnit")
    UNIT_FIELD_NUMBER: _ClassVar[int]
    WEIGHTFORONEUNIT_FIELD_NUMBER: _ClassVar[int]
    unit: _food_units_pb2.FoodUnitRef
    weightForOneUnit: float
    def __init__(self, unit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ..., weightForOneUnit: _Optional[float] = ...) -> None: ...

class Food(_message.Message):
    __slots__ = ("id", "localizations", "properties", "weights", "source", "sourceId", "concept", "emoji", "relevance")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEID_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[FoodLocalized]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    weights: _containers.RepeatedCompositeFieldContainer[FoodWeight]
    source: _food_source_pb2.FoodSourceRef
    sourceId: str
    concept: _concepts_pb2.ConceptRef
    emoji: str
    relevance: float
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[FoodLocalized, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ..., weights: _Optional[_Iterable[_Union[FoodWeight, _Mapping]]] = ..., source: _Optional[_Union[_food_source_pb2.FoodSourceRef, _Mapping]] = ..., sourceId: _Optional[str] = ..., concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., emoji: _Optional[str] = ..., relevance: _Optional[float] = ...) -> None: ...

class FoodLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
