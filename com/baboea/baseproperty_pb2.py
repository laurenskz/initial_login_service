# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/baboea/baseproperty.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'com/baboea/baseproperty.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea import nutrient_pb2 as com_dot_baboea_dot_nutrient__pb2
from com.baboea import qualifier_pb2 as com_dot_baboea_dot_qualifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63om/baboea/baseproperty.proto\x12\ncom.baboea\x1a\x19\x63om/baboea/nutrient.proto\x1a\x1a\x63om/baboea/qualifier.proto*<\n\x0c\x42\x61seProperty\x12\x0e\n\nFOOD_COUNT\x10\x00\x12\n\n\x06WEIGHT\x10\x01\x12\x10\n\x0cRECIPE_COUNT\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.baseproperty_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BASEPROPERTY']._serialized_start=100
  _globals['_BASEPROPERTY']._serialized_end=160
# @@protoc_insertion_point(module_scope)
