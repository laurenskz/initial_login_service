# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/application_level_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import objectivegroup_pb2 as com_dot_baboea_dot_models_dot_objectivegroup__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3com/baboea/services/application_level_service.proto\x12\x13\x63om.baboea.services\x1a&com/baboea/models/objectivegroup.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"d\n\x14\x41pplicationLevelList\x12\x35\n\x05items\x18\x01 \x03(\x0b\x32&.com.baboea.models.ApplicationLevelRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"b\n\x1d\x41pplicationLevelUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x35\n\x08newValue\x18\x02 \x01(\x0b\x32#.com.baboea.models.ApplicationLevel\"p\n\x15\x41pplicationLevelQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef2\x9d\x05\n\x17\x41pplicationLevelService\x12N\n\x03\x41\x64\x64\x12#.com.baboea.models.ApplicationLevel\x1a .com.baboea.services.AddResponse\"\x00\x12T\n\x06Remove\x12#.com.baboea.models.ApplicationLevel\x1a#.com.baboea.services.RemoveResponse\"\x00\x12Y\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a).com.baboea.services.ApplicationLevelList\"\x00\x12\x61\n\x06Search\x12*.com.baboea.services.ApplicationLevelQuery\x1a).com.baboea.services.ApplicationLevelList\"\x00\x12M\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a#.com.baboea.models.ApplicationLevel\"\x00\x12\x63\n\x06Update\x12\x32.com.baboea.services.ApplicationLevelUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x12j\n\x10\x42yHandleOrCreate\x12,.com.baboea.services.FindSingleHandleRequest\x1a&.com.baboea.models.ApplicationLevelRef\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.application_level_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APPLICATIONLEVELLIST']._serialized_start=183
  _globals['_APPLICATIONLEVELLIST']._serialized_end=283
  _globals['_APPLICATIONLEVELUPDATEREQUEST']._serialized_start=285
  _globals['_APPLICATIONLEVELUPDATEREQUEST']._serialized_end=383
  _globals['_APPLICATIONLEVELQUERY']._serialized_start=385
  _globals['_APPLICATIONLEVELQUERY']._serialized_end=497
  _globals['_APPLICATIONLEVELSERVICE']._serialized_start=500
  _globals['_APPLICATIONLEVELSERVICE']._serialized_end=1169
# @@protoc_insertion_point(module_scope)