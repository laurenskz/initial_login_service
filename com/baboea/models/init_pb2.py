# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/models/init.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import objectivegroup_pb2 as com_dot_baboea_dot_models_dot_objectivegroup__pb2
from com.baboea.models import meal_pb2 as com_dot_baboea_dot_models_dot_meal__pb2
from com.baboea import concept_pb2 as com_dot_baboea_dot_concept__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63om/baboea/models/init.proto\x12\x11\x63om.baboea.models\x1a&com/baboea/models/objectivegroup.proto\x1a\x1c\x63om/baboea/models/meal.proto\x1a\x18\x63om/baboea/concept.proto\"r\n\x11\x41ppInitialization\x12&\n\x05meals\x18\x01 \x01(\x0b\x32\x17.com.baboea.models.Meal\x12\x35\n\nobjectives\x18\x02 \x03(\x0b\x32!.com.baboea.models.ObjectiveGroupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.models.init_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APPINITIALIZATION']._serialized_start=147
  _globals['_APPINITIALIZATION']._serialized_end=261
# @@protoc_insertion_point(module_scope)