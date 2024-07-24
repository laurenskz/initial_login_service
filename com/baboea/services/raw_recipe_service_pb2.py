# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/raw_recipe_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import recipes_pb2 as com_dot_baboea_dot_models_dot_recipes__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,com/baboea/services/raw_recipe_service.proto\x12\x13\x63om.baboea.services\x1a\x1f\x63om/baboea/models/recipes.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"\\\n\x10RemoteRecipeList\x12\x31\n\x05items\x18\x01 \x03(\x0b\x32\".com.baboea.models.RemoteRecipeRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"Z\n\x19RemoteRecipeUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x31\n\x08newValue\x18\x02 \x01(\x0b\x32\x1f.com.baboea.models.RemoteRecipe\"l\n\x11RemoteRecipeQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef2\x91\x04\n\x13RemoteRecipeService\x12J\n\x03\x41\x64\x64\x12\x1f.com.baboea.models.RemoteRecipe\x1a .com.baboea.services.AddResponse\"\x00\x12P\n\x06Remove\x12\x1f.com.baboea.models.RemoteRecipe\x1a#.com.baboea.services.RemoveResponse\"\x00\x12U\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a%.com.baboea.services.RemoteRecipeList\"\x00\x12Y\n\x06Search\x12&.com.baboea.services.RemoteRecipeQuery\x1a%.com.baboea.services.RemoteRecipeList\"\x00\x12I\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a\x1f.com.baboea.models.RemoteRecipe\"\x00\x12_\n\x06Update\x12..com.baboea.services.RemoteRecipeUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.raw_recipe_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REMOTERECIPELIST']._serialized_start=169
  _globals['_REMOTERECIPELIST']._serialized_end=261
  _globals['_REMOTERECIPEUPDATEREQUEST']._serialized_start=263
  _globals['_REMOTERECIPEUPDATEREQUEST']._serialized_end=353
  _globals['_REMOTERECIPEQUERY']._serialized_start=355
  _globals['_REMOTERECIPEQUERY']._serialized_end=463
  _globals['_REMOTERECIPESERVICE']._serialized_start=466
  _globals['_REMOTERECIPESERVICE']._serialized_end=995
# @@protoc_insertion_point(module_scope)
