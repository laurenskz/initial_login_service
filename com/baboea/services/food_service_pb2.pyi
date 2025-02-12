from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import food_source_pb2 as _food_source_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import weights_pb2 as _weights_pb2
from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASC: _ClassVar[Sort]
    DESC: _ClassVar[Sort]
ASC: Sort
DESC: Sort

class FoodList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class FoodUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _food_pb2.Food
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_food_pb2.Food, _Mapping]] = ...) -> None: ...

class FoodQuery(_message.Message):
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

class AppendAllPropertiesRequest(_message.Message):
    __slots__ = ("foodId", "properties")
    FOODID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    foodId: str
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, foodId: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class FoodByPropertyRequest(_message.Message):
    __slots__ = ("prop", "sort", "page", "limit")
    PROP_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    prop: _property_pb2.PropertyRef
    sort: Sort
    page: str
    limit: int
    def __init__(self, prop: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., sort: _Optional[_Union[Sort, str]] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class FoodBySourceIdRequest(_message.Message):
    __slots__ = ("sourceIds", "source")
    SOURCEIDS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    sourceIds: _containers.RepeatedScalarFieldContainer[str]
    source: _food_source_pb2.FoodSourceRef
    def __init__(self, sourceIds: _Optional[_Iterable[str]] = ..., source: _Optional[_Union[_food_source_pb2.FoodSourceRef, _Mapping]] = ...) -> None: ...

class FoodBySourceIdResponse(_message.Message):
    __slots__ = ("foods",)
    FOODS_FIELD_NUMBER: _ClassVar[int]
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    def __init__(self, foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ...) -> None: ...

class GetWeightsRequest(_message.Message):
    __slots__ = ("food", "locale")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    locale: _localized_pb2.LocaleRef
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...

class GetWeightsResponse(_message.Message):
    __slots__ = ("weights",)
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    weights: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodWeight]
    def __init__(self, weights: _Optional[_Iterable[_Union[_food_pb2.FoodWeight, _Mapping]]] = ...) -> None: ...

class GetFreeFormWeightsResponse(_message.Message):
    __slots__ = ("weights",)
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    weights: _containers.RepeatedCompositeFieldContainer[_weights_pb2.FreeFormWeight]
    def __init__(self, weights: _Optional[_Iterable[_Union[_weights_pb2.FreeFormWeight, _Mapping]]] = ...) -> None: ...

class AddFreeFormWeightsToSourceIdRequest(_message.Message):
    __slots__ = ("sourceId", "source", "weights")
    SOURCEID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    sourceId: str
    source: _food_source_pb2.FoodSourceRef
    weights: _weights_pb2.FreeFormWeight
    def __init__(self, sourceId: _Optional[str] = ..., source: _Optional[_Union[_food_source_pb2.FoodSourceRef, _Mapping]] = ..., weights: _Optional[_Union[_weights_pb2.FreeFormWeight, _Mapping]] = ...) -> None: ...
