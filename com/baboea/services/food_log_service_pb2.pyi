from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea import generaterequest_pb2 as _generaterequest_pb2
from com.baboea.models import dates_pb2 as _dates_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.models import meal_components_pb2 as _meal_components_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFoodLogDayRequest(_message.Message):
    __slots__ = ("user", "date", "locale")
    USER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    date: _dates_pb2.CalendarDate
    locale: _localized_pb2.LocaleRef
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., date: _Optional[_Union[_dates_pb2.CalendarDate, _Mapping]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...

class PropertyTarget(_message.Message):
    __slots__ = ("property", "useMin", "useMax", "min", "max")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    USEMIN_FIELD_NUMBER: _ClassVar[int]
    USEMAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    property: _property_pb2.PropertyRef
    useMin: bool
    useMax: bool
    min: float
    max: float
    def __init__(self, property: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., useMin: bool = ..., useMax: bool = ..., min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...

class FoodRefWithProperties(_message.Message):
    __slots__ = ("food", "properties")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class GeneratedDayWithReferencedFoods(_message.Message):
    __slots__ = ("day", "referencedFoods", "referencedProperties", "targets")
    DAY_FIELD_NUMBER: _ClassVar[int]
    REFERENCEDFOODS_FIELD_NUMBER: _ClassVar[int]
    REFERENCEDPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    day: _generaterequest_pb2.GeneratedDay
    referencedFoods: _containers.RepeatedCompositeFieldContainer[FoodRefWithProperties]
    referencedProperties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyRef]
    targets: _containers.RepeatedCompositeFieldContainer[PropertyTarget]
    def __init__(self, day: _Optional[_Union[_generaterequest_pb2.GeneratedDay, _Mapping]] = ..., referencedFoods: _Optional[_Iterable[_Union[FoodRefWithProperties, _Mapping]]] = ..., referencedProperties: _Optional[_Iterable[_Union[_property_pb2.PropertyRef, _Mapping]]] = ..., targets: _Optional[_Iterable[_Union[PropertyTarget, _Mapping]]] = ...) -> None: ...

class FoodLogMealSpecifier(_message.Message):
    __slots__ = ("date", "meal", "user", "component", "recipe", "userRecipe", "templateRecipe")
    DATE_FIELD_NUMBER: _ClassVar[int]
    MEAL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    USERRECIPE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATERECIPE_FIELD_NUMBER: _ClassVar[int]
    date: _dates_pb2.CalendarDate
    meal: _meal_pb2.MealRef
    user: _users_pb2.UserRef
    component: _meal_components_pb2.MealComponentRef
    recipe: _recipes_pb2.ParsedRemoteRecipeRef
    userRecipe: _recipes_pb2.RecipeRef
    templateRecipe: _template_recipe_data_pb2.ImprovedTemplateRecipeRef
    def __init__(self, date: _Optional[_Union[_dates_pb2.CalendarDate, _Mapping]] = ..., meal: _Optional[_Union[_meal_pb2.MealRef, _Mapping]] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., component: _Optional[_Union[_meal_components_pb2.MealComponentRef, _Mapping]] = ..., recipe: _Optional[_Union[_recipes_pb2.ParsedRemoteRecipeRef, _Mapping]] = ..., userRecipe: _Optional[_Union[_recipes_pb2.RecipeRef, _Mapping]] = ..., templateRecipe: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipeRef, _Mapping]] = ...) -> None: ...

class AddFoodRequest(_message.Message):
    __slots__ = ("food", "specifier")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    SPECIFIER_FIELD_NUMBER: _ClassVar[int]
    food: _generaterequest_pb2.QuantifiedFood
    specifier: FoodLogMealSpecifier
    def __init__(self, food: _Optional[_Union[_generaterequest_pb2.QuantifiedFood, _Mapping]] = ..., specifier: _Optional[_Union[FoodLogMealSpecifier, _Mapping]] = ...) -> None: ...

class UpdateFoodRequest(_message.Message):
    __slots__ = ("food", "specifier")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    SPECIFIER_FIELD_NUMBER: _ClassVar[int]
    food: _generaterequest_pb2.QuantifiedFood
    specifier: FoodLogMealSpecifier
    def __init__(self, food: _Optional[_Union[_generaterequest_pb2.QuantifiedFood, _Mapping]] = ..., specifier: _Optional[_Union[FoodLogMealSpecifier, _Mapping]] = ...) -> None: ...

class ReplaceFoodRequest(_message.Message):
    __slots__ = ("originalFood", "specifier", "newFood")
    ORIGINALFOOD_FIELD_NUMBER: _ClassVar[int]
    SPECIFIER_FIELD_NUMBER: _ClassVar[int]
    NEWFOOD_FIELD_NUMBER: _ClassVar[int]
    originalFood: _food_pb2.FoodRef
    specifier: FoodLogMealSpecifier
    newFood: _food_pb2.FoodRef
    def __init__(self, originalFood: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., specifier: _Optional[_Union[FoodLogMealSpecifier, _Mapping]] = ..., newFood: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ...) -> None: ...

class DeleteFoodRequest(_message.Message):
    __slots__ = ("food", "specifier")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    SPECIFIER_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    specifier: FoodLogMealSpecifier
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., specifier: _Optional[_Union[FoodLogMealSpecifier, _Mapping]] = ...) -> None: ...

class NewDailyPropertiesResponse(_message.Message):
    __slots__ = ("newDailyProperties",)
    NEWDAILYPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    newDailyProperties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, newDailyProperties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class SaveDayRequest(_message.Message):
    __slots__ = ("user", "day")
    USER_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    day: _generaterequest_pb2.GeneratedDay
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., day: _Optional[_Union[_generaterequest_pb2.GeneratedDay, _Mapping]] = ...) -> None: ...

class SetDayToPendingRequest(_message.Message):
    __slots__ = ("user", "date")
    USER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    date: _dates_pb2.CalendarDate
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., date: _Optional[_Union[_dates_pb2.CalendarDate, _Mapping]] = ...) -> None: ...

class GetShoppingListFoodsRequest(_message.Message):
    __slots__ = ("startDateInclusive", "endDateInclusive", "locale", "user")
    STARTDATEINCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    ENDDATEINCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    startDateInclusive: _dates_pb2.CalendarDate
    endDateInclusive: _dates_pb2.CalendarDate
    locale: _localized_pb2.LocaleRef
    user: _users_pb2.UserRef
    def __init__(self, startDateInclusive: _Optional[_Union[_dates_pb2.CalendarDate, _Mapping]] = ..., endDateInclusive: _Optional[_Union[_dates_pb2.CalendarDate, _Mapping]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class GetShoppingListFoodsResponse(_message.Message):
    __slots__ = ("foods",)
    FOODS_FIELD_NUMBER: _ClassVar[int]
    foods: _containers.RepeatedCompositeFieldContainer[_generaterequest_pb2.QuantifiedFood]
    def __init__(self, foods: _Optional[_Iterable[_Union[_generaterequest_pb2.QuantifiedFood, _Mapping]]] = ...) -> None: ...
