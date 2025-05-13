from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import recipe_quality_pb2 as _recipe_quality_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import dates_pb2 as _dates_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_recipes_pb2.RecipeRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class RecipeUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _recipes_pb2.Recipe
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_recipes_pb2.Recipe, _Mapping]] = ...) -> None: ...

class RecipeRequest(_message.Message):
    __slots__ = ("page", "limit", "query")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    page: str
    limit: int
    query: _recipes_pb2.RecipeQuery
    def __init__(self, page: _Optional[str] = ..., limit: _Optional[int] = ..., query: _Optional[_Union[_recipes_pb2.RecipeQuery, _Mapping]] = ...) -> None: ...

class CategoryQuery(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CategoryRequest(_message.Message):
    __slots__ = ("page", "limit", "query")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    page: str
    limit: int
    query: CategoryQuery
    def __init__(self, page: _Optional[str] = ..., limit: _Optional[int] = ..., query: _Optional[_Union[CategoryQuery, _Mapping]] = ...) -> None: ...

class CategoryResponse(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategoryRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class DoubleRange(_message.Message):
    __slots__ = ("min", "max")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...

class SmartRecipesQuery(_message.Message):
    __slots__ = ("categories", "cuisines", "allowedConcepts", "requiredConcepts", "cookTimeMinutes", "prepTimeMinutes", "totalTimeMinutes", "smartRecipeCount", "ranges", "targetDate", "quality_filter", "maxFoods")
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    REQUIREDCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    COOKTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    PREPTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    TOTALTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    SMARTRECIPECOUNT_FIELD_NUMBER: _ClassVar[int]
    RANGES_FIELD_NUMBER: _ClassVar[int]
    TARGETDATE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAXFOODS_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategoryRef]
    cuisines: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCuisineRef]
    allowedConcepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    requiredConcepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    cookTimeMinutes: IntRange
    prepTimeMinutes: IntRange
    totalTimeMinutes: IntRange
    smartRecipeCount: int
    ranges: _containers.RepeatedCompositeFieldContainer[RequiredPropertyRange]
    targetDate: _dates_pb2.CalendarDate
    quality_filter: _recipe_quality_pb2.RecipeQualityFilter
    maxFoods: int
    def __init__(self, categories: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCuisineRef, _Mapping]]] = ..., allowedConcepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., requiredConcepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ..., cookTimeMinutes: _Optional[_Union[IntRange, _Mapping]] = ..., prepTimeMinutes: _Optional[_Union[IntRange, _Mapping]] = ..., totalTimeMinutes: _Optional[_Union[IntRange, _Mapping]] = ..., smartRecipeCount: _Optional[int] = ..., ranges: _Optional[_Iterable[_Union[RequiredPropertyRange, _Mapping]]] = ..., targetDate: _Optional[_Union[_dates_pb2.CalendarDate, _Mapping]] = ..., quality_filter: _Optional[_Union[_recipe_quality_pb2.RecipeQualityFilter, _Mapping]] = ..., maxFoods: _Optional[int] = ...) -> None: ...

class IntRange(_message.Message):
    __slots__ = ("min", "max")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...

class RequiredPropertyRange(_message.Message):
    __slots__ = ("property", "propertyRangePer100Kcal")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    PROPERTYRANGEPER100KCAL_FIELD_NUMBER: _ClassVar[int]
    property: _property_pb2.PropertyRef
    propertyRangePer100Kcal: DoubleRange
    def __init__(self, property: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., propertyRangePer100Kcal: _Optional[_Union[DoubleRange, _Mapping]] = ...) -> None: ...

class SmartRecipeEntry(_message.Message):
    __slots__ = ("recipe", "ingredients")
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    recipe: _recipes_pb2.ParsedRemoteRecipeRef
    ingredients: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RemoteRecipeIngredient]
    def __init__(self, recipe: _Optional[_Union[_recipes_pb2.ParsedRemoteRecipeRef, _Mapping]] = ..., ingredients: _Optional[_Iterable[_Union[_recipes_pb2.RemoteRecipeIngredient, _Mapping]]] = ...) -> None: ...

class SmartRecipesResponse(_message.Message):
    __slots__ = ("recipes",)
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    recipes: _containers.RepeatedCompositeFieldContainer[SmartRecipeEntry]
    def __init__(self, recipes: _Optional[_Iterable[_Union[SmartRecipeEntry, _Mapping]]] = ...) -> None: ...
