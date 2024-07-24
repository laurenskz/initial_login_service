from com.baboea.models import localized_pb2 as _localized_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchSet(_message.Message):
    __slots__ = ("locale", "positiveRegexes", "negativeRegexes")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    POSITIVEREGEXES_FIELD_NUMBER: _ClassVar[int]
    NEGATIVEREGEXES_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    positiveRegexes: _containers.RepeatedScalarFieldContainer[str]
    negativeRegexes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., positiveRegexes: _Optional[_Iterable[str]] = ..., negativeRegexes: _Optional[_Iterable[str]] = ...) -> None: ...
