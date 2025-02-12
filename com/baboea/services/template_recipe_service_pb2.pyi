from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.services import recipe_service_pb2 as _recipe_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImprovedTemplateRecipeList(_message.Message):
    __slots__ = ("items", "nextPageToken")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_template_recipe_data_pb2.ImprovedTemplateRecipeRef]
    nextPageToken: str
    def __init__(self, items: _Optional[_Iterable[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipeRef, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class ImprovedTemplateRecipeUpdateRequest(_message.Message):
    __slots__ = ("id", "newValue")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEWVALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    newValue: _template_recipe_data_pb2.ImprovedTemplateRecipe
    def __init__(self, id: _Optional[str] = ..., newValue: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipe, _Mapping]] = ...) -> None: ...

class ImprovedTemplateRecipeQuery(_message.Message):
    __slots__ = ("name", "page", "limit", "locale", "alsoPublic", "owner")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ALSOPUBLIC_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    name: str
    page: str
    limit: int
    locale: _localized_pb2.LocaleRef
    alsoPublic: bool
    owner: _users_pb2.UserRef
    def __init__(self, name: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[int] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ..., alsoPublic: bool = ..., owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class SmartTemplateRecipeEntry(_message.Message):
    __slots__ = ("item", "data")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    item: _template_recipe_data_pb2.ImprovedTemplateRecipeRef
    data: _template_recipe_data_pb2.TemplateRecipeWithoutMetaData
    def __init__(self, item: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipeRef, _Mapping]] = ..., data: _Optional[_Union[_template_recipe_data_pb2.TemplateRecipeWithoutMetaData, _Mapping]] = ...) -> None: ...

class SmartTemplateRecipeResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SmartTemplateRecipeEntry]
    def __init__(self, items: _Optional[_Iterable[_Union[SmartTemplateRecipeEntry, _Mapping]]] = ...) -> None: ...

class SmartTemplateRecipeQuery(_message.Message):
    __slots__ = ("owner", "smartQuery")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SMARTQUERY_FIELD_NUMBER: _ClassVar[int]
    owner: _users_pb2.UserRef
    smartQuery: _recipe_service_pb2.SmartRecipesQuery
    def __init__(self, owner: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., smartQuery: _Optional[_Union[_recipe_service_pb2.SmartRecipesQuery, _Mapping]] = ...) -> None: ...
