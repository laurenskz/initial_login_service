from com.baboea.models import days_pb2 as _days_pb2
from com.baboea.models import meal_components_pb2 as _meal_components_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MealComponentGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIDES: _ClassVar[MealComponentGroup]
    RECIPES: _ClassVar[MealComponentGroup]
SIDES: MealComponentGroup
RECIPES: MealComponentGroup

class Root(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FoodGroupNode(_message.Message):
    __slots__ = ("day", "meal", "mealComponent", "recipe", "userRecipe")
    DAY_FIELD_NUMBER: _ClassVar[int]
    MEAL_FIELD_NUMBER: _ClassVar[int]
    MEALCOMPONENT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    USERRECIPE_FIELD_NUMBER: _ClassVar[int]
    day: _days_pb2.MealPlanDayRef
    meal: _meal_pb2.MealRef
    mealComponent: _meal_components_pb2.MealComponentRef
    recipe: _recipes_pb2.ParsedRemoteRecipeRef
    userRecipe: _recipes_pb2.RecipeRef
    def __init__(self, day: _Optional[_Union[_days_pb2.MealPlanDayRef, _Mapping]] = ..., meal: _Optional[_Union[_meal_pb2.MealRef, _Mapping]] = ..., mealComponent: _Optional[_Union[_meal_components_pb2.MealComponentRef, _Mapping]] = ..., recipe: _Optional[_Union[_recipes_pb2.ParsedRemoteRecipeRef, _Mapping]] = ..., userRecipe: _Optional[_Union[_recipes_pb2.RecipeRef, _Mapping]] = ...) -> None: ...

class FoodGroupIdentifier(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedCompositeFieldContainer[FoodGroupNode]
    def __init__(self, path: _Optional[_Iterable[_Union[FoodGroupNode, _Mapping]]] = ...) -> None: ...

class RecipeNode(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
