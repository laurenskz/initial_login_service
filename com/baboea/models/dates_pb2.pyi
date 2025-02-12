from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MONDAY: _ClassVar[DayOfWeek]
    TUESDAY: _ClassVar[DayOfWeek]
    WEDNESDAY: _ClassVar[DayOfWeek]
    THURSDAY: _ClassVar[DayOfWeek]
    FRIDAY: _ClassVar[DayOfWeek]
    SATURDAY: _ClassVar[DayOfWeek]
    SUNDAY: _ClassVar[DayOfWeek]
MONDAY: DayOfWeek
TUESDAY: DayOfWeek
WEDNESDAY: DayOfWeek
THURSDAY: DayOfWeek
FRIDAY: DayOfWeek
SATURDAY: DayOfWeek
SUNDAY: DayOfWeek

class CalendarDate(_message.Message):
    __slots__ = ("year", "month", "day")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    day: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...
