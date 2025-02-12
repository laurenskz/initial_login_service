from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FreeFormWeight(_message.Message):
    __slots__ = ("id", "name", "weightForOneUnit", "isDiscreteOption")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WEIGHTFORONEUNIT_FIELD_NUMBER: _ClassVar[int]
    ISDISCRETEOPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    weightForOneUnit: float
    isDiscreteOption: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., weightForOneUnit: _Optional[float] = ..., isDiscreteOption: bool = ...) -> None: ...

class ModifiableFreeFormWeight(_message.Message):
    __slots__ = ("freeForm", "nameOverride", "weightOverride")
    FREEFORM_FIELD_NUMBER: _ClassVar[int]
    NAMEOVERRIDE_FIELD_NUMBER: _ClassVar[int]
    WEIGHTOVERRIDE_FIELD_NUMBER: _ClassVar[int]
    freeForm: FreeFormWeight
    nameOverride: _localized_pb2.LocalizedString
    weightOverride: float
    def __init__(self, freeForm: _Optional[_Union[FreeFormWeight, _Mapping]] = ..., nameOverride: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., weightOverride: _Optional[float] = ...) -> None: ...

class RangeWeight(_message.Message):
    __slots__ = ("min", "max")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...
