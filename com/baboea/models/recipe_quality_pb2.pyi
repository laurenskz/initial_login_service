from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeQualityFilter(_message.Message):
    __slots__ = ("status", "min_vote_confidence", "min_like_percentage")
    class RecipeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANY: _ClassVar[RecipeQualityFilter.RecipeStatus]
        VERIFIED_ONLY: _ClassVar[RecipeQualityFilter.RecipeStatus]
        COMMUNITY_ONLY: _ClassVar[RecipeQualityFilter.RecipeStatus]
    ANY: RecipeQualityFilter.RecipeStatus
    VERIFIED_ONLY: RecipeQualityFilter.RecipeStatus
    COMMUNITY_ONLY: RecipeQualityFilter.RecipeStatus
    class VoteConfidence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETELY_NEW: _ClassVar[RecipeQualityFilter.VoteConfidence]
        TESTING_WATERS: _ClassVar[RecipeQualityFilter.VoteConfidence]
        GAINING_TRACTION: _ClassVar[RecipeQualityFilter.VoteConfidence]
        POPULAR: _ClassVar[RecipeQualityFilter.VoteConfidence]
        TRIED_AND_TRUE: _ClassVar[RecipeQualityFilter.VoteConfidence]
    COMPLETELY_NEW: RecipeQualityFilter.VoteConfidence
    TESTING_WATERS: RecipeQualityFilter.VoteConfidence
    GAINING_TRACTION: RecipeQualityFilter.VoteConfidence
    POPULAR: RecipeQualityFilter.VoteConfidence
    TRIED_AND_TRUE: RecipeQualityFilter.VoteConfidence
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MIN_VOTE_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    MIN_LIKE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    status: RecipeQualityFilter.RecipeStatus
    min_vote_confidence: RecipeQualityFilter.VoteConfidence
    min_like_percentage: int
    def __init__(self, status: _Optional[_Union[RecipeQualityFilter.RecipeStatus, str]] = ..., min_vote_confidence: _Optional[_Union[RecipeQualityFilter.VoteConfidence, str]] = ..., min_like_percentage: _Optional[int] = ...) -> None: ...
