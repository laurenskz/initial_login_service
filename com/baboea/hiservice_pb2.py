# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/baboea/hiservice.proto
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
    'com/baboea/hiservice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63om/baboea/hiservice.proto\")\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x62\x61\x62\x18\x02 \x01(\x05\".\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x32\x35\n\tHiService\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.hiservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLOREQUEST']._serialized_start=30
  _globals['_HELLOREQUEST']._serialized_end=71
  _globals['_HELLOREPLY']._serialized_start=73
  _globals['_HELLOREPLY']._serialized_end=119
  _globals['_HISERVICE']._serialized_start=121
  _globals['_HISERVICE']._serialized_end=174
# @@protoc_insertion_point(module_scope)
