from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import food_units_pb2 as _food_units_pb2
from com.baboea.models import objectivegroup_pb2 as _objectivegroup_pb2
from com.baboea.models import meal_components_pb2 as _meal_components_pb2
from com.baboea.models import plugins_pb2 as _plugins_pb2
from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import concept_impl_pb2 as _concept_impl_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MealPlanGenerateSet(_message.Message):
    __slots__ = ("foods", "concepts", "implementationNodes", "conversions", "gramsUnit", "properties", "kcalProp", "foodWeightProp", "foodCountProp", "recipeCountProp", "mealPlanApplication", "dayApplication", "mealApplication", "mealComponentApplication", "mealComponents", "recipes", "sides", "foodRefs", "plugins")
    FOODS_FIELD_NUMBER: _ClassVar[int]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATIONNODES_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    GRAMSUNIT_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    KCALPROP_FIELD_NUMBER: _ClassVar[int]
    FOODWEIGHTPROP_FIELD_NUMBER: _ClassVar[int]
    FOODCOUNTPROP_FIELD_NUMBER: _ClassVar[int]
    RECIPECOUNTPROP_FIELD_NUMBER: _ClassVar[int]
    MEALPLANAPPLICATION_FIELD_NUMBER: _ClassVar[int]
    DAYAPPLICATION_FIELD_NUMBER: _ClassVar[int]
    MEALAPPLICATION_FIELD_NUMBER: _ClassVar[int]
    MEALCOMPONENTAPPLICATION_FIELD_NUMBER: _ClassVar[int]
    MEALCOMPONENTS_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    SIDES_FIELD_NUMBER: _ClassVar[int]
    FOODREFS_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.Food]
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.Concept]
    implementationNodes: _containers.RepeatedCompositeFieldContainer[_concept_impl_pb2.ConceptImplementationNode]
    conversions: _food_units_pb2.ConversionList
    gramsUnit: _food_units_pb2.FoodUnitRef
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.PropertyRef]
    kcalProp: _property_pb2.PropertyRef
    foodWeightProp: _property_pb2.PropertyRef
    foodCountProp: _property_pb2.PropertyRef
    recipeCountProp: _property_pb2.PropertyRef
    mealPlanApplication: _objectivegroup_pb2.ApplicationLevelRef
    dayApplication: _objectivegroup_pb2.ApplicationLevelRef
    mealApplication: _objectivegroup_pb2.ApplicationLevelRef
    mealComponentApplication: _objectivegroup_pb2.ApplicationLevelRef
    mealComponents: _containers.RepeatedCompositeFieldContainer[_meal_components_pb2.MealComponentRef]
    recipes: _meal_components_pb2.MealComponentRef
    sides: _meal_components_pb2.MealComponentRef
    foodRefs: _containers.RepeatedCompositeFieldContainer[_food_pb2.FoodRef]
    plugins: _containers.RepeatedCompositeFieldContainer[_plugins_pb2.Plugin]
    def __init__(self, foods: _Optional[_Iterable[_Union[_food_pb2.Food, _Mapping]]] = ..., concepts: _Optional[_Iterable[_Union[_concepts_pb2.Concept, _Mapping]]] = ..., implementationNodes: _Optional[_Iterable[_Union[_concept_impl_pb2.ConceptImplementationNode, _Mapping]]] = ..., conversions: _Optional[_Union[_food_units_pb2.ConversionList, _Mapping]] = ..., gramsUnit: _Optional[_Union[_food_units_pb2.FoodUnitRef, _Mapping]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.PropertyRef, _Mapping]]] = ..., kcalProp: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., foodWeightProp: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., foodCountProp: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., recipeCountProp: _Optional[_Union[_property_pb2.PropertyRef, _Mapping]] = ..., mealPlanApplication: _Optional[_Union[_objectivegroup_pb2.ApplicationLevelRef, _Mapping]] = ..., dayApplication: _Optional[_Union[_objectivegroup_pb2.ApplicationLevelRef, _Mapping]] = ..., mealApplication: _Optional[_Union[_objectivegroup_pb2.ApplicationLevelRef, _Mapping]] = ..., mealComponentApplication: _Optional[_Union[_objectivegroup_pb2.ApplicationLevelRef, _Mapping]] = ..., mealComponents: _Optional[_Iterable[_Union[_meal_components_pb2.MealComponentRef, _Mapping]]] = ..., recipes: _Optional[_Union[_meal_components_pb2.MealComponentRef, _Mapping]] = ..., sides: _Optional[_Union[_meal_components_pb2.MealComponentRef, _Mapping]] = ..., foodRefs: _Optional[_Iterable[_Union[_food_pb2.FoodRef, _Mapping]]] = ..., plugins: _Optional[_Iterable[_Union[_plugins_pb2.Plugin, _Mapping]]] = ...) -> None: ...
