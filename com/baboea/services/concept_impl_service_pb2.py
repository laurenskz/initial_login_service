# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/concept_impl_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import concept_impl_pb2 as com_dot_baboea_dot_models_dot_concept__impl__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.com/baboea/services/concept_impl_service.proto\x12\x13\x63om.baboea.services\x1a$com/baboea/models/concept_impl.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"n\n\x19\x43onceptImplementationList\x12:\n\x05items\x18\x01 \x03(\x0b\x32+.com.baboea.models.ConceptImplementationRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"l\n\"ConceptImplementationUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12:\n\x08newValue\x18\x02 \x01(\x0b\x32(.com.baboea.models.ConceptImplementation\"u\n\x1a\x43onceptImplementationQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef2\xd9\x04\n\x1c\x43onceptImplementationService\x12S\n\x03\x41\x64\x64\x12(.com.baboea.models.ConceptImplementation\x1a .com.baboea.services.AddResponse\"\x00\x12Y\n\x06Remove\x12(.com.baboea.models.ConceptImplementation\x1a#.com.baboea.services.RemoveResponse\"\x00\x12^\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a..com.baboea.services.ConceptImplementationList\"\x00\x12k\n\x06Search\x12/.com.baboea.services.ConceptImplementationQuery\x1a..com.baboea.services.ConceptImplementationList\"\x00\x12R\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a(.com.baboea.models.ConceptImplementation\"\x00\x12h\n\x06Update\x12\x37.com.baboea.services.ConceptImplementationUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.concept_impl_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONCEPTIMPLEMENTATIONLIST']._serialized_start=176
  _globals['_CONCEPTIMPLEMENTATIONLIST']._serialized_end=286
  _globals['_CONCEPTIMPLEMENTATIONUPDATEREQUEST']._serialized_start=288
  _globals['_CONCEPTIMPLEMENTATIONUPDATEREQUEST']._serialized_end=396
  _globals['_CONCEPTIMPLEMENTATIONQUERY']._serialized_start=398
  _globals['_CONCEPTIMPLEMENTATIONQUERY']._serialized_end=515
  _globals['_CONCEPTIMPLEMENTATIONSERVICE']._serialized_start=518
  _globals['_CONCEPTIMPLEMENTATIONSERVICE']._serialized_end=1119
# @@protoc_insertion_point(module_scope)