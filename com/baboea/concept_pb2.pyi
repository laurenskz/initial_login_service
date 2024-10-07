from com.baboea.models import concept_tag_pb2 as _concept_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class ConceptTagStatus(_message.Message):
    __slots__ = ("tag", "status")
    TAG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    tag: _concept_tag_pb2.ConceptTagRef
    status: bool
    def __init__(self, tag: _Optional[_Union[_concept_tag_pb2.ConceptTagRef, _Mapping]] = ..., status: bool = ...) -> None: ...

class BoolConceptValues(_message.Message):
    __slots__ = ("conceptValues", "foodValues", "tagPreferences")
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
    TAGPREFERENCES_FIELD_NUMBER: _ClassVar[int]
    conceptValues: _containers.ScalarMap[str, bool]
    foodValues: _containers.ScalarMap[str, bool]
    tagPreferences: _containers.RepeatedCompositeFieldContainer[ConceptTagStatus]
    def __init__(self, conceptValues: _Optional[_Mapping[str, bool]] = ..., foodValues: _Optional[_Mapping[str, bool]] = ..., tagPreferences: _Optional[_Iterable[_Union[ConceptTagStatus, _Mapping]]] = ...) -> None: ...

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
