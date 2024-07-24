from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PortionSize(_message.Message):
    __slots__ = ("min", "max", "step")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    step: float
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., step: _Optional[float] = ...) -> None: ...

class BoolConceptValues(_message.Message):
    __slots__ = ("conceptValues", "foodValues")
    class ConceptValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class FoodValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    CONCEPTVALUES_FIELD_NUMBER: _ClassVar[int]
    FOODVALUES_FIELD_NUMBER: _ClassVar[int]
    conceptValues: _containers.ScalarMap[str, bool]
    foodValues: _containers.ScalarMap[str, bool]
    def __init__(self, conceptValues: _Optional[_Mapping[str, bool]] = ..., foodValues: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class PortionConceptValues(_message.Message):
    __slots__ = ("conceptValues", "foodValues")
    class ConceptValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PortionSize
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PortionSize, _Mapping]] = ...) -> None: ...
    class FoodValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PortionSize
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PortionSize, _Mapping]] = ...) -> None: ...
    CONCEPTVALUES_FIELD_NUMBER: _ClassVar[int]
    FOODVALUES_FIELD_NUMBER: _ClassVar[int]
    conceptValues: _containers.MessageMap[str, PortionSize]
    foodValues: _containers.MessageMap[str, PortionSize]
    def __init__(self, conceptValues: _Optional[_Mapping[str, PortionSize]] = ..., foodValues: _Optional[_Mapping[str, PortionSize]] = ...) -> None: ...
