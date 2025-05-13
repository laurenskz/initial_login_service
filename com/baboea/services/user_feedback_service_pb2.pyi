from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.services import template_recipe_service_pb2 as _template_recipe_service_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.models import users_pb2 as _users_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindConceptPathRequest(_message.Message):
    __slots__ = ("food", "locale")
    FOOD_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    locale: _localized_pb2.LocaleRef
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ..., locale: _Optional[_Union[_localized_pb2.LocaleRef, _Mapping]] = ...) -> None: ...

class FindConceptPathResponse(_message.Message):
    __slots__ = ("concepts",)
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    def __init__(self, concepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ...) -> None: ...

class NeverSuggestAgainRequest(_message.Message):
    __slots__ = ("concept", "user")
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    user: _users_pb2.UserRef
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class GiveRecipeFeedbackRequest(_message.Message):
    __slots__ = ("recipe", "user", "status")
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    recipe: _template_recipe_data_pb2.ImprovedTemplateRecipeRef
    user: _users_pb2.UserRef
    status: _template_recipe_service_pb2.TemplateRecipeLikeStatus
    def __init__(self, recipe: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipeRef, _Mapping]] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., status: _Optional[_Union[_template_recipe_service_pb2.TemplateRecipeLikeStatus, str]] = ...) -> None: ...
