# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/baboea/services/base.proto
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
    'com/baboea/services/base.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63om/baboea/services/base.proto\x12\x13\x63om.baboea.services\")\n\x17\x46indSingleHandleRequest\x12\x0e\n\x06handle\x18\x01 \x01(\t\";\n\x11OperationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"K\n\x0eUpdateResponse\x12\x39\n\toperation\x18\x02 \x01(\x0b\x32&.com.baboea.services.OperationResponse\"\x1b\n\rRemoveRequest\x12\n\n\x02id\x18\x01 \x01(\t\"K\n\x0eRemoveResponse\x12\x39\n\toperation\x18\x02 \x01(\x0b\x32&.com.baboea.services.OperationResponse\",\n\rGetAllRequest\x12\x0c\n\x04page\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\"\x18\n\nGetRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x0e\n\x0c\x45mptyRequest\"\x1b\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\"T\n\x0b\x41\x64\x64Response\x12\n\n\x02id\x18\x01 \x01(\t\x12\x39\n\toperation\x18\x02 \x01(\x0b\x32&.com.baboea.services.OperationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.base_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FINDSINGLEHANDLEREQUEST']._serialized_start=55
  _globals['_FINDSINGLEHANDLEREQUEST']._serialized_end=96
  _globals['_OPERATIONRESPONSE']._serialized_start=98
  _globals['_OPERATIONRESPONSE']._serialized_end=157
  _globals['_UPDATERESPONSE']._serialized_start=159
  _globals['_UPDATERESPONSE']._serialized_end=234
  _globals['_REMOVEREQUEST']._serialized_start=236
  _globals['_REMOVEREQUEST']._serialized_end=263
  _globals['_REMOVERESPONSE']._serialized_start=265
  _globals['_REMOVERESPONSE']._serialized_end=340
  _globals['_GETALLREQUEST']._serialized_start=342
  _globals['_GETALLREQUEST']._serialized_end=386
  _globals['_GETREQUEST']._serialized_start=388
  _globals['_GETREQUEST']._serialized_end=412
  _globals['_EMPTYREQUEST']._serialized_start=414
  _globals['_EMPTYREQUEST']._serialized_end=428
  _globals['_UPDATEREQUEST']._serialized_start=430
  _globals['_UPDATEREQUEST']._serialized_end=457
  _globals['_ADDRESPONSE']._serialized_start=459
  _globals['_ADDRESPONSE']._serialized_end=543
# @@protoc_insertion_point(module_scope)
