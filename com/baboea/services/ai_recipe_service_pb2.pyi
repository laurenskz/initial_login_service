from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AiRecipeGenerationRequest(_message.Message):
    __slots__ = ("recipeName", "user")
    RECIPENAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    recipeName: str
    user: _users_pb2.UserRef
    def __init__(self, recipeName: _Optional[str] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class AiRecipeGenerationResponse(_message.Message):
    __slots__ = ("recipe",)
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    recipe: _template_recipe_data_pb2.ImprovedTemplateRecipe
    def __init__(self, recipe: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipe, _Mapping]] = ...) -> None: ...
