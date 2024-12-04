from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import users_pb2 as _users_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImprovedTemplateRecipeRef(_message.Message):
    __slots__ = ("id", "name", "emoji")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _localized_pb2.LocalizedString
    emoji: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., emoji: _Optional[str] = ...) -> None: ...

class TemplateRecipeLocalized(_message.Message):
    __slots__ = ("name", "description", "instructions", "locale")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    instructions: _containers.RepeatedScalarFieldContainer[str]
    locale: _localized_pb2.LocaleRef
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., instructions: _Optional[_Iterable[str]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...

class ImprovedTemplateRecipe(_message.Message):
    __slots__ = ("id", "categories", "cuisines", "totalTimeMinutes", "isPublic", "isVerified", "owner", "emoji", "allowedScale", "groups", "localizations")
    ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    TOTALTIMEMINUTES_FIELD_NUMBER: _ClassVar[int]
    ISPUBLIC_FIELD_NUMBER: _ClassVar[int]
    ISVERIFIED_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDSCALE_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    categories: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategoryRef]
    cuisines: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCuisineRef]
    totalTimeMinutes: int
    isPublic: bool
    isVerified: bool
    owner: _users_pb2.UserRef
    emoji: str
    allowedScale: float
    groups: _containers.RepeatedCompositeFieldContainer[TemplateRecipeIngredientGroup]
    localizations: _containers.RepeatedCompositeFieldContainer[TemplateRecipeLocalized]
    def __init__(self, id: _Optional[str] = ..., categories: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCuisineRef, _Mapping]]] = ..., totalTimeMinutes: _Optional[int] = ..., isPublic: bool = ..., isVerified: bool = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., emoji: _Optional[str] = ..., allowedScale: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[TemplateRecipeIngredientGroup, _Mapping]]] = ..., localizations: _Optional[_Iterable[_Union[TemplateRecipeLocalized, _Mapping]]] = ...) -> None: ...

class TemplateRecipeData(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TemplateRecipeIngredientGroup(_message.Message):
    __slots__ = ("optional", "options", "maxCountPerRecipe", "minCountPerRecipe", "noRepetition", "maxRepetitionsPerServing", "fixedMaxRepetitions")
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MAXCOUNTPERRECIPE_FIELD_NUMBER: _ClassVar[int]
    MINCOUNTPERRECIPE_FIELD_NUMBER: _ClassVar[int]
    NOREPETITION_FIELD_NUMBER: _ClassVar[int]
    MAXREPETITIONSPERSERVING_FIELD_NUMBER: _ClassVar[int]
    FIXEDMAXREPETITIONS_FIELD_NUMBER: _ClassVar[int]
    optional: bool
    options: _containers.RepeatedCompositeFieldContainer[TemplateRecipeIngredient]
    maxCountPerRecipe: float
    minCountPerRecipe: float
    noRepetition: bool
    maxRepetitionsPerServing: float
    fixedMaxRepetitions: float
    def __init__(self, optional: bool = ..., options: _Optional[_Iterable[_Union[TemplateRecipeIngredient, _Mapping]]] = ..., maxCountPerRecipe: _Optional[float] = ..., minCountPerRecipe: _Optional[float] = ..., noRepetition: bool = ..., maxRepetitionsPerServing: _Optional[float] = ..., fixedMaxRepetitions: _Optional[float] = ...) -> None: ...

class TemplateRecipeIngredient(_message.Message):
    __slots__ = ("food", "quantityMin", "quantityMax")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    QUANTITYMIN_FIELD_NUMBER: _ClassVar[int]
    QUANTITYMAX_FIELD_NUMBER: _ClassVar[int]
    food: _concepts_pb2.ConceptRef
    quantityMin: float
    quantityMax: float
    def __init__(self, food: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., quantityMin: _Optional[float] = ..., quantityMax: _Optional[float] = ...) -> None: ...