from com.baboea.models import objectivegroup_pb2 as _objectivegroup_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import recipe_entropy_pb2 as _recipe_entropy_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea.services import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskClarificationOption(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AskClarification(_message.Message):
    __slots__ = ("dimension", "values", "userQuestion")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    USERQUESTION_FIELD_NUMBER: _ClassVar[int]
    dimension: _recipe_entropy_pb2.EntropicFeatureOrDimensionRef
    values: _containers.RepeatedCompositeFieldContainer[_recipe_entropy_pb2.EntropicValueRef]
    userQuestion: _localized_pb2.LocalizedString
    def __init__(self, dimension: _Optional[_Union[_recipe_entropy_pb2.EntropicFeatureOrDimensionRef, _Mapping]] = ..., values: _Optional[_Iterable[_Union[_recipe_entropy_pb2.EntropicValueRef, _Mapping]]] = ..., userQuestion: _Optional[_Union[_localized_pb2.LocalizedString, _Mapping]] = ...) -> None: ...

class RecommendedFoods(_message.Message):
    __slots__ = ("concepts",)
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    def __init__(self, concepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ...) -> None: ...

class SetCurrentRecipeTo(_message.Message):
    __slots__ = ("concepts",)
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.ConceptRef]
    def __init__(self, concepts: _Optional[_Iterable[_Union[_concepts_pb2.ConceptRef, _Mapping]]] = ...) -> None: ...

class ChooseEntropicDimension(_message.Message):
    __slots__ = ("dimension", "value")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    dimension: _recipe_entropy_pb2.EntropicFeatureOrDimensionRef
    value: _recipe_entropy_pb2.EntropicValueRef
    def __init__(self, dimension: _Optional[_Union[_recipe_entropy_pb2.EntropicFeatureOrDimensionRef, _Mapping]] = ..., value: _Optional[_Union[_recipe_entropy_pb2.EntropicValueRef, _Mapping]] = ...) -> None: ...

class BuildARecipeFinished(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _template_recipe_data_pb2.ImprovedTemplateRecipe
    def __init__(self, result: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipe, _Mapping]] = ...) -> None: ...

class InitializeQuestionFlow(_message.Message):
    __slots__ = ("maxResultingEntropy", "minSupport")
    MAXRESULTINGENTROPY_FIELD_NUMBER: _ClassVar[int]
    MINSUPPORT_FIELD_NUMBER: _ClassVar[int]
    maxResultingEntropy: float
    minSupport: float
    def __init__(self, maxResultingEntropy: _Optional[float] = ..., minSupport: _Optional[float] = ...) -> None: ...

class BuildARecipeRequest(_message.Message):
    __slots__ = ("setCurrent", "chooseDimension", "initializeQuestions")
    SETCURRENT_FIELD_NUMBER: _ClassVar[int]
    CHOOSEDIMENSION_FIELD_NUMBER: _ClassVar[int]
    INITIALIZEQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    setCurrent: SetCurrentRecipeTo
    chooseDimension: ChooseEntropicDimension
    initializeQuestions: InitializeQuestionFlow
    def __init__(self, setCurrent: _Optional[_Union[SetCurrentRecipeTo, _Mapping]] = ..., chooseDimension: _Optional[_Union[ChooseEntropicDimension, _Mapping]] = ..., initializeQuestions: _Optional[_Union[InitializeQuestionFlow, _Mapping]] = ...) -> None: ...

class BuildARecipeResponse(_message.Message):
    __slots__ = ("askClarification", "foods", "done")
    ASKCLARIFICATION_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    askClarification: AskClarification
    foods: RecommendedFoods
    done: BuildARecipeFinished
    def __init__(self, askClarification: _Optional[_Union[AskClarification, _Mapping]] = ..., foods: _Optional[_Union[RecommendedFoods, _Mapping]] = ..., done: _Optional[_Union[BuildARecipeFinished, _Mapping]] = ...) -> None: ...
