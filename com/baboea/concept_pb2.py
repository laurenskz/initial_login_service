# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/concept.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import concept_tag_pb2 as com_dot_baboea_dot_models_dot_concept__tag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63om/baboea/concept.proto\x12\ncom.baboea\x1a#com/baboea/models/concept_tag.proto\"5\n\x0bPortionSize\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\x0c\n\x04step\x18\x03 \x01(\x01\"Q\n\x10\x43onceptTagStatus\x12-\n\x03tag\x18\x01 \x01(\x0b\x32 .com.baboea.models.ConceptTagRef\x12\x0e\n\x06status\x18\x02 \x01(\x08\"\xbe\x02\n\x11\x42oolConceptValues\x12G\n\rconceptValues\x18\x01 \x03(\x0b\x32\x30.com.baboea.BoolConceptValues.ConceptValuesEntry\x12\x41\n\nfoodValues\x18\x02 \x03(\x0b\x32-.com.baboea.BoolConceptValues.FoodValuesEntry\x12\x34\n\x0etagPreferences\x18\x03 \x03(\x0b\x32\x1c.com.baboea.ConceptTagStatus\x1a\x34\n\x12\x43onceptValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x31\n\x0f\x46oodValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\xc3\x02\n\x14PortionConceptValues\x12J\n\rconceptValues\x18\x01 \x03(\x0b\x32\x33.com.baboea.PortionConceptValues.ConceptValuesEntry\x12\x44\n\nfoodValues\x18\x02 \x03(\x0b\x32\x30.com.baboea.PortionConceptValues.FoodValuesEntry\x1aM\n\x12\x43onceptValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.com.baboea.PortionSize:\x02\x38\x01\x1aJ\n\x0f\x46oodValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.com.baboea.PortionSize:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.concept_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOOLCONCEPTVALUES_CONCEPTVALUESENTRY']._loaded_options = None
  _globals['_BOOLCONCEPTVALUES_CONCEPTVALUESENTRY']._serialized_options = b'8\001'
  _globals['_BOOLCONCEPTVALUES_FOODVALUESENTRY']._loaded_options = None
  _globals['_BOOLCONCEPTVALUES_FOODVALUESENTRY']._serialized_options = b'8\001'
  _globals['_PORTIONCONCEPTVALUES_CONCEPTVALUESENTRY']._loaded_options = None
  _globals['_PORTIONCONCEPTVALUES_CONCEPTVALUESENTRY']._serialized_options = b'8\001'
  _globals['_PORTIONCONCEPTVALUES_FOODVALUESENTRY']._loaded_options = None
  _globals['_PORTIONCONCEPTVALUES_FOODVALUESENTRY']._serialized_options = b'8\001'
  _globals['_PORTIONSIZE']._serialized_start=77
  _globals['_PORTIONSIZE']._serialized_end=130
  _globals['_CONCEPTTAGSTATUS']._serialized_start=132
  _globals['_CONCEPTTAGSTATUS']._serialized_end=213
  _globals['_BOOLCONCEPTVALUES']._serialized_start=216
  _globals['_BOOLCONCEPTVALUES']._serialized_end=534
  _globals['_BOOLCONCEPTVALUES_CONCEPTVALUESENTRY']._serialized_start=431
  _globals['_BOOLCONCEPTVALUES_CONCEPTVALUESENTRY']._serialized_end=483
  _globals['_BOOLCONCEPTVALUES_FOODVALUESENTRY']._serialized_start=485
  _globals['_BOOLCONCEPTVALUES_FOODVALUESENTRY']._serialized_end=534
  _globals['_PORTIONCONCEPTVALUES']._serialized_start=537
  _globals['_PORTIONCONCEPTVALUES']._serialized_end=860
  _globals['_PORTIONCONCEPTVALUES_CONCEPTVALUESENTRY']._serialized_start=707
  _globals['_PORTIONCONCEPTVALUES_CONCEPTVALUESENTRY']._serialized_end=784
  _globals['_PORTIONCONCEPTVALUES_FOODVALUESENTRY']._serialized_start=786
  _globals['_PORTIONCONCEPTVALUES_FOODVALUESENTRY']._serialized_end=860
# @@protoc_insertion_point(module_scope)
