from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import concept_impl_pb2 as _concept_impl_pb2
from com.baboea.models import food_units_pb2 as _food_units_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import matching_pb2 as _matching_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeParseSet(_message.Message):
    __slots__ = ("concept", "cuisine", "category", "units", "piecesUnit", "gramsUnit", "kcalProperty", "conceptImplementation", "conversionList", "version")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    CUISINE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    PIECESUNIT_FIELD_NUMBER: _ClassVar[int]
    GRAMSUNIT_FIELD_NUMBER: _ClassVar[int]
    KCALPROPERTY_FIELD_NUMBER: _ClassVar[int]
    CONCEPTIMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONLIST_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    concept: ConceptParseSet
    cuisine: RecipeCuisineParseSet
    category: RecipeCategoryParseSet
    units: FoodUnitParseSet
    piecesUnit: _food_units_pb2.FoodUnitRef
    gramsUnit: _food_units_pb2.FoodUnitRef
    kcalProperty: _property_pb2.PropertyRef
    conceptImplementation: _concept_impl_pb2.ConceptImplementationData
    conversionList: _food_units_pb2.ConversionList
    version: _recipes_pb2.RecipeBuildVersion
    def __init__(self, concept: _Optional[_Union[ConceptParseSet, _Mapping]] = ..., cuisine: _Optional[_Union[RecipeCuisineParseSet, _Mapping]] = ..., category: _Optional[_Union[RecipeCategoryParseSet, _Mapping]] = ..., units: _Optional[_Union[FoodUnitParseSet, _Mapping]] = ..., piecesUnit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ..., gramsUnit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ..., kcalProperty: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., conceptImplementation: _Optional[_Union[_concept_impl_pb2.ConceptImplementationData, _Mapping]] = ..., conversionList: _Optional[_Union[_food_units_pb2.ConversionList, _Mapping]] = ..., version: _Optional[_Union[_recipes_pb2.RecipeBuildVersion, _Mapping]] = ...) -> None: ...

class ConceptParseSet(_message.Message):
    __slots__ = ("sets",)
    SETS_FIELD_NUMBER: _ClassVar[int]
    sets: _containers.RepeatedCompositeFieldContainer[ConceptParseEntry]
    def __init__(self, sets: _Optional[_Iterable[_Union[ConceptParseEntry, _Mapping]]] = ...) -> None: ...

class ConceptParseEntry(_message.Message):
    __slots__ = ("concept", "matchset")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    MATCHSET_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    matchset: _matching_pb2.MatchSet
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., matchset: _Optional[_Union[_matching_pb2.MatchSet, _Mapping]] = ...) -> None: ...

class RecipeCuisineParseSet(_message.Message):
    __slots__ = ("sets",)
    SETS_FIELD_NUMBER: _ClassVar[int]
    sets: _containers.RepeatedCompositeFieldContainer[RecipeCuisineParseEntry]
    def __init__(self, sets: _Optional[_Iterable[_Union[RecipeCuisineParseEntry, _Mapping]]] = ...) -> None: ...

class RecipeCuisineParseEntry(_message.Message):
    __slots__ = ("cuisine", "matchset")
    CUISINE_FIELD_NUMBER: _ClassVar[int]
    MATCHSET_FIELD_NUMBER: _ClassVar[int]
    cuisine: _recipes_pb2.RecipeCuisineRef
    matchset: _matching_pb2.MatchSet
    def __init__(self, cuisine: _Optional[_Union[_recipes_pb2.RecipeCuisineRef, _Mapping]] = ..., matchset: _Optional[_Union[_matching_pb2.MatchSet, _Mapping]] = ...) -> None: ...

class RecipeCategoryParseSet(_message.Message):
    __slots__ = ("sets",)
    SETS_FIELD_NUMBER: _ClassVar[int]
    sets: _containers.RepeatedCompositeFieldContainer[RecipeCategoryParseEntry]
    def __init__(self, sets: _Optional[_Iterable[_Union[RecipeCategoryParseEntry, _Mapping]]] = ...) -> None: ...

class RecipeCategoryParseEntry(_message.Message):
    __slots__ = ("category", "matchset")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MATCHSET_FIELD_NUMBER: _ClassVar[int]
    category: _recipes_pb2.RecipeCategoryRef
    matchset: _matching_pb2.MatchSet
    def __init__(self, category: _Optional[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]] = ..., matchset: _Optional[_Union[_matching_pb2.MatchSet, _Mapping]] = ...) -> None: ...

class FoodUnitParseSet(_message.Message):
    __slots__ = ("sets",)
    SETS_FIELD_NUMBER: _ClassVar[int]
    sets: _containers.RepeatedCompositeFieldContainer[FoodUnitParseEntry]
    def __init__(self, sets: _Optional[_Iterable[_Union[FoodUnitParseEntry, _Mapping]]] = ...) -> None: ...

class FoodUnitParseEntry(_message.Message):
    __slots__ = ("unit", "matchset")
    UNIT_FIELD_NUMBER: _ClassVar[int]
    MATCHSET_FIELD_NUMBER: _ClassVar[int]
    unit: _food_units_pb2.FoodUnitRef
    matchset: _matching_pb2.MatchSet
    def __init__(self, unit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ..., matchset: _Optional[_Union[_matching_pb2.MatchSet, _Mapping]] = ...) -> None: ...

class PendingRemoteRecipe(_message.Message):
    __slots__ = ("minVersion", "remote", "localeId")
    MINVERSION_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    LOCALEID_FIELD_NUMBER: _ClassVar[int]
    minVersion: int
    remote: _recipes_pb2.RemoteRecipe
    localeId: str
    def __init__(self, minVersion: _Optional[int] = ..., remote: _Optional[_Union[_recipes_pb2.RemoteRecipe, _Mapping]] = ..., localeId: _Optional[str] = ...) -> None: ...

class RecipeToProcess(_message.Message):
    __slots__ = ("localeId", "minRecipeBuildVersion", "recipe")
    LOCALEID_FIELD_NUMBER: _ClassVar[int]
    MINRECIPEBUILDVERSION_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    localeId: str
    minRecipeBuildVersion: int
    recipe: _recipes_pb2.RemoteRecipe
    def __init__(self, localeId: _Optional[str] = ..., minRecipeBuildVersion: _Optional[int] = ..., recipe: _Optional[_Union[_recipes_pb2.RemoteRecipe, _Mapping]] = ...) -> None: ...

class RecipeVersionUpgradeRequest(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
