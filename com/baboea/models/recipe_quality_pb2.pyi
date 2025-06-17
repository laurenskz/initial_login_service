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
        VOTE_VERIFIED_ONLY: _ClassVar[RecipeQualityFilter.VoteConfidence]
        COMPLETELY_NEW: _ClassVar[RecipeQualityFilter.VoteConfidence]
        VERIFIED_AND_USER_TESTED: _ClassVar[RecipeQualityFilter.VoteConfidence]
        EVERYTHING: _ClassVar[RecipeQualityFilter.VoteConfidence]
    VOTE_VERIFIED_ONLY: RecipeQualityFilter.VoteConfidence
    COMPLETELY_NEW: RecipeQualityFilter.VoteConfidence
    VERIFIED_AND_USER_TESTED: RecipeQualityFilter.VoteConfidence
    EVERYTHING: RecipeQualityFilter.VoteConfidence
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MIN_VOTE_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    MIN_LIKE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    status: RecipeQualityFilter.RecipeStatus
    min_vote_confidence: RecipeQualityFilter.VoteConfidence
    min_like_percentage: int
    def __init__(self, status: _Optional[_Union[RecipeQualityFilter.RecipeStatus, str]] = ..., min_vote_confidence: _Optional[_Union[RecipeQualityFilter.VoteConfidence, str]] = ..., min_like_percentage: _Optional[int] = ...) -> None: ...
