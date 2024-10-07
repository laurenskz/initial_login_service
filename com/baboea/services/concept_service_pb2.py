# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/concept_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import concepts_pb2 as com_dot_baboea_dot_models_dot_concepts__pb2
from com.baboea.models import concept_tag_pb2 as com_dot_baboea_dot_models_dot_concept__tag__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)com/baboea/services/concept_service.proto\x12\x13\x63om.baboea.services\x1a com/baboea/models/concepts.proto\x1a#com/baboea/models/concept_tag.proto\x1a!com/baboea/models/localized.proto\x1a\x1e\x63om/baboea/services/base.proto\"R\n\x0b\x43onceptList\x12,\n\x05items\x18\x01 \x03(\x0b\x32\x1d.com.baboea.models.ConceptRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"P\n\x14\x43onceptUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12,\n\x08newValue\x18\x02 \x01(\x0b\x32\x1a.com.baboea.models.Concept\"\xab\x01\n\x0c\x43onceptQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12,\n\x06locale\x18\x04 \x01(\x0b\x32\x1c.com.baboea.models.LocaleRef\x12.\n\x04tags\x18\x05 \x03(\x0b\x32 .com.baboea.models.ConceptTagRef\x12\x12\n\ntagHandles\x18\x06 \x03(\t2\xc1\x04\n\x0e\x43onceptService\x12\x45\n\x03\x41\x64\x64\x12\x1a.com.baboea.models.Concept\x1a .com.baboea.services.AddResponse\"\x00\x12K\n\x06Remove\x12\x1a.com.baboea.models.Concept\x1a#.com.baboea.services.RemoveResponse\"\x00\x12P\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a .com.baboea.services.ConceptList\"\x00\x12O\n\x06Search\x12!.com.baboea.services.ConceptQuery\x1a .com.baboea.services.ConceptList\"\x00\x12\x44\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a\x1a.com.baboea.models.Concept\"\x00\x12Z\n\x06Update\x12).com.baboea.services.ConceptUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x12V\n\x08\x42yHandle\x12,.com.baboea.services.FindSingleHandleRequest\x1a\x1a.com.baboea.models.Concept\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.concept_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONCEPTLIST']._serialized_start=204
  _globals['_CONCEPTLIST']._serialized_end=286
  _globals['_CONCEPTUPDATEREQUEST']._serialized_start=288
  _globals['_CONCEPTUPDATEREQUEST']._serialized_end=368
  _globals['_CONCEPTQUERY']._serialized_start=371
  _globals['_CONCEPTQUERY']._serialized_end=542
  _globals['_CONCEPTSERVICE']._serialized_start=545
  _globals['_CONCEPTSERVICE']._serialized_end=1122
# @@protoc_insertion_point(module_scope)
