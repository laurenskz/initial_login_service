# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/template_recipe_generation_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import recipes_pb2 as com_dot_baboea_dot_models_dot_recipes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<com/baboea/services/template_recipe_generation_service.proto\x12\x13\x63om.baboea.services\x1a\x1f\x63om/baboea/models/recipes.proto\"?\n\x14SlimRecipeIngredient\x12\x11\n\tconceptId\x18\x01 \x01(\t\x12\x14\n\x0cgramQuantity\x18\x02 \x01(\x01\"m\n\nSlimRecipe\x12\n\n\x02id\x18\x03 \x01(\t\x12>\n\x0bingredients\x18\x01 \x03(\x0b\x32).com.baboea.services.SlimRecipeIngredient\x12\x13\n\x0b\x65ntropyTags\x18\x02 \x03(\t\"V\n\"GenerateTemplateFromRecipesRequest\x12\x30\n\x07recipes\x18\x01 \x03(\x0b\x32\x1f.com.baboea.services.SlimRecipe\"!\n\x1fGeneratedTemplateRecipeResponse2\xb2\x01\n\x1fTemplateRecipeGenerationService\x12\x8e\x01\n\x1bGenerateTemplateFromRecipes\x12\x37.com.baboea.services.GenerateTemplateFromRecipesRequest\x1a\x34.com.baboea.services.GeneratedTemplateRecipeResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.template_recipe_generation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SLIMRECIPEINGREDIENT']._serialized_start=118
  _globals['_SLIMRECIPEINGREDIENT']._serialized_end=181
  _globals['_SLIMRECIPE']._serialized_start=183
  _globals['_SLIMRECIPE']._serialized_end=292
  _globals['_GENERATETEMPLATEFROMRECIPESREQUEST']._serialized_start=294
  _globals['_GENERATETEMPLATEFROMRECIPESREQUEST']._serialized_end=380
  _globals['_GENERATEDTEMPLATERECIPERESPONSE']._serialized_start=382
  _globals['_GENERATEDTEMPLATERECIPERESPONSE']._serialized_end=415
  _globals['_TEMPLATERECIPEGENERATIONSERVICE']._serialized_start=418
  _globals['_TEMPLATERECIPEGENERATIONSERVICE']._serialized_end=596
# @@protoc_insertion_point(module_scope)
