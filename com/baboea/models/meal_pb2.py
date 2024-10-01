# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/models/meal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import recipes_pb2 as com_dot_baboea_dot_models_dot_recipes__pb2
from com.baboea.models import foodgroup_pb2 as com_dot_baboea_dot_models_dot_foodgroup__pb2
from com.baboea.models import users_pb2 as com_dot_baboea_dot_models_dot_users__pb2
from com.baboea.models import property_pb2 as com_dot_baboea_dot_models_dot_property__pb2
from com.baboea import concept_pb2 as com_dot_baboea_dot_concept__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63om/baboea/models/meal.proto\x12\x11\x63om.baboea.models\x1a\x1f\x63om/baboea/models/recipes.proto\x1a!com/baboea/models/foodgroup.proto\x1a\x1d\x63om/baboea/models/users.proto\x1a com/baboea/models/property.proto\x1a\x18\x63om/baboea/concept.proto\"#\n\x07MealRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x93\x02\n\x04Meal\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12)\n\x05owner\x18\x04 \x01(\x0b\x32\x1a.com.baboea.models.UserRef\x12?\n\x0csmartRecipes\x18\x07 \x01(\x0b\x32).com.baboea.models.SmartRecipePreferences\x12/\n\x08\x63oncepts\x18\x08 \x01(\x0b\x32\x1d.com.baboea.BoolConceptValues\x12-\n\x07recipes\x18\t \x03(\x0b\x32\x1c.com.baboea.models.RecipeRef\x12\x10\n\x08\x62\x61lanced\x18\n \x01(\x08\"\xff\x02\n\x0fMealRequirement\x12\x0b\n\x03min\x18\x03 \x01(\x01\x12\x0b\n\x03max\x18\x04 \x01(\x01\x12\x0e\n\x06useMin\x18\x05 \x01(\x08\x12\x0e\n\x06useMax\x18\x06 \x01(\x08\x12\x31\n\tnumerator\x18\x07 \x01(\x0b\x32\x1e.com.baboea.models.PropertyRef\x12\x38\n\x0b\x64\x65nominator\x18\x08 \x01(\x0b\x32\x1e.com.baboea.models.PropertyRefH\x00\x88\x01\x01\x12\r\n\x05ratio\x18\t \x01(\x08\x12\x16\n\x0escaleNumerator\x18\x0e \x01(\x01\x12\x18\n\x10scaleDenominator\x18\x0f \x01(\x01\x12\x38\n\x11numeratorConcepts\x18\x10 \x01(\x0b\x32\x1d.com.baboea.BoolConceptValues\x12:\n\x13\x64\x65nominatorConcepts\x18\x11 \x01(\x0b\x32\x1d.com.baboea.BoolConceptValuesB\x0e\n\x0c_denominator\"N\n\x1dSmartRecipeAccuracyPreference\x12\x0f\n\x05\x65xact\x18\x01 \x01(\x08H\x00\x12\x10\n\x06margin\x18\x02 \x01(\x01H\x00\x42\n\n\x08\x61\x63\x63uracy\"\xb1\x02\n\x16SmartRecipePreferences\x12\x0f\n\x07\x65nabled\x18\x07 \x01(\x08\x12\x38\n\ncategories\x18\x01 \x03(\x0b\x32$.com.baboea.models.RecipeCategoryRef\x12\x35\n\x08\x63uisines\x18\x06 \x03(\x0b\x32#.com.baboea.models.RecipeCuisineRef\x12\x0f\n\x07minTime\x18\x02 \x01(\x05\x12\x0f\n\x07maxTime\x18\x03 \x01(\x05\x12/\n\x08\x63oncepts\x18\x04 \x01(\x0b\x32\x1d.com.baboea.BoolConceptValues\x12\x42\n\x08\x61\x63\x63uracy\x18\x05 \x01(\x0b\x32\x30.com.baboea.models.SmartRecipeAccuracyPreference\"\x19\n\tMealQuery\x12\x0c\n\x04name\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.models.meal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MEALREF']._serialized_start=210
  _globals['_MEALREF']._serialized_end=245
  _globals['_MEAL']._serialized_start=248
  _globals['_MEAL']._serialized_end=523
  _globals['_MEALREQUIREMENT']._serialized_start=526
  _globals['_MEALREQUIREMENT']._serialized_end=909
  _globals['_SMARTRECIPEACCURACYPREFERENCE']._serialized_start=911
  _globals['_SMARTRECIPEACCURACYPREFERENCE']._serialized_end=989
  _globals['_SMARTRECIPEPREFERENCES']._serialized_start=992
  _globals['_SMARTRECIPEPREFERENCES']._serialized_end=1297
  _globals['_MEALQUERY']._serialized_start=1299
  _globals['_MEALQUERY']._serialized_end=1324
# @@protoc_insertion_point(module_scope)
