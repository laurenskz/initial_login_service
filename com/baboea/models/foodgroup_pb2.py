# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/models/foodgroup.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import food_pb2 as com_dot_baboea_dot_models_dot_food__pb2
from com.baboea import concept_pb2 as com_dot_baboea_dot_concept__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!com/baboea/models/foodgroup.proto\x12\x11\x63om.baboea.models\x1a\x1c\x63om/baboea/models/food.proto\x1a\x18\x63om/baboea/concept.proto\"=\n\x0c\x46oodGroupRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\x96\x01\n\tFoodGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12)\n\x05\x66oods\x18\x03 \x03(\x0b\x32\x1a.com.baboea.models.FoodRef\x12/\n\x08\x63oncepts\x18\x04 \x01(\x0b\x32\x1d.com.baboea.BoolConceptValues\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"\x1e\n\x0e\x46oodGroupQuery\x12\x0c\n\x04name\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.models.foodgroup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FOODGROUPREF']._serialized_start=112
  _globals['_FOODGROUPREF']._serialized_end=173
  _globals['_FOODGROUP']._serialized_start=176
  _globals['_FOODGROUP']._serialized_end=326
  _globals['_FOODGROUPQUERY']._serialized_start=328
  _globals['_FOODGROUPQUERY']._serialized_end=358
# @@protoc_insertion_point(module_scope)