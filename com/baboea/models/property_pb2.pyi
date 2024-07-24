from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import food_units_pb2 as _food_units_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropertyRef(_message.Message):
    __slots__ = ("id", "name", "handle")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    handle: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., handle: _Optional[str] = ...) -> None: ...

class Property(_message.Message):
    __slots__ = ("id", "handle", "localizations", "defaultUnit")
    ID_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULTUNIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    handle: str
    localizations: _containers.RepeatedCompositeFieldContainer[PropertyLocalized]
    defaultUnit: _food_units_pb2.FoodUnitRef
    def __init__(self, id: _Optional[str] = ..., handle: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[PropertyLocalized, _Mapping]]] = ..., defaultUnit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ...) -> None: ...

class PropertyLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class PropertyValue(_message.Message):
    __slots__ = ("property", "value")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    property: PropertyRef
    value: float
    def __init__(self, property: _Optional[_Union[PropertyRef, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...
