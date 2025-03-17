from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import days_pb2 as _days_pb2
from com.baboea.models import plugins_pb2 as _plugins_pb2
from com.baboea import generaterequest_pb2 as _generaterequest_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MealPlanPluginDay(_message.Message):
    __slots__ = ("day", "variables")
    DAY_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    day: _days_pb2.UserPlanDay
    variables: _containers.RepeatedCompositeFieldContainer[_plugins_pb2.InstantiatedPluginVariable]
    def __init__(self, day: _Optional[_Union[_days_pb2.UserPlanDay, _Mapping]] = ..., variables: _Optional[_Iterable[_Union[_plugins_pb2.InstantiatedPluginVariable, _Mapping]]] = ...) -> None: ...

class MealPlanPluginTransformRequest(_message.Message):
    __slots__ = ("generateRequest", "days")
    GENERATEREQUEST_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    generateRequest: _generaterequest_pb2.MealPlanGenerateRequest
    days: _containers.RepeatedCompositeFieldContainer[MealPlanPluginDay]
    def __init__(self, generateRequest: _Optional[_Union[_generaterequest_pb2.MealPlanGenerateRequest, _Mapping]] = ..., days: _Optional[_Iterable[_Union[MealPlanPluginDay, _Mapping]]] = ...) -> None: ...

class MealPlanPluginTransformResponse(_message.Message):
    __slots__ = ("transformed",)
    TRANSFORMED_FIELD_NUMBER: _ClassVar[int]
    transformed: _generaterequest_pb2.MealPlanGenerateRequest
    def __init__(self, transformed: _Optional[_Union[_generaterequest_pb2.MealPlanGenerateRequest, _Mapping]] = ...) -> None: ...
