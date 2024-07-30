# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/locale_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import food_pb2 as com_dot_baboea_dot_models_dot_food__pb2
from com.baboea.models import property_pb2 as com_dot_baboea_dot_models_dot_property__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(com/baboea/services/locale_service.proto\x12\x13\x63om.baboea.services\x1a\x1c\x63om/baboea/models/food.proto\x1a com/baboea/models/property.proto\x1a\x1e\x63om/baboea/services/base.proto\x1a!com/baboea/models/localized.proto\"P\n\nLocaleList\x12+\n\x05items\x18\x01 \x03(\x0b\x32\x1c.com.baboea.models.LocaleRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"N\n\x13LocaleUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\x08newValue\x18\x02 \x01(\x0b\x32\x19.com.baboea.models.Locale\"8\n\x0bLocaleQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x32\xe1\x03\n\rLocaleService\x12\x44\n\x03\x41\x64\x64\x12\x19.com.baboea.models.Locale\x1a .com.baboea.services.AddResponse\"\x00\x12J\n\x06Remove\x12\x19.com.baboea.models.Locale\x1a#.com.baboea.services.RemoveResponse\"\x00\x12O\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a\x1f.com.baboea.services.LocaleList\"\x00\x12M\n\x06Search\x12 .com.baboea.services.LocaleQuery\x1a\x1f.com.baboea.services.LocaleList\"\x00\x12\x43\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a\x19.com.baboea.models.Locale\"\x00\x12Y\n\x06Update\x12(.com.baboea.services.LocaleUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.locale_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOCALELIST']._serialized_start=196
  _globals['_LOCALELIST']._serialized_end=276
  _globals['_LOCALEUPDATEREQUEST']._serialized_start=278
  _globals['_LOCALEUPDATEREQUEST']._serialized_end=356
  _globals['_LOCALEQUERY']._serialized_start=358
  _globals['_LOCALEQUERY']._serialized_end=414
  _globals['_LOCALESERVICE']._serialized_start=417
  _globals['_LOCALESERVICE']._serialized_end=898
# @@protoc_insertion_point(module_scope)