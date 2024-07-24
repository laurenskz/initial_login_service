from com.baboea import features_pb2 as _features_pb2
from com.baboea.models import objectivegroup_pb2 as _objectivegroup_pb2
from com.baboea.models import diet_pb2 as _diet_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import days_pb2 as _days_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import meal_components_pb2 as _meal_components_pb2
from com.baboea import requirement_pb2 as _requirement_pb2
from com.baboea import concept_pb2 as _concept_pb2
from com.baboea.models import users_pb2 as _users_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserPlanInput(_message.Message):
    __slots__ = ("user", "desiredDays")
    USER_FIELD_NUMBER: _ClassVar[int]
    DESIREDDAYS_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    desiredDays: _containers.RepeatedCompositeFieldContainer[_days_pb2.MealPlanDayRef]
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., desiredDays: _Optional[_Iterable[_Union[_days_pb2.MealPlanDayRef, _Mapping]]] = ...) -> None: ...

class MealPlanGenerateRequest(_message.Message):
    __slots__ = ("user", "desiredDays", "enabledObjectives", "availableMeals", "diet")
    USER_FIELD_NUMBER: _ClassVar[int]
    DESIREDDAYS_FIELD_NUMBER: _ClassVar[int]
    ENABLEDOBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEMEALS_FIELD_NUMBER: _ClassVar[int]
    DIET_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    desiredDays: _containers.RepeatedCompositeFieldContainer[_days_pb2.MealPlanDay]
    enabledObjectives: _containers.RepeatedCompositeFieldContainer[_objectivegroup_pb2.ObjectiveGroup]
    availableMeals: _containers.RepeatedCompositeFieldContainer[_meal_pb2.Meal]
    diet: _diet_pb2.UserDietDefinition
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., desiredDays: _Optional[_Iterable[_Union[_days_pb2.MealPlanDay, _Mapping]]] = ..., enabledObjectives: _Optional[_Iterable[_Union[_objectivegroup_pb2.ObjectiveGroup, _Mapping]]] = ..., availableMeals: _Optional[_Iterable[_Union[_meal_pb2.Meal, _Mapping]]] = ..., diet: _Optional[_Union[_diet_pb2.UserDietDefinition, _Mapping]] = ...) -> None: ...

class GeneratedMealPlan(_message.Message):
    __slots__ = ("days",)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: _containers.RepeatedCompositeFieldContainer[GeneratedDay]
    def __init__(self, days: _Optional[_Iterable[_Union[GeneratedDay, _Mapping]]] = ...) -> None: ...

class GenerateRefResolution(_message.Message):
    __slots__ = ("properties", "foods", "recipes", "user", "locale")
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyRef]
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    recipes: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.ParsedRemoteRecipeRef]
    user: _users_pb2.UserRef
    locale: _localized_pb2.LocaleRef
    def __init__(self, properties: _Optional[_Iterable[_Union[_property_pb2.PropertyRef, _Mapping]]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ..., recipes: _Optional[_Iterable[_Union[_recipes_pb2.ParsedRemoteRecipeRef, _Mapping]]] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...

class GeneratedDay(_message.Message):
    __slots__ = ("day", "meals", "properties")
    DAY_FIELD_NUMBER: _ClassVar[int]
    MEALS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    day: _days_pb2.MealPlanDayRef
    meals: _containers.RepeatedCompositeFieldContainer[GeneratedMeal]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, day: _Optional[_Union[_days_pb2.MealPlanDayRef, _Mapping]] = ..., meals: _Optional[_Iterable[_Union[GeneratedMeal, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class GeneratedMeal(_message.Message):
    __slots__ = ("meal", "components", "properties")
    MEAL_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    meal: _meal_pb2.MealRef
    components: _containers.RepeatedCompositeFieldContainer[GeneratedMealComponent]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, meal: _Optional[_Union[_meal_pb2.MealRef, _Mapping]] = ..., components: _Optional[_Iterable[_Union[GeneratedMealComponent, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class GeneratedMealComponent(_message.Message):
    __slots__ = ("component", "recipe", "foods", "properties")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    component: _meal_components_pb2.MealComponentRef
    recipe: _recipes_pb2.ParsedRemoteRecipeRef
    foods: _containers.RepeatedCompositeFieldContainer[QuantifiedFood]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, component: _Optional[_Union[_meal_components_pb2.MealComponentRef, _Mapping]] = ..., recipe: _Optional[_Union[_recipes_pb2.ParsedRemoteRecipeRef, _Mapping]] = ..., foods: _Optional[_Iterable[_Union[QuantifiedFood, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class QuantifiedFood(_message.Message):
    __slots__ = ("food", "quantity")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    quantity: float
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., quantity: _Optional[float] = ...) -> None: ...
