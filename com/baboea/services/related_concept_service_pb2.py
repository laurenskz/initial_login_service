# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/baboea/services/related_concept_service.proto
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
    'com/baboea/services/related_concept_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import concepts_pb2 as com_dot_baboea_dot_models_dot_concepts__pb2
from com.baboea.models import culinary_groups_pb2 as com_dot_baboea_dot_models_dot_culinary__groups__pb2
from com.baboea.models import recipes_pb2 as com_dot_baboea_dot_models_dot_recipes__pb2
from com.baboea.models import users_pb2 as com_dot_baboea_dot_models_dot_users__pb2
from com.baboea.models import localized_pb2 as com_dot_baboea_dot_models_dot_localized__pb2
from com.baboea.models import weights_pb2 as com_dot_baboea_dot_models_dot_weights__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1com/baboea/services/related_concept_service.proto\x12\x13\x63om.baboea.services\x1a com/baboea/models/concepts.proto\x1a\'com/baboea/models/culinary_groups.proto\x1a\x1f\x63om/baboea/models/recipes.proto\x1a\x1d\x63om/baboea/models/users.proto\x1a!com/baboea/models/localized.proto\x1a\x1f\x63om/baboea/models/weights.proto\"\xc2\x01\n\x13RelatedConceptQuery\x12+\n\x04\x62\x61se\x18\x01 \x03(\x0b\x32\x1d.com.baboea.models.ConceptRef\x12\x30\n\tforbidden\x18\x02 \x03(\x0b\x32\x1d.com.baboea.models.ConceptRef\x12\x38\n\ncategories\x18\x03 \x03(\x0b\x32$.com.baboea.models.RecipeCategoryRef\x12\x12\n\nminSupport\x18\x04 \x01(\x01\"P\n\x16RelatedConceptResponse\x12\x36\n\x0frelatedConcepts\x18\x01 \x03(\x0b\x32\x1d.com.baboea.models.ConceptRef2\x84\x01\n\x15RelatedConceptService\x12k\n\x12GetRelatedConcepts\x12(.com.baboea.services.RelatedConceptQuery\x1a+.com.baboea.services.RelatedConceptResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.related_concept_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RELATEDCONCEPTQUERY']._serialized_start=282
  _globals['_RELATEDCONCEPTQUERY']._serialized_end=476
  _globals['_RELATEDCONCEPTRESPONSE']._serialized_start=478
  _globals['_RELATEDCONCEPTRESPONSE']._serialized_end=558
  _globals['_RELATEDCONCEPTSERVICE']._serialized_start=561
  _globals['_RELATEDCONCEPTSERVICE']._serialized_end=693
# @@protoc_insertion_point(module_scope)
