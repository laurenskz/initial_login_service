from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import culinary_groups_pb2 as _culinary_groups_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import flavour_recipe_pb2 as _flavour_recipe_pb2
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

class TemplateRecipePropertyBounds(_message.Message):
    __slots__ = ("property", "min", "max")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    property: _property_pb2.PropertyRef
    min: float
    max: float
    def __init__(self, property: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...

class ImprovedTemplateRecipe(_message.Message):
    __slots__ = ("id", "categories", "cuisines", "totalTimeMinutes", "isPublic", "isVerified", "owner", "emoji", "allowedScale", "groups", "localizations", "globalConstraints", "ratioConstraints", "propertyBounds")
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
    GLOBALCONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    RATIOCONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    PROPERTYBOUNDS_FIELD_NUMBER: _ClassVar[int]
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
    globalConstraints: _containers.RepeatedCompositeFieldContainer[_flavour_recipe_pb2.GlobalConstraint]
    ratioConstraints: _containers.RepeatedCompositeFieldContainer[_flavour_recipe_pb2.RatioConstraint]
    propertyBounds: _containers.RepeatedCompositeFieldContainer[TemplateRecipePropertyBounds]
    def __init__(self, id: _Optional[str] = ..., categories: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategoryRef, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCuisineRef, _Mapping]]] = ..., totalTimeMinutes: _Optional[int] = ..., isPublic: bool = ..., isVerified: bool = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., emoji: _Optional[str] = ..., allowedScale: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[TemplateRecipeIngredientGroup, _Mapping]]] = ..., localizations: _Optional[_Iterable[_Union[TemplateRecipeLocalized, _Mapping]]] = ..., globalConstraints: _Optional[_Iterable[_Union[_flavour_recipe_pb2.GlobalConstraint, _Mapping]]] = ..., ratioConstraints: _Optional[_Iterable[_Union[_flavour_recipe_pb2.RatioConstraint, _Mapping]]] = ..., propertyBounds: _Optional[_Iterable[_Union[TemplateRecipePropertyBounds, _Mapping]]] = ...) -> None: ...

class TemplateRecipeWithoutMetaData(_message.Message):
    __slots__ = ("groups", "globalConstraints", "ratioConstraints")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    GLOBALCONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    RATIOCONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[TemplateRecipeIngredientGroup]
    globalConstraints: _containers.RepeatedCompositeFieldContainer[_flavour_recipe_pb2.GlobalConstraint]
    ratioConstraints: _containers.RepeatedCompositeFieldContainer[_flavour_recipe_pb2.RatioConstraint]
    def __init__(self, groups: _Optional[_Iterable[_Union[TemplateRecipeIngredientGroup, _Mapping]]] = ..., globalConstraints: _Optional[_Iterable[_Union[_flavour_recipe_pb2.GlobalConstraint, _Mapping]]] = ..., ratioConstraints: _Optional[_Iterable[_Union[_flavour_recipe_pb2.RatioConstraint, _Mapping]]] = ...) -> None: ...

class TemplateRecipeIngredientGroup(_message.Message):
    __slots__ = ("culinaryGroup", "concepts", "groupId", "nameOverride")
    CULINARYGROUP_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    NAMEOVERRIDE_FIELD_NUMBER: _ClassVar[int]
    culinaryGroup: _culinary_groups_pb2.CulinaryGroupRef
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.QuantifiedConcept]
    groupId: str
    nameOverride: TemplateRecipeIngredientGroupNameOverride
    def __init__(self, culinaryGroup: _Optional[_Union[_culinary_groups_pb2.CulinaryGroupRef, _Mapping]] = ..., concepts: _Optional[_Iterable[_Union[_concepts_pb2.QuantifiedConcept, _Mapping]]] = ..., groupId: _Optional[str] = ..., nameOverride: _Optional[_Union[TemplateRecipeIngredientGroupNameOverride, _Mapping]] = ...) -> None: ...

class TemplateRecipeIngredientGroupNameOverride(_message.Message):
    __slots__ = ("name", "emoji")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    name: _localized_pb2.LocalizedString
    emoji: str
    def __init__(self, name: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ..., emoji: _Optional[str] = ...) -> None: ...
