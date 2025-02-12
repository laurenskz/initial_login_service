from com.baboea.models import recipes_pb2 as _recipes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SlimRecipeIngredient(_message.Message):
    __slots__ = ("conceptId", "gramQuantity")
    CONCEPTID_FIELD_NUMBER: _ClassVar[int]
    GRAMQUANTITY_FIELD_NUMBER: _ClassVar[int]
    conceptId: str
    gramQuantity: float
    def __init__(self, conceptId: _Optional[str] = ..., gramQuantity: _Optional[float] = ...) -> None: ...

class SlimRecipe(_message.Message):
    __slots__ = ("id", "ingredients", "entropyTags")
    ID_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    ENTROPYTAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ingredients: _containers.RepeatedCompositeFieldContainer[SlimRecipeIngredient]
    entropyTags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., ingredients: _Optional[_Iterable[_Union[SlimRecipeIngredient, _Mapping]]] = ..., entropyTags: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateTemplateFromRecipesRequest(_message.Message):
    __slots__ = ("recipes",)
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    recipes: _containers.RepeatedCompositeFieldContainer[SlimRecipe]
    def __init__(self, recipes: _Optional[_Iterable[_Union[SlimRecipe, _Mapping]]] = ...) -> None: ...

class GeneratedTemplateRecipeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
