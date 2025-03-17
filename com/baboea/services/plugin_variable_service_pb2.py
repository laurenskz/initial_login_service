# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/baboea/services/plugin_variable_service.proto
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
    'com/baboea/services/plugin_variable_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import plugins_pb2 as com_dot_baboea_dot_models_dot_plugins__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1com/baboea/services/plugin_variable_service.proto\x12\x13\x63om.baboea.services\x1a\x1f\x63om/baboea/models/plugins.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"`\n\x12PluginVariableList\x12\x33\n\x05items\x18\x01 \x03(\x0b\x32$.com.baboea.models.PluginVariableRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"^\n\x1bPluginVariableUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x33\n\x08newValue\x18\x02 \x01(\x0b\x32!.com.baboea.models.PluginVariable\"n\n\x13PluginVariableQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef2\xa1\x04\n\x15PluginVariableService\x12L\n\x03\x41\x64\x64\x12!.com.baboea.models.PluginVariable\x1a .com.baboea.services.AddResponse\"\x00\x12R\n\x06Remove\x12!.com.baboea.models.PluginVariable\x1a#.com.baboea.services.RemoveResponse\"\x00\x12W\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a\'.com.baboea.services.PluginVariableList\"\x00\x12]\n\x06Search\x12(.com.baboea.services.PluginVariableQuery\x1a\'.com.baboea.services.PluginVariableList\"\x00\x12K\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a!.com.baboea.models.PluginVariable\"\x00\x12\x61\n\x06Update\x12\x30.com.baboea.services.PluginVariableUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.plugin_variable_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PLUGINVARIABLELIST']._serialized_start=174
  _globals['_PLUGINVARIABLELIST']._serialized_end=270
  _globals['_PLUGINVARIABLEUPDATEREQUEST']._serialized_start=272
  _globals['_PLUGINVARIABLEUPDATEREQUEST']._serialized_end=366
  _globals['_PLUGINVARIABLEQUERY']._serialized_start=368
  _globals['_PLUGINVARIABLEQUERY']._serialized_end=478
  _globals['_PLUGINVARIABLESERVICE']._serialized_start=481
  _globals['_PLUGINVARIABLESERVICE']._serialized_end=1026
# @@protoc_insertion_point(module_scope)
