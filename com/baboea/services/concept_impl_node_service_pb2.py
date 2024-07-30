# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/concept_impl_node_service.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3com/baboea/services/concept_impl_node_service.proto\x12\x13\x63om.baboea.services\x1a$com/baboea/models/concept_impl.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"v\n\x1d\x43onceptImplementationNodeList\x12>\n\x05items\x18\x01 \x03(\x0b\x32/.com.baboea.models.ConceptImplementationNodeRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"t\n&ConceptImplementationNodeUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12>\n\x08newValue\x18\x02 \x01(\x0b\x32,.com.baboea.models.ConceptImplementationNode\"\xc5\x01\n\x1e\x43onceptImplementationNodeQuery\x12\x43\n\x0eimplementation\x18\x01 \x01(\x0b\x32+.com.baboea.models.ConceptImplementationRef\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef\x12\x13\n\x0b\x63onceptName\x18\x05 \x01(\t2\xe6\x05\n ConceptImplementationNodeService\x12W\n\x03\x41\x64\x64\x12,.com.baboea.models.ConceptImplementationNode\x1a .com.baboea.services.AddResponse\"\x00\x12]\n\x06Remove\x12,.com.baboea.models.ConceptImplementationNode\x1a#.com.baboea.services.RemoveResponse\"\x00\x12\x62\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a\x32.com.baboea.services.ConceptImplementationNodeList\"\x00\x12k\n\x0cGetFullFoods\x12+.com.baboea.models.ConceptImplementationRef\x1a,.com.baboea.models.ConceptImplementationData\"\x00\x12s\n\x06Search\x12\x33.com.baboea.services.ConceptImplementationNodeQuery\x1a\x32.com.baboea.services.ConceptImplementationNodeList\"\x00\x12V\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a,.com.baboea.models.ConceptImplementationNode\"\x00\x12l\n\x06Update\x12;.com.baboea.services.ConceptImplementationNodeUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.concept_impl_node_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONCEPTIMPLEMENTATIONNODELIST']._serialized_start=181
  _globals['_CONCEPTIMPLEMENTATIONNODELIST']._serialized_end=299
  _globals['_CONCEPTIMPLEMENTATIONNODEUPDATEREQUEST']._serialized_start=301
  _globals['_CONCEPTIMPLEMENTATIONNODEUPDATEREQUEST']._serialized_end=417
  _globals['_CONCEPTIMPLEMENTATIONNODEQUERY']._serialized_start=420
  _globals['_CONCEPTIMPLEMENTATIONNODEQUERY']._serialized_end=617
  _globals['_CONCEPTIMPLEMENTATIONNODESERVICE']._serialized_start=620
  _globals['_CONCEPTIMPLEMENTATIONNODESERVICE']._serialized_end=1362
# @@protoc_insertion_point(module_scope)