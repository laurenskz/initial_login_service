# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/baboea/services/property_service.proto
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
    'com/baboea/services/property_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import property_pb2 as com_dot_baboea_dot_models_dot_property__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*com/baboea/services/property_service.proto\x12\x13\x63om.baboea.services\x1a com/baboea/models/property.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"T\n\x0cPropertyList\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.com.baboea.models.PropertyRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"R\n\x15PropertyUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\x08newValue\x18\x02 \x01(\x0b\x32\x1b.com.baboea.models.Property\"h\n\rPropertyQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef\"&\n\x13\x46indByHandleRequest\x12\x0f\n\x07handles\x18\x01 \x03(\t\"E\n\x14\x46indByHandleResponse\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.com.baboea.models.PropertyRef2\xbc\x05\n\x0fPropertyService\x12\x46\n\x03\x41\x64\x64\x12\x1b.com.baboea.models.Property\x1a .com.baboea.services.AddResponse\"\x00\x12\x65\n\x0c\x46indByHandle\x12(.com.baboea.services.FindByHandleRequest\x1a).com.baboea.services.FindByHandleResponse\"\x00\x12\x62\n\x10\x42yHandleOrCreate\x12,.com.baboea.services.FindSingleHandleRequest\x1a\x1e.com.baboea.models.PropertyRef\"\x00\x12L\n\x06Remove\x12\x1b.com.baboea.models.Property\x1a#.com.baboea.services.RemoveResponse\"\x00\x12Q\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a!.com.baboea.services.PropertyList\"\x00\x12Q\n\x06Search\x12\".com.baboea.services.PropertyQuery\x1a!.com.baboea.services.PropertyList\"\x00\x12\x45\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a\x1b.com.baboea.models.Property\"\x00\x12[\n\x06Update\x12*.com.baboea.services.PropertyUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.property_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PROPERTYLIST']._serialized_start=168
  _globals['_PROPERTYLIST']._serialized_end=252
  _globals['_PROPERTYUPDATEREQUEST']._serialized_start=254
  _globals['_PROPERTYUPDATEREQUEST']._serialized_end=336
  _globals['_PROPERTYQUERY']._serialized_start=338
  _globals['_PROPERTYQUERY']._serialized_end=442
  _globals['_FINDBYHANDLEREQUEST']._serialized_start=444
  _globals['_FINDBYHANDLEREQUEST']._serialized_end=482
  _globals['_FINDBYHANDLERESPONSE']._serialized_start=484
  _globals['_FINDBYHANDLERESPONSE']._serialized_end=553
  _globals['_PROPERTYSERVICE']._serialized_start=556
  _globals['_PROPERTYSERVICE']._serialized_end=1256
# @@protoc_insertion_point(module_scope)
