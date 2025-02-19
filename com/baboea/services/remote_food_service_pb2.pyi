from com.baboea.models import objectivegroup_pb2 as _objectivegroup_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import users_pb2 as _users_pb2
from com.baboea.models import recipe_entropy_pb2 as _recipe_entropy_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendEan(_message.Message):
    __slots__ = ("ean", "user")
    EAN_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ean: str
    user: _users_pb2.UserRef
    def __init__(self, ean: _Optional[str] = ..., user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ...) -> None: ...

class PresentConcepts(_message.Message):
    __slots__ = ("concepts",)
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    def __init__(self, concepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ...) -> None: ...

class ChooseConceptRequest(_message.Message):
    __slots__ = ("concept",)
    CONCEPT_FIELD_NUMBER: _ClassVar[int]
    concept: _concepts_pb2.ConceptRef
    def __init__(self, concept: _Optional[_Union[_concepts_pb2.ConceptRef, _Mapping]] = ...) -> None: ...

class FoodDataInaccurate(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AddFoodComplete(_message.Message):
    __slots__ = ("food",)
    FOOD_FIELD_NUMBER: _ClassVar[int]
    food: _food_pb2.FoodRef
    def __init__(self, food: _Optional[_Union[_food_pb2.FoodRef, _Mapping]] = ...) -> None: ...

class AddRemoteFoodRequest(_message.Message):
    __slots__ = ("sendEan", "choose")
    SENDEAN_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_FIELD_NUMBER: _ClassVar[int]
    sendEan: SendEan
    choose: ChooseConceptRequest
    def __init__(self, sendEan: _Optional[_Union[SendEan, _Mapping]] = ..., choose: _Optional[_Union[ChooseConceptRequest, _Mapping]] = ...) -> None: ...

class AddRemoteFoodResponse(_message.Message):
    __slots__ = ("presentConcepts", "complete", "inaccurate")
    PRESENTCONCEPTS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    INACCURATE_FIELD_NUMBER: _ClassVar[int]
    presentConcepts: PresentConcepts
    complete: AddFoodComplete
    inaccurate: FoodDataInaccurate
    def __init__(self, presentConcepts: _Optional[_Union[PresentConcepts, _Mapping]] = ..., complete: _Optional[_Union[AddFoodComplete, _Mapping]] = ..., inaccurate: _Optional[_Union[FoodDataInaccurate, _Mapping]] = ...) -> None: ...
