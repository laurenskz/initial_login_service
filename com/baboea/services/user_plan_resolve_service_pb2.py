# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/user_plan_resolve_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import days_pb2 as com_dot_baboea_dot_models_dot_days__pb2
from com.baboea.models import users_pb2 as com_dot_baboea_dot_models_dot_users__pb2
from com.baboea import generaterequest_pb2 as com_dot_baboea_dot_generaterequest__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3com/baboea/services/user_plan_resolve_service.proto\x12\x13\x63om.baboea.services\x1a\x1c\x63om/baboea/models/days.proto\x1a\x1d\x63om/baboea/models/users.proto\x1a com/baboea/generaterequest.proto2_\n\x10GenerateResolver\x12K\n\x07Resolve\x12\x19.com.baboea.UserPlanInput\x1a#.com.baboea.MealPlanGenerateRequest\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.user_plan_resolve_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GENERATERESOLVER']._serialized_start=171
  _globals['_GENERATERESOLVER']._serialized_end=266
# @@protoc_insertion_point(module_scope)