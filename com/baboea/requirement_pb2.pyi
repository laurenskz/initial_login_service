from com.baboea import selector_pb2 as _selector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GiveReward(_message.Message):
    __slots__ = ("weight",)
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    weight: float
    def __init__(self, weight: _Optional[float] = ...) -> None: ...

class AtLeast(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class AtMost(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class RequirementType(_message.Message):
    __slots__ = ("giveReward", "atLeast", "atMost")
    GIVEREWARD_FIELD_NUMBER: _ClassVar[int]
    ATLEAST_FIELD_NUMBER: _ClassVar[int]
    ATMOST_FIELD_NUMBER: _ClassVar[int]
    giveReward: GiveReward
    atLeast: AtLeast
    atMost: AtMost
    def __init__(self, giveReward: _Optional[_Union[GiveReward, _Mapping]] = ..., atLeast: _Optional[_Union[AtLeast, _Mapping]] = ..., atMost: _Optional[_Union[AtMost, _Mapping]] = ...) -> None: ...

class RatioRequirementType(_message.Message):
    __slots__ = ("atLeast", "atMost")
    ATLEAST_FIELD_NUMBER: _ClassVar[int]
    ATMOST_FIELD_NUMBER: _ClassVar[int]
    atLeast: AtLeast
    atMost: AtMost
    def __init__(self, atLeast: _Optional[_Union[AtLeast, _Mapping]] = ..., atMost: _Optional[_Union[AtMost, _Mapping]] = ...) -> None: ...

class Requirement(_message.Message):
    __slots__ = ("normal", "ratio")
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    RATIO_FIELD_NUMBER: _ClassVar[int]
    normal: NormalRequirement
    ratio: RatioRequirement
    def __init__(self, normal: _Optional[_Union[NormalRequirement, _Mapping]] = ..., ratio: _Optional[_Union[RatioRequirement, _Mapping]] = ...) -> None: ...

class NormalRequirement(_message.Message):
    __slots__ = ("selector", "type")
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    selector: _selector_pb2.Selector
    type: RequirementType
    def __init__(self, selector: _Optional[_Union[_selector_pb2.Selector, _Mapping]] = ..., type: _Optional[_Union[RequirementType, _Mapping]] = ...) -> None: ...

class RatioRequirement(_message.Message):
    __slots__ = ("numerator", "denominator", "type")
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    numerator: _selector_pb2.Selector
    denominator: _selector_pb2.Selector
    type: RatioRequirementType
    def __init__(self, numerator: _Optional[_Union[_selector_pb2.Selector, _Mapping]] = ..., denominator: _Optional[_Union[_selector_pb2.Selector, _Mapping]] = ..., type: _Optional[_Union[RatioRequirementType, _Mapping]] = ...) -> None: ...

class UnAppliedNormalRequirement(_message.Message):
    __slots__ = ("selector", "type")
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    selector: _selector_pb2.UnAppliedSelector
    type: RequirementType
    def __init__(self, selector: _Optional[_Union[_selector_pb2.UnAppliedSelector, _Mapping]] = ..., type: _Optional[_Union[RequirementType, _Mapping]] = ...) -> None: ...

class UnAppliedRatioRequirement(_message.Message):
    __slots__ = ("numerator", "denominator", "type")
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    numerator: _selector_pb2.UnAppliedSelector
    denominator: _selector_pb2.UnAppliedSelector
    type: RatioRequirementType
    def __init__(self, numerator: _Optional[_Union[_selector_pb2.UnAppliedSelector, _Mapping]] = ..., denominator: _Optional[_Union[_selector_pb2.UnAppliedSelector, _Mapping]] = ..., type: _Optional[_Union[RatioRequirementType, _Mapping]] = ...) -> None: ...

class UnAppliedRequirement(_message.Message):
    __slots__ = ("normal", "ratio")
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    RATIO_FIELD_NUMBER: _ClassVar[int]
    normal: UnAppliedNormalRequirement
    ratio: UnAppliedRatioRequirement
    def __init__(self, normal: _Optional[_Union[UnAppliedNormalRequirement, _Mapping]] = ..., ratio: _Optional[_Union[UnAppliedRatioRequirement, _Mapping]] = ...) -> None: ...
