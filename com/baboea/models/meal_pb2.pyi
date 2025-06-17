from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import recipe_quality_pb2 as _recipe_quality_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.models import foodgroup_pb2 as _foodgroup_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea import concept_pb2 as _concept_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscreteMealSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEAL_SIZE_TINY: _ClassVar[DiscreteMealSize]
    MEAL_SIZE_SMALL: _ClassVar[DiscreteMealSize]
    MEAL_SIZE_MEDIUM: _ClassVar[DiscreteMealSize]
    MEAL_SIZE_LARGE: _ClassVar[DiscreteMealSize]
    MEAL_SIZE_HUGE: _ClassVar[DiscreteMealSize]

class MealType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BREAKFAST: _ClassVar[MealType]
    LUNCH: _ClassVar[MealType]
    DINNER: _ClassVar[MealType]
    SNACK: _ClassVar[MealType]
    PRE_WORKOUT: _ClassVar[MealType]
    INTRA_WORKOUT: _ClassVar[MealType]
    POST_WORKOUT: _ClassVar[MealType]
    DESSERT: _ClassVar[MealType]
MEAL_SIZE_TINY: DiscreteMealSize
MEAL_SIZE_SMALL: DiscreteMealSize
MEAL_SIZE_MEDIUM: DiscreteMealSize
MEAL_SIZE_LARGE: DiscreteMealSize
MEAL_SIZE_HUGE: DiscreteMealSize
BREAKFAST: MealType
LUNCH: MealType
DINNER: MealType
SNACK: MealType
PRE_WORKOUT: MealType
INTRA_WORKOUT: MealType
POST_WORKOUT: MealType
DESSERT: MealType

class MealRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Meal(_message.Message):
    __slots__ = ("id", "name", "description", "owner", "smartRecipes", "concepts", "recipes", "templateRecipes", "balanced", "maxSideKcalPercentage", "enableSides", "maxSideFoods", "simplifiedSides")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SMARTRECIPES_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    TEMPLATERECIPES_FIELD_NUMBER: _ClassVar[int]
    BALANCED_FIELD_NUMBER: _ClassVar[int]
    MAXSIDEKCALPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ENABLESIDES_FIELD_NUMBER: _ClassVar[int]
    MAXSIDEFOODS_FIELD_NUMBER: _ClassVar[int]
    SIMPLIFIEDSIDES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    owner: _users_pb2.UserRef
    smartRecipes: SmartRecipePreferences
    concepts: _concept_pb2.BoolConceptValues
    recipes: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeRef]
    templateRecipes: _containers.RepeatedCompositeFieldContainer[_template_recipe_data_pb2.ImprovedTemplateRecipeRef]
    balanced: bool
    maxSideKcalPercentage: float
    enableSides: bool
    maxSideFoods: int
    simplifiedSides: _containers.RepeatedCompositeFieldContainer[SimplifiedSideFoodOption]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., smartRecipes: _Optional[_Union[SmartRecipePreferences, _Mapping]] = ..., concepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., recipes: _Optional[_Iterable[_Union[_recipes_pb2.RecipeRef, _Mapping]]] = ..., templateRecipes: _Optional[_Iterable[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipeRef, _Mapping]]] = ..., balanced: bool = ..., maxSideKcalPercentage: _Optional[float] = ..., enableSides: bool = ..., maxSideFoods: _Optional[int] = ..., simplifiedSides: _Optional[_Iterable[_Union[SimplifiedSideFoodOption, _Mapping]]] = ...) -> None: ...

class SimplifiedSideFoodOption(_message.Message):
    __slots__ = ("concept", "minCount", "maxCount")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    MINCOUNT_FIELD_NUMBER: _ClassVar[int]
    MAXCOUNT_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    minCount: int
    maxCount: int
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., minCount: _Optional[int] = ..., maxCount: _Optional[int] = ...) -> None: ...

class MealRequirement(_message.Message):
    __slots__ = ("min", "max", "useMin", "useMax", "numerator", "denominator", "ratio", "scaleNumerator", "scaleDenominator", "numeratorConcepts", "denominatorConcepts")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    USEMIN_FIELD_NUMBER: _ClassVar[int]
    USEMAX_FIELD_NUMBER: _ClassVar[int]
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    RATIO_FIELD_NUMBER: _ClassVar[int]
    SCALENUMERATOR_FIELD_NUMBER: _ClassVar[int]
    SCALEDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    NUMERATORCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    DENOMINATORCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    useMin: bool
    useMax: bool
    numerator: _property_pb2.PropertyRef
    denominator: _property_pb2.PropertyRef
    ratio: bool
    scaleNumerator: float
    scaleDenominator: float
    numeratorConcepts: _concept_pb2.BoolConceptValues
    denominatorConcepts: _concept_pb2.BoolConceptValues
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., useMin: bool = ..., useMax: bool = ..., numerator: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., denominator: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., ratio: bool = ..., scaleNumerator: _Optional[float] = ..., scaleDenominator: _Optional[float] = ..., numeratorConcepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., denominatorConcepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ...) -> None: ...

class SmartRecipeAccuracyPreference(_message.Message):
    __slots__ = ("exact", "margin")
    EXACT_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    exact: bool
    margin: float
    def __init__(self, exact: bool = ..., margin: _Optional[float] = ...) -> None: ...

class SmartRecipePreferences(_message.Message):
    __slots__ = ("enabled", "categories", "cuisines", "minTime", "maxTime", "concepts", "accuracy", "minMealKcalPercentage", "qualityFilter", "maxFoods")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    MINTIME_FIELD_NUMBER: _ClassVar[int]
    MAXTIME_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    MINMEALKCALPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    QUALITYFILTER_FIELD_NUMBER: _ClassVar[int]
    MAXFOODS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    categories: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategoryRef]
    cuisines: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCuisineRef]
    minTime: int
    maxTime: int
    concepts: _concept_pb2.BoolConceptValues
    accuracy: SmartRecipeAccuracyPreference
    minMealKcalPercentage: float
    qualityFilter: _recipe_quality_pb2.RecipeQualityFilter
    maxFoods: int
    def __init__(self, enabled: bool = ..., categories: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCuisineRef, _Mapping]]] = ..., minTime: _Optional[int] = ..., maxTime: _Optional[int] = ..., concepts: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., accuracy: _Optional[_Union[SmartRecipeAccuracyPreference, _Mapping]] = ..., minMealKcalPercentage: _Optional[float] = ..., qualityFilter: _Optional[_Union[_recipe_quality_pb2.RecipeQualityFilter, _Mapping]] = ..., maxFoods: _Optional[int] = ...) -> None: ...

class MealQuery(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
