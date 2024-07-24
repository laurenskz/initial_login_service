# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/meal_component_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import meal_components_pb2 as com_dot_baboea_dot_models_dot_meal__components__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0com/baboea/services/meal_component_service.proto\x12\x13\x63om.baboea.services\x1a\'com/baboea/models/meal_components.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"^\n\x11MealComponentList\x12\x32\n\x05items\x18\x01 \x03(\x0b\x32#.com.baboea.models.MealComponentRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"\\\n\x1aMealComponentUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x08newValue\x18\x02 \x01(\x0b\x32 .com.baboea.models.MealComponent\"m\n\x12MealComponentQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef2\x99\x04\n\x14MealComponentService\x12K\n\x03\x41\x64\x64\x12 .com.baboea.models.MealComponent\x1a .com.baboea.services.AddResponse\"\x00\x12Q\n\x06Remove\x12 .com.baboea.models.MealComponent\x1a#.com.baboea.services.RemoveResponse\"\x00\x12V\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a&.com.baboea.services.MealComponentList\"\x00\x12[\n\x06Search\x12\'.com.baboea.services.MealComponentQuery\x1a&.com.baboea.services.MealComponentList\"\x00\x12J\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a .com.baboea.models.MealComponent\"\x00\x12`\n\x06Update\x12/.com.baboea.services.MealComponentUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.meal_component_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MEALCOMPONENTLIST']._serialized_start=181
  _globals['_MEALCOMPONENTLIST']._serialized_end=275
  _globals['_MEALCOMPONENTUPDATEREQUEST']._serialized_start=277
  _globals['_MEALCOMPONENTUPDATEREQUEST']._serialized_end=369
  _globals['_MEALCOMPONENTQUERY']._serialized_start=371
  _globals['_MEALCOMPONENTQUERY']._serialized_end=480
  _globals['_MEALCOMPONENTSERVICE']._serialized_start=483
  _globals['_MEALCOMPONENTSERVICE']._serialized_end=1020
# @@protoc_insertion_point(module_scope)
