from com.baboea import baseproperty_pb2 as _baseproperty_pb2
from com.baboea import foodgroup_pb2 as _foodgroup_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Aggregation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[Aggregation]
    SUM: _ClassVar[Aggregation]
    AVG: _ClassVar[Aggregation]
NONE: Aggregation
SUM: Aggregation
AVG: Aggregation

class FoodGroupSpecifier(_message.Message):
    __slots__ = ("foodGroups",)
    FOODGROUPS_FIELD_NUMBER: _ClassVar[int]
    foodGroups: _containers.RepeatedCompositeFieldContainer[_foodgroup_pb2.FoodGroupIdentifier]
    def __init__(self, foodGroups: _Optional[_Iterable[_Union[_foodgroup_pb2.FoodGroupIdentifier, _Mapping]]] = ...) -> None: ...

class Property(_message.Message):
    __slots__ = ("id", "base")
    ID_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    base: _baseproperty_pb2.BaseProperty
    def __init__(self, id: _Optional[str] = ..., base: _Optional[_Union[_baseproperty_pb2.BaseProperty, str]] = ...) -> None: ...

class SelectAll(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelectIds(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class SelectComplement(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class Selector(_message.Message):
    __slots__ = ("property", "foodGroups", "all", "ids", "complement", "aggregation")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    FOODGROUPS_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    property: Property
    foodGroups: _containers.RepeatedCompositeFieldContainer[_foodgroup_pb2.FoodGroupIdentifier]
    all: SelectAll
    ids: SelectIds
    complement: SelectComplement
    aggregation: Aggregation
    def __init__(self, property: _Optional[_Union[Property, _Mapping]] = ..., foodGroups: _Optional[_Iterable[_Union[_foodgroup_pb2.FoodGroupIdentifier, _Mapping]]] = ..., all: _Optional[_Union[SelectAll, _Mapping]] = ..., ids: _Optional[_Union[SelectIds, _Mapping]] = ..., complement: _Optional[_Union[SelectComplement, _Mapping]] = ..., aggregation: _Optional[_Union[Aggregation, str]] = ...) -> None: ...

class UnAppliedSelector(_message.Message):
    __slots__ = ("property", "all", "ids", "complement", "aggregation")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    property: Property
    all: SelectAll
    ids: SelectIds
    complement: SelectComplement
    aggregation: Aggregation
    def __init__(self, property: _Optional[_Union[Property, _Mapping]] = ..., all: _Optional[_Union[SelectAll, _Mapping]] = ..., ids: _Optional[_Union[SelectIds, _Mapping]] = ..., complement: _Optional[_Union[SelectComplement, _Mapping]] = ..., aggregation: _Optional[_Union[Aggregation, str]] = ...) -> None: ...
