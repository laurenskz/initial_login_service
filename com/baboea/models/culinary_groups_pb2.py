# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/models/culinary_groups.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.models import concepts_pb2 as com_dot_baboea_dot_models_dot_concepts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'com/baboea/models/culinary_groups.proto\x12\x11\x63om.baboea.models\x1a!com/baboea/models/localized.proto\x1a com/baboea/models/concepts.proto\"\xb1\x01\n\rCulinaryGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\rlocalizations\x18\x02 \x03(\x0b\x32).com.baboea.models.CulinaryGroupLocalized\x12/\n\x08\x63oncepts\x18\x03 \x03(\x0b\x32\x1d.com.baboea.models.ConceptRef\x12\r\n\x05\x65moji\x18\x04 \x01(\t\x12\x12\n\nimportance\x18\x05 \x01(\x01\"s\n\x10\x43ulinaryGroupRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x04name\x18\x02 \x01(\x0b\x32\".com.baboea.models.LocalizedString\x12\r\n\x05\x65moji\x18\x03 \x01(\t\x12\x12\n\nimportance\x18\x04 \x01(\x01\";\n\x16\x43ulinaryGroupLocalized\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.models.culinary_groups_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CULINARYGROUP']._serialized_start=132
  _globals['_CULINARYGROUP']._serialized_end=309
  _globals['_CULINARYGROUPREF']._serialized_start=311
  _globals['_CULINARYGROUPREF']._serialized_end=426
  _globals['_CULINARYGROUPLOCALIZED']._serialized_start=428
  _globals['_CULINARYGROUPLOCALIZED']._serialized_end=487
# @@protoc_insertion_point(module_scope)
