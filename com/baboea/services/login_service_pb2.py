# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/login_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import curated_diet_pb2 as com_dot_baboea_dot_models_dot_curated__diet__pb2
from com.baboea.models import meal_pb2 as com_dot_baboea_dot_models_dot_meal__pb2
from com.baboea import concept_pb2 as com_dot_baboea_dot_concept__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2
from com.baboea.models import users_pb2 as com_dot_baboea_dot_models_dot_users__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'com/baboea/services/login_service.proto\x12\x13\x63om.baboea.services\x1a$com/baboea/models/curated_diet.proto\x1a\x1c\x63om/baboea/models/meal.proto\x1a\x18\x63om/baboea/concept.proto\x1a\x1e\x63om/baboea/services/base.proto\x1a\x1d\x63om/baboea/models/users.proto\"\xf1\x01\n\x08MealInit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bmealKcalMin\x18\x02 \x01(\x01\x12\x13\n\x0bmealKcalMax\x18\x03 \x01(\x01\x12\x0f\n\x07useKcal\x18\x04 \x01(\x08\x12\x38\n\x05smart\x18\x05 \x01(\x0b\x32).com.baboea.models.SmartRecipePreferences\x12\x31\n\nsideDishes\x18\x06 \x01(\x0b\x32\x1d.com.baboea.BoolConceptValues\x12/\n\x08mealSize\x18\x07 \x01(\x0e\x32\x1d.com.baboea.services.MealSize\"G\n\x0eNutritionPrefs\x12\x0c\n\x04kcal\x18\x01 \x01(\x01\x12\x0f\n\x07protein\x18\x02 \x01(\x01\x12\x16\n\x0e\x63\x61rbPercentage\x18\x03 \x01(\x01\"\xb5\x01\n\x0cPersonalData\x12+\n\x06gender\x18\x01 \x01(\x0e\x32\x1b.com.baboea.services.Gender\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x39\n\ractivityLevel\x18\x03 \x01(\x0e\x32\".com.baboea.services.ActivityLevel\x12\x10\n\x08weightKg\x18\x04 \x01(\x01\x12\x10\n\x08heightCm\x18\x05 \x01(\x01\x12\x0c\n\x04name\x18\x06 \x01(\t\"\xf1\x02\n\x10InitialLoginForm\x12\x33\n\x08personal\x18\x01 \x01(\x0b\x32!.com.baboea.services.PersonalData\x12\x38\n\x06manual\x18\x02 \x01(\x0b\x32#.com.baboea.services.NutritionPrefsH\x00\x88\x01\x01\x12/\n\x04\x64iet\x18\x03 \x01(\x0b\x32!.com.baboea.models.CuratedDietRef\x12\x32\n\x06macros\x18\x04 \x01(\x0e\x32\".com.baboea.services.MacroStrategy\x12,\n\x05meals\x18\x05 \x03(\x0b\x32\x1d.com.baboea.services.MealInit\x12\x14\n\x0cremoteUserId\x18\x06 \x01(\t\x12:\n\nweightLoss\x18\x07 \x01(\x0e\x32&.com.baboea.services.DesiredWeightLossB\t\n\x07_manual\"$\n\x0cLoginRequest\x12\x14\n\x0cremoteUserId\x18\x01 \x01(\t\"L\n\rLoginResponse\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.com.baboea.models.UserRef\x12\x11\n\tneedsInit\x18\x02 \x01(\x08*)\n\x06Gender\x12\x08\n\x04male\x10\x00\x12\n\n\x06\x66\x65male\x10\x01\x12\t\n\x05other\x10\x02**\n\x08MealSize\x12\t\n\x05small\x10\x00\x12\n\n\x06normal\x10\x01\x12\x07\n\x03\x62ig\x10\x02*h\n\rActivityLevel\x12\r\n\tsedentary\x10\x00\x12\x11\n\rlightlyActive\x10\x01\x12\x14\n\x10moderatelyActive\x10\x02\x12\x0e\n\nveryActive\x10\x03\x12\x0f\n\x0b\x65xtraActive\x10\x04*G\n\rMacroStrategy\x12\x0c\n\x08\x62\x61lanced\x10\x00\x12\x08\n\x04keto\x10\x01\x12\x0c\n\x08low_carb\x10\x02\x12\x10\n\x0chigh_protein\x10\x03*S\n\x11\x44\x65siredWeightLoss\x12\x0f\n\x0bgain_weight\x10\x00\x12\x0c\n\x08maintain\x10\x01\x12\x0f\n\x0blose_slowly\x10\x02\x12\x0e\n\nlose_rapid\x10\x03\x32`\n\x0cLoginService\x12P\n\x05Login\x12!.com.baboea.services.LoginRequest\x1a\".com.baboea.services.LoginResponse\"\x00\x32o\n\x0fUserInitService\x12\\\n\tSetupUser\x12%.com.baboea.services.InitialLoginForm\x1a&.com.baboea.services.OperationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.login_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GENDER']._serialized_start=1210
  _globals['_GENDER']._serialized_end=1251
  _globals['_MEALSIZE']._serialized_start=1253
  _globals['_MEALSIZE']._serialized_end=1295
  _globals['_ACTIVITYLEVEL']._serialized_start=1297
  _globals['_ACTIVITYLEVEL']._serialized_end=1401
  _globals['_MACROSTRATEGY']._serialized_start=1403
  _globals['_MACROSTRATEGY']._serialized_end=1474
  _globals['_DESIREDWEIGHTLOSS']._serialized_start=1476
  _globals['_DESIREDWEIGHTLOSS']._serialized_end=1559
  _globals['_MEALINIT']._serialized_start=222
  _globals['_MEALINIT']._serialized_end=463
  _globals['_NUTRITIONPREFS']._serialized_start=465
  _globals['_NUTRITIONPREFS']._serialized_end=536
  _globals['_PERSONALDATA']._serialized_start=539
  _globals['_PERSONALDATA']._serialized_end=720
  _globals['_INITIALLOGINFORM']._serialized_start=723
  _globals['_INITIALLOGINFORM']._serialized_end=1092
  _globals['_LOGINREQUEST']._serialized_start=1094
  _globals['_LOGINREQUEST']._serialized_end=1130
  _globals['_LOGINRESPONSE']._serialized_start=1132
  _globals['_LOGINRESPONSE']._serialized_end=1208
  _globals['_LOGINSERVICE']._serialized_start=1561
  _globals['_LOGINSERVICE']._serialized_end=1657
  _globals['_USERINITSERVICE']._serialized_start=1659
  _globals['_USERINITSERVICE']._serialized_end=1770
# @@protoc_insertion_point(module_scope)
