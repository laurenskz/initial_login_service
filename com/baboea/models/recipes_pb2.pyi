from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import food_units_pb2 as _food_units_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import matching_pb2 as _matching_pb2
from com.baboea.models import property_pb2 as _property_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RecipeQuery(_message.Message):
    __slots__ = ("name", "page", "limit", "owner")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    owner: _users_pb2.UserRef
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class Recipe(_message.Message):
    __slots__ = ("id", "name", "description", "requiredTime", "instructions", "categories", "cuisines", "owner", "public", "quantified")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIREDTIME_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    QUANTIFIED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    requiredTime: int
    instructions: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedCompositeFieldContainer[RecipeCategoryRef]
    cuisines: _containers.RepeatedCompositeFieldContainer[RecipeCuisineRef]
    owner: _users_pb2.UserRef
    public: bool
    quantified: QuantifiedRecipe
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., requiredTime: _Optional[int] = ..., instructions: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[_Union[RecipeCategoryRef, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[RecipeCuisineRef, _Mapping]]] = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., public: bool = ..., quantified: _Optional[_Union[QuantifiedRecipe, _Mapping]] = ...) -> None: ...

class UnmatchedConcept(_message.Message):
    __slots__ = ("concept_id", "unit")
    CONCEPT_ID_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    concept_id: str
    unit: _food_units_pb2.FoodUnits
    def __init__(self, concept_id: _Optional[str] = ..., unit: _Optional[_Union[_food_units_pb2.FoodUnits, str]] = ...) -> None: ...

class ConceptWeightRatio(_message.Message):
    __slots__ = ("conceptId", "weightPercentage")
    CONCEPTID_FIELD_NUMBER: _ClassVar[int]
    WEIGHTPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    conceptId: str
    weightPercentage: float
    def __init__(self, conceptId: _Optional[str] = ..., weightPercentage: _Optional[float] = ...) -> None: ...

class RemoteRecipeMetaData(_message.Message):
    __slots__ = ("proteinPerKcal", "fatPerKcal", "netCarbsPerKcal", "fiberPerKcal", "maxCompletionRatio", "unmatched", "weights")
    PROTEINPERKCAL_FIELD_NUMBER: _ClassVar[int]
    FATPERKCAL_FIELD_NUMBER: _ClassVar[int]
    NETCARBSPERKCAL_FIELD_NUMBER: _ClassVar[int]
    FIBERPERKCAL_FIELD_NUMBER: _ClassVar[int]
    MAXCOMPLETIONRATIO_FIELD_NUMBER: _ClassVar[int]
    UNMATCHED_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    proteinPerKcal: float
    fatPerKcal: float
    netCarbsPerKcal: float
    fiberPerKcal: float
    maxCompletionRatio: float
    unmatched: _containers.RepeatedCompositeFieldContainer[UnmatchedConcept]
    weights: _containers.RepeatedCompositeFieldContainer[ConceptWeightRatio]
    def __init__(self, proteinPerKcal: _Optional[float] = ..., fatPerKcal: _Optional[float] = ..., netCarbsPerKcal: _Optional[float] = ..., fiberPerKcal: _Optional[float] = ..., maxCompletionRatio: _Optional[float] = ..., unmatched: _Optional[_Iterable[_Union[UnmatchedConcept, _Mapping]]] = ..., weights: _Optional[_Iterable[_Union[ConceptWeightRatio, _Mapping]]] = ...) -> None: ...

class RemoteRecipeData(_message.Message):
    __slots__ = ("sourceDomain", "imageUrl", "sourceUrl", "concepts")
    SOURCEDOMAIN_FIELD_NUMBER: _ClassVar[int]
    IMAGEURL_FIELD_NUMBER: _ClassVar[int]
    SOURCEURL_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    sourceDomain: str
    imageUrl: str
    sourceUrl: str
    concepts: _containers.RepeatedCompositeFieldContainer[RemoteRecipeIngredient]
    def __init__(self, sourceDomain: _Optional[str] = ..., imageUrl: _Optional[str] = ..., sourceUrl: _Optional[str] = ..., concepts: _Optional[_Iterable[_Union[RemoteRecipeIngredient, _Mapping]]] = ...) -> None: ...

class RecipeCategory(_message.Message):
    __slots__ = ("id", "localizations", "matchSets")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    MATCHSETS_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[RecipeCategoryLocalized]
    matchSets: _containers.RepeatedCompositeFieldContainer[_matching_pb2.MatchSet]
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[RecipeCategoryLocalized, _Mapping]]] = ..., matchSets: _Optional[_Iterable[_Union[_matching_pb2.MatchSet, _Mapping]]] = ...) -> None: ...

class RecipeCategoryLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class RecipeCuisine(_message.Message):
    __slots__ = ("id", "localizations", "matchSets")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    MATCHSETS_FIELD_NUMBER: _ClassVar[int]
    id: str
    localizations: _containers.RepeatedCompositeFieldContainer[RecipeCuisineLocalized]
    matchSets: _containers.RepeatedCompositeFieldContainer[_matching_pb2.MatchSet]
    def __init__(self, id: _Optional[str] = ..., localizations: _Optional[_Iterable[_Union[RecipeCuisineLocalized, _Mapping]]] = ..., matchSets: _Optional[_Iterable[_Union[_matching_pb2.MatchSet, _Mapping]]] = ...) -> None: ...

class RecipeCuisineLocalized(_message.Message):
    __slots__ = ("locale", "name", "description")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class RecipeCategoryRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class RecipeCuisineRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class TemplateRecipe(_message.Message):
    __slots__ = ("simpleFoods", "compositeFoods")
    SIMPLEFOODS_FIELD_NUMBER: _ClassVar[int]
    COMPOSITEFOODS_FIELD_NUMBER: _ClassVar[int]
    simpleFoods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    compositeFoods: _containers.RepeatedCompositeFieldContainer[CompositeFood]
    def __init__(self, simpleFoods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ..., compositeFoods: _Optional[_Iterable[_Union[CompositeFood, _Mapping]]] = ...) -> None: ...

class QuantifiedRecipeIngredient(_message.Message):
    __slots__ = ("food", "quantity")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    quantity: float
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., quantity: _Optional[float] = ...) -> None: ...

class QuantifiedRecipe(_message.Message):
    __slots__ = ("ingredients", "min", "max", "margin")
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    ingredients: _containers.RepeatedCompositeFieldContainer[QuantifiedRecipeIngredient]
    min: float
    max: float
    margin: float
    def __init__(self, ingredients: _Optional[_Iterable[_Union[QuantifiedRecipeIngredient, _Mapping]]] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., margin: _Optional[float] = ...) -> None: ...

class CompositeFood(_message.Message):
    __slots__ = ("foods", "min", "max")
    FOODS_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    min: int
    max: int
    def __init__(self, foods: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ..., min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...

class RemoteRecipeIngredient(_message.Message):
    __slots__ = ("concept", "unit", "quantity", "originalFood")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORIGINALFOOD_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    unit: _food_units_pb2.FoodUnitRef
    quantity: float
    originalFood: str
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., unit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ..., quantity: _Optional[float] = ..., originalFood: _Optional[str] = ...) -> None: ...

class ConceptWeightInformation(_message.Message):
    __slots__ = ("concept", "foundMatchingIngredient", "ratioOfRecipe")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    FOUNDMATCHINGINGREDIENT_FIELD_NUMBER: _ClassVar[int]
    RATIOOFRECIPE_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    foundMatchingIngredient: bool
    ratioOfRecipe: float
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., foundMatchingIngredient: bool = ..., ratioOfRecipe: _Optional[float] = ...) -> None: ...

class RecipeBuildVersion(_message.Message):
    __slots__ = ("versionId", "version", "name", "description")
    VERSIONID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    versionId: str
    version: int
    name: str
    description: str
    def __init__(self, versionId: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ParsedRemoteRecipeRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class ParsedRemoteRecipe(_message.Message):
    __slots__ = ("id", "remoteRecipeId", "foods", "localizations", "categories", "cuisines", "prepTimeMinutes", "cookTimeMinutes", "totalTimeMinutes", "unmatched", "servings", "version", "propertiesPer100Kcal", "kcalPerServing", "conceptWeights", "remote")
    ID_FIELD_NUMBER: _ClassVar[int]
    REMOTERECIPEID_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    PREPTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    COOKTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    TOTALTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    UNMATCHED_FIELD_NUMBER: _ClassVar[int]
    SERVINGS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIESPER100KCAL_FIELD_NUMBER: _ClassVar[int]
    KCALPERSERVING_FIELD_NUMBER: _ClassVar[int]
    CONCEPTWEIGHTS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    remoteRecipeId: str
    foods: _containers.RepeatedCompositeFieldContainer[RemoteRecipeIngredient]
    localizations: _containers.RepeatedCompositeFieldContainer[ParsedRemoteRecipeLocalized]
    categories: _containers.RepeatedCompositeFieldContainer[RecipeCategoryRef]
    cuisines: _containers.RepeatedCompositeFieldContainer[RecipeCuisineRef]
    prepTimeMinutes: int
    cookTimeMinutes: int
    totalTimeMinutes: int
    unmatched: _containers.RepeatedCompositeFieldContainer[UnmatchedIngredient]
    servings: float
    version: RecipeBuildVersion
    propertiesPer100Kcal: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyValue]
    kcalPerServing: float
    conceptWeights: _containers.RepeatedCompositeFieldContainer[ConceptWeightInformation]
    remote: RemoteRecipeRef
    def __init__(self, id: _Optional[str] = ..., remoteRecipeId: _Optional[str] = ..., foods: _Optional[_Iterable[_Union[RemoteRecipeIngredient, _Mapping]]] = ..., localizations: _Optional[_Iterable[_Union[ParsedRemoteRecipeLocalized, _Mapping]]] = ..., categories: _Optional[_Iterable[_Union[RecipeCategoryRef, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[RecipeCuisineRef, _Mapping]]] = ..., prepTimeMinutes: _Optional[int] = ..., cookTimeMinutes: _Optional[int] = ..., totalTimeMinutes: _Optional[int] = ..., unmatched: _Optional[_Iterable[_Union[UnmatchedIngredient, _Mapping]]] = ..., servings: _Optional[float] = ..., version: _Optional[_Union[RecipeBuildVersion, _Mapping]] = ..., propertiesPer100Kcal: _Optional[_Iterable[_Union[_property_pb2.PropertyValue, _Mapping]]] = ..., kcalPerServing: _Optional[float] = ..., conceptWeights: _Optional[_Iterable[_Union[ConceptWeightInformation, _Mapping]]] = ..., remote: _Optional[_Union[RemoteRecipeRef, _Mapping]] = ...) -> None: ...

class ParsedRemoteRecipeLocalized(_message.Message):
    __slots__ = ("locale", "name", "description", "instructions")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    locale: _localized_pb2.LocaleRef
    name: str
    description: str
    instructions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., instructions: _Optional[_Iterable[str]] = ...) -> None: ...

class RemoteRecipe(_message.Message):
    __slots__ = ("id", "foods", "name", "description", "instructions", "categories", "url", "sourceDomain", "imageUrl", "prepTimeMinutes", "cookTimeMinutes", "totalTimeMinutes", "cuisines", "servings")
    ID_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SOURCEDOMAIN_FIELD_NUMBER: _ClassVar[int]
    IMAGEURL_FIELD_NUMBER: _ClassVar[int]
    PREPTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    COOKTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    TOTALTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    SERVINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    foods: _containers.RepeatedScalarFieldContainer[str]
    name: str
    description: str
    instructions: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    url: str
    sourceDomain: str
    imageUrl: str
    prepTimeMinutes: int
    cookTimeMinutes: int
    totalTimeMinutes: int
    cuisines: _containers.RepeatedScalarFieldContainer[str]
    servings: float
    def __init__(self, id: _Optional[str] = ..., foods: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., instructions: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., url: _Optional[str] = ..., sourceDomain: _Optional[str] = ..., imageUrl: _Optional[str] = ..., prepTimeMinutes: _Optional[int] = ..., cookTimeMinutes: _Optional[int] = ..., totalTimeMinutes: _Optional[int] = ..., cuisines: _Optional[_Iterable[str]] = ..., servings: _Optional[float] = ...) -> None: ...

class RemoteRecipeRef(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UnmatchedIngredient(_message.Message):
    __slots__ = ("originalFood", "unitFound", "conceptFound")
    ORIGINALFOOD_FIELD_NUMBER: _ClassVar[int]
    UNITFOUND_FIELD_NUMBER: _ClassVar[int]
    CONCEPTFOUND_FIELD_NUMBER: _ClassVar[int]
    originalFood: str
    unitFound: bool
    conceptFound: bool
    def __init__(self, originalFood: _Optional[str] = ..., unitFound: bool = ..., conceptFound: bool = ...) -> None: ...

class RemoteRecipeList(_message.Message):
    __slots__ = ("recipes", "parsedUrls")
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    PARSEDURLS_FIELD_NUMBER: _ClassVar[int]
    recipes: _containers.RepeatedCompositeFieldContainer[RemoteRecipe]
    parsedUrls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, recipes: _Optional[_Iterable[_Union[RemoteRecipe, _Mapping]]] = ..., parsedUrls: _Optional[_Iterable[str]] = ...) -> None: ...
