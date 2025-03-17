from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plugin(_message.Message):
    __slots__ = ("id", "localizations", "variables", "address", "port")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[PluginLocalized]
    variables: _containers.RepeatedCompositeFieldContainer[PluginVariableRef]
    address: str
    port: int
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[PluginLocalized, _Mapping]]] = ..., variables: _Optional[_Iterable[_Union[PluginVariableRef, _Mapping]]] = ..., address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class PluginRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class PluginLocalized(_message.Message):
    __slots__ = ("name", "description", "locale")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    locale: _localized_pb2.LocaleRef
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...

class PluginVariable(_message.Message):
    __slots__ = ("id", "localizations", "defaultValue", "handle")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[PluginVariableLocalized]
    defaultValue: str
    handle: str
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[PluginVariableLocalized, _Mapping]]] = ..., defaultValue: _Optional[str] = ..., handle: _Optional[str] = ...) -> None: ...

class PluginVariableRef(_message.Message):
    __slots__ = ("id", "name", "handle")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    handle: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., handle: _Optional[str] = ...) -> None: ...

class InstantiatedPluginVariable(_message.Message):
    __slots__ = ("variable", "value")
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    variable: PluginVariableRef
    value: str
    def __init__(self, variable: _Optional[_Union[PluginVariableRef, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class VariableValue(_message.Message):
    __slots__ = ("floatValue", "intValue", "stringValue")
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    floatValue: FloatVariableValue
    intValue: IntVariableValue
    stringValue: StringVariableValue
    def __init__(self, floatValue: _Optional[_Union[FloatVariableValue, _Mapping]] = ..., intValue: _Optional[_Union[IntVariableValue, _Mapping]] = ..., stringValue: _Optional[_Union[StringVariableValue, _Mapping]] = ...) -> None: ...

class FloatVariableValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class IntVariableValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class StringVariableValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class PluginVariableLocalized(_message.Message):
    __slots__ = ("name", "description", "locale")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    locale: _localized_pb2.LocaleRef
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...
