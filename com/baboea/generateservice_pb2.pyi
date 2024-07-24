from com.baboea import generaterequest_pb2 as _generaterequest_pb2
from com.baboea import foodgroup_pb2 as _foodgroup_pb2
from com.baboea import selector_pb2 as _selector_pb2
from com.baboea.models import food_pb2 as _food_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratedFoodList(_message.Message):
    __slots__ = ("foods",)
    FOODS_FIELD_NUMBER: _ClassVar[int]
    foods: _containers.RepeatedCompositeFieldContainer[GeneratedFood]
    def __init__(self, foods: _Optional[_Iterable[_Union[GeneratedFood, _Mapping]]] = ...) -> None: ...

class GeneratedFood(_message.Message):
    __slots__ = ("food", "weight")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    weight: float
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., weight: _Optional[float] = ...) -> None: ...

class PropertyValueInformation(_message.Message):
    __slots__ = ("property", "value")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    property: _selector_pb2.Property
    value: float
    def __init__(self, property: _Optional[_Union[_selector_pb2.Property, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class PropertyValueInformationList(_message.Message):
    __slots__ = ("properties",)
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[PropertyValueInformation]
    def __init__(self, properties: _Optional[_Iterable[_Union[PropertyValueInformation, _Mapping]]] = ...) -> None: ...

class RecipeInstructions(_message.Message):
    __slots__ = ("instructions",)
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    def __init__(self, instructions: _Optional[str] = ...) -> None: ...

class GenerateInformation(_message.Message):
    __slots__ = ("foods", "properties", "instructions")
    FOODS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    foods: GeneratedFoodList
    properties: PropertyValueInformationList
    instructions: RecipeInstructions
    def __init__(self, foods: _Optional[_Union[GeneratedFoodList, _Mapping]] = ..., properties: _Optional[_Union[PropertyValueInformationList, _Mapping]] = ..., instructions: _Optional[_Union[RecipeInstructions, _Mapping]] = ...) -> None: ...

class GeneratedFoodTree(_message.Message):
    __slots__ = ("children", "infoNodes", "node")
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    INFONODES_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[GeneratedFoodTree]
    infoNodes: _containers.RepeatedCompositeFieldContainer[GenerateInformation]
    node: _foodgroup_pb2.FoodGroupNode
    def __init__(self, children: _Optional[_Iterable[_Union[GeneratedFoodTree, _Mapping]]] = ..., infoNodes: _Optional[_Iterable[_Union[GenerateInformation, _Mapping]]] = ..., node: _Optional[_Union[_foodgroup_pb2.FoodGroupNode, _Mapping]] = ...) -> None: ...

class GenerateSuccess(_message.Message):
    __slots__ = ("tree",)
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _containers.RepeatedCompositeFieldContainer[GeneratedFoodTree]
    def __init__(self, tree: _Optional[_Iterable[_Union[GeneratedFoodTree, _Mapping]]] = ...) -> None: ...

class GenerateFailure(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GenerateResponse(_message.Message):
    __slots__ = ("error", "plan")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    error: GenerateFailure
    plan: _generaterequest_pb2.GeneratedMealPlan
    def __init__(self, error: _Optional[_Union[GenerateFailure, _Mapping]] = ..., plan: _Optional[_Union[_generaterequest_pb2.GeneratedMealPlan, _Mapping]] = ...) -> None: ...
