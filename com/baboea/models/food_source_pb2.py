# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/models/food_source.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import property_pb2 as com_dot_baboea_dot_models_dot_property__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.models import food_units_pb2 as com_dot_baboea_dot_models_dot_food__units__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#com/baboea/models/food_source.proto\x12\x11\x63om.baboea.models\x1a com/baboea/models/property.proto\x1a!com/baboea/models/localized.proto\x1a\"com/baboea/models/food_units.proto\"g\n\nFoodSource\x12\n\n\x02id\x18\x01 \x01(\t\x12=\n\rlocalizations\x18\x02 \x03(\x0b\x32&.com.baboea.models.FoodSourceLocalized\x12\x0e\n\x06handle\x18\x04 \x01(\t\"f\n\x13\x46oodSourceLocalized\x12,\n\x06locale\x18\x01 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"M\n\rFoodSourceRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x04name\x18\x02 \x01(\x0b\x32\".com.baboea.models.LocalizedStringb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.models.food_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FOODSOURCE']._serialized_start=163
  _globals['_FOODSOURCE']._serialized_end=266
  _globals['_FOODSOURCELOCALIZED']._serialized_start=268
  _globals['_FOODSOURCELOCALIZED']._serialized_end=370
  _globals['_FOODSOURCEREF']._serialized_start=372
  _globals['_FOODSOURCEREF']._serialized_end=449
# @@protoc_insertion_point(module_scope)