from com.baboea import nutrient_pb2 as _nutrient_pb2
from com.baboea import qualifier_pb2 as _qualifier_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BaseProperty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOOD_COUNT: _ClassVar[BaseProperty]
    WEIGHT: _ClassVar[BaseProperty]
    RECIPE_COUNT: _ClassVar[BaseProperty]
FOOD_COUNT: BaseProperty
WEIGHT: BaseProperty
RECIPE_COUNT: BaseProperty
