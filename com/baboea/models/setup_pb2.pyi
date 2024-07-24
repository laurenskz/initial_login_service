from com.baboea.models import property_pb2 as _property_pb2
from com.baboea.models import localized_pb2 as _localized_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import food_units_pb2 as _food_units_pb2
from com.baboea.models import food_pb2 as _food_pb2
from com.baboea.models import concepts_pb2 as _concepts_pb2
from com.baboea.models import concept_impl_pb2 as _concept_impl_pb2
from com.baboea.services import scrape_service_pb2 as _scrape_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestData(_message.Message):
    __slots__ = ("concepts", "implementation", "foodUnits", "conversions", "foods", "categories", "cuisines", "locales", "properties", "scrapedPage")
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    FOODUNITS_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    FOODS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CUISINES_FIELD_NUMBER: _ClassVar[int]
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SCRAPEDPAGE_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[_concepts_pb2.Concept]
    implementation: _concept_impl_pb2.ConceptImplementation
    foodUnits: _containers.RepeatedCompositeFieldContainer[_food_units_pb2.FoodUnit]
    conversions: _containers.RepeatedCompositeFieldContainer[_food_units_pb2.Conversion]
    foods: _containers.RepeatedCompositeFieldContainer[_food_pb2.Food]
    categories: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCategory]
    cuisines: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.RecipeCuisine]
    locales: _containers.RepeatedCompositeFieldContainer[_localized_pb2.LocaleRef]
    properties: _containers.RepeatedCompositeFieldContainer[_property_pb2.Property]
    scrapedPage: _containers.RepeatedCompositeFieldContainer[_scrape_service_pb2.ScrapedPage]
    def __init__(self, concepts: _Optional[_Iterable[_Union[_concepts_pb2.Concept, _Mapping]]] = ..., implementation: _Optional[_Union[_concept_impl_pb2.ConceptImplementation, _Mapping]] = ..., foodUnits: _Optional[_Iterable[_Union[_food_units_pb2.FoodUnit, _Mapping]]] = ..., conversions: _Optional[_Iterable[_Union[_food_units_pb2.Conversion, _Mapping]]] = ..., foods: _Optional[_Iterable[_Union[_food_pb2.Food, _Mapping]]] = ..., categories: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCategory, _Mapping]]] = ..., cuisines: _Optional[_Iterable[_Union[_recipes_pb2.RecipeCuisine, _Mapping]]] = ..., locales: _Optional[_Iterable[_Union[_localized_pb2.LocaleRef, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_property_pb2.Property, _Mapping]]] = ..., scrapedPage: _Optional[_Iterable[_Union[_scrape_service_pb2.ScrapedPage, _Mapping]]] = ...) -> None: ...
