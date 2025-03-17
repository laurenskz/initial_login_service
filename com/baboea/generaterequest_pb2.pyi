from com.baboea import features_pb2 as _features_pb2
from com.baboea.models import objectivegroup_pb2 as _objectivegroup_pb2
from com.baboea.models import concept_impl_pb2 as _concept_impl_pb2
from com.baboea.models import diet_pb2 as _diet_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.models import days_pb2 as _days_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import dates_pb2 as _dates_pb2
from com.baboea.models import meal_components_pb2 as _meal_components_pb2
from com.baboea import requirement_pb2 as _requirement_pb2
from com.baboea import concept_pb2 as _concept_pb2
from com.baboea.models import users_pb2 as _users_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailedObjectiveReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXCEEDED_LIMIT: _ClassVar[FailedObjectiveReason]
    BELOW_THRESHOLD: _ClassVar[FailedObjectiveReason]
EXCEEDED_LIMIT: FailedObjectiveReason
BELOW_THRESHOLD: FailedObjectiveReason

class UserPlanInput(_message.Message):
    __slots__ = ("user", "desiredDays", "name")
    USER_FIELD_NUMBER: _ClassVar[int]
    DESIREDDAYS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    desiredDays: _containers.RepeatedCompositeFieldContainer[_days_pb2.UserPlanDay]
    name: str
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., desiredDays: _Optional[_Iterable[_Union[_days_pb2.UserPlanDay, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...

class MealPlanGenerateRequest(_message.Message):
    __slots__ = ("user", "dates", "utilizedDayTemplates", "enabledObjectives", "availableMeals", "diet", "availableRecipes", "templateRecipes", "userConceptImpls")
    USER_FIELD_NUMBER: _ClassVar[int]
    DATES_FIELD_NUMBER: _ClassVar[int]
    UTILIZEDDAYTEMPLATES_FIELD_NUMBER: _ClassVar[int]
    ENABLEDOBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEMEALS_FIELD_NUMBER: _ClassVar[int]
    DIET_FIELD_NUMBER: _ClassVar[int]
    AVAILABLERECIPES_FIELD_NUMBER: _ClassVar[int]
    TEMPLATERECIPES_FIELD_NUMBER: _ClassVar[int]
    USERCONCEPTIMPLS_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    dates: _containers.RepeatedCompositeFieldContainer[_days_pb2.UserPlanDay]
    utilizedDayTemplates: _containers.RepeatedCompositeFieldContainer[_days_pb2.MealPlanDay]
    enabledObjectives: _containers.RepeatedCompositeFieldContainer[_objectivegroup_pb2.ObjectiveGroup]
    availableMeals: _containers.RepeatedCompositeFieldContainer[_meal_pb2.Meal]
    diet: _diet_pb2.UserDietDefinition
    availableRecipes: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.Recipe]
    templateRecipes: _containers.RepeatedCompositeFieldContainer[_template_recipe_data_pb2.ImprovedTemplateRecipe]
    userConceptImpls: _containers.RepeatedCompositeFieldContainer[_concept_impl_pb2.ConceptImplementationNode]
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., dates: _Optional[_Iterable[_Union[_days_pb2.UserPlanDay, _Mapping]]] = ..., utilizedDayTemplates: _Optional[_Iterable[_Union[_days_pb2.MealPlanDay, _Mapping]]] = ..., enabledObjectives: _Optional[_Iterable[_Union[_objectivegroup_pb2.ObjectiveGroup, _Mapping]]] = ..., availableMeals: _Optional[_Iterable[_Union[_meal_pb2.Meal, _Mapping]]] = ..., diet: _Optional[_Union[_diet_pb2.UserDietDefinition, _Mapping]] = ..., availableRecipes: _Optional[_Iterable[_Union[_recipes_pb2.Recipe, _Mapping]]] = ..., templateRecipes: _Optional[_Iterable[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipe, _Mapping]]] = ..., userConceptImpls: _Optional[_Iterable[_Union[_concept_impl_pb2.ConceptImplementationNode, _Mapping]]] = ...) -> None: ...

class GroceryGroup(_message.Message):
    __slots__ = ("foods",)
    FOODS_FIELD_NUMBER: _ClassVar[int]
    foods: _containers.RepeatedCompositeFieldContainer[QuantifiedFood]
    def __init__(self, foods: _Optional[_Iterable[_Union[QuantifiedFood, _Mapping]]] = ...) -> None: ...

class GroceryList(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[GroceryGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[GroceryGroup, _Mapping]]] = ...) -> None: ...

class GeneratedMealPlan(_message.Message):
    __slots__ = ("id", "groceryList", "days", "notes", "feasible")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROCERYLIST_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    FEASIBLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    groceryList: GroceryList
    days: _containers.RepeatedCompositeFieldContainer[GeneratedDay]
    notes: _containers.RepeatedCompositeFieldContainer[GeneratedMealPlanNotes]
    feasible: bool
    def __init__(self, id: _Optional[str] = ..., groceryList: _Optional[_Union[GroceryList, _Mapping]] = ..., days: _Optional[_Iterable[_Union[GeneratedDay, _Mapping]]] = ..., notes: _Optional[_Iterable[_Union[GeneratedMealPlanNotes, _Mapping]]] = ..., feasible: bool = ...) -> None: ...

class GeneratedMealPlanNotes(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GeneratedMealPlanRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GeneratedMealPlanQuery(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

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

class FailedObjective(_message.Message):
    __slots__ = ("requirement", "reason", "group")
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    requirement: _objectivegroup_pb2.SpecializedRequirementRef
    reason: FailedObjectiveReason
    group: _objectivegroup_pb2.ObjectiveGroupRef
    def __init__(self, requirement: _Optional[_Union[_objectivegroup_pb2.SpecializedRequirementRef, _Mapping]] = ..., reason: _Optional[_Union[FailedObjectiveReason, str]] = ..., group: _Optional[_Union[_objectivegroup_pb2.ObjectiveGroupRef, _Mapping]] = ...) -> None: ...

class GeneratedDay(_message.Message):
    __slots__ = ("day", "meals", "properties", "failedObjectives")
    DAY_FIELD_NUMBER: _ClassVar[int]
    MEALS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FAILEDOBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    day: _days_pb2.UserPlanDay
    meals: _containers.RepeatedCompositeFieldContainer[GeneratedMeal]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    failedObjectives: _containers.RepeatedCompositeFieldContainer[FailedObjective]
    def __init__(self, day: _Optional[_Union[_days_pb2.UserPlanDay, _Mapping]] = ..., meals: _Optional[_Iterable[_Union[GeneratedMeal, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ..., failedObjectives: _Optional[_Iterable[_Union[FailedObjective, _Mapping]]] = ...) -> None: ...

class GeneratedMetaDay(_message.Message):
    __slots__ = ("pending", "day", "errorMessages")
    PENDING_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGES_FIELD_NUMBER: _ClassVar[int]
    pending: bool
    day: GeneratedDay
    errorMessages: _containers.RepeatedCompositeFieldContainer[_localized_pb2.LocalizedString]
    def __init__(self, pending: bool = ..., day: _Optional[_Union[GeneratedDay, _Mapping]] = ..., errorMessages: _Optional[_Iterable[_Union[_localized_pb2.LocalizedString, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("component", "recipe", "userRecipe", "templateRecipe", "foods", "properties")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    USERRECIPE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATERECIPE_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    component: _meal_components_pb2.MealComponentRef
    recipe: _recipes_pb2.ParsedRemoteRecipeRef
    userRecipe: _recipes_pb2.RecipeRef
    templateRecipe: _template_recipe_data_pb2.ImprovedTemplateRecipeRef
    foods: _containers.RepeatedCompositeFieldContainer[QuantifiedFood]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    def __init__(self, component: _Optional[_Union[_meal_components_pb2.MealComponentRef, _Mapping]] = ..., recipe: _Optional[_Union[_recipes_pb2.ParsedRemoteRecipeRef, _Mapping]] = ..., userRecipe: _Optional[_Union[_recipes_pb2.RecipeRef, _Mapping]] = ..., templateRecipe: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipeRef, _Mapping]] = ..., foods: _Optional[_Iterable[_Union[QuantifiedFood, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

class QuantifiedFood(_message.Message):
    __slots__ = ("food", "quantity")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    quantity: float
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., quantity: _Optional[float] = ...) -> None: ...
