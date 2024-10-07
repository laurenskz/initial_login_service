# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/concept_tag_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import concept_tag_pb2 as com_dot_baboea_dot_models_dot_concept__tag__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-com/baboea/services/concept_tag_service.proto\x12\x13\x63om.baboea.services\x1a#com/baboea/models/concept_tag.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"X\n\x0e\x43onceptTagList\x12/\n\x05items\x18\x01 \x03(\x0b\x32 .com.baboea.models.ConceptTagRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"V\n\x17\x43onceptTagUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x08newValue\x18\x02 \x01(\x0b\x32\x1d.com.baboea.models.ConceptTag\"j\n\x0f\x43onceptTagQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef2\xe7\x04\n\x11\x43onceptTagService\x12H\n\x03\x41\x64\x64\x12\x1d.com.baboea.models.ConceptTag\x1a .com.baboea.services.AddResponse\"\x00\x12N\n\x06Remove\x12\x1d.com.baboea.models.ConceptTag\x1a#.com.baboea.services.RemoveResponse\"\x00\x12S\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a#.com.baboea.services.ConceptTagList\"\x00\x12U\n\x06Search\x12$.com.baboea.services.ConceptTagQuery\x1a#.com.baboea.services.ConceptTagList\"\x00\x12G\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a\x1d.com.baboea.models.ConceptTag\"\x00\x12]\n\x06Update\x12,.com.baboea.services.ConceptTagUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x12\x64\n\x10\x42yHandleOrCreate\x12,.com.baboea.services.FindSingleHandleRequest\x1a .com.baboea.models.ConceptTagRef\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.concept_tag_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONCEPTTAGLIST']._serialized_start=174
  _globals['_CONCEPTTAGLIST']._serialized_end=262
  _globals['_CONCEPTTAGUPDATEREQUEST']._serialized_start=264
  _globals['_CONCEPTTAGUPDATEREQUEST']._serialized_end=350
  _globals['_CONCEPTTAGQUERY']._serialized_start=352
  _globals['_CONCEPTTAGQUERY']._serialized_end=458
  _globals['_CONCEPTTAGSERVICE']._serialized_start=461
  _globals['_CONCEPTTAGSERVICE']._serialized_end=1076
# @@protoc_insertion_point(module_scope)
