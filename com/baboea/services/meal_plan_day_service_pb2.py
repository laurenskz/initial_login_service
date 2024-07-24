# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/baboea/services/meal_plan_day_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.baboea.models import days_pb2 as com_dot_baboea_dot_models_dot_days__pb2
from com.baboea.models import users_pb2 as com_dot_baboea_dot_models_dot_users__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/com/baboea/services/meal_plan_day_service.proto\x12\x13\x63om.baboea.services\x1a\x1c\x63om/baboea/models/days.proto\x1a\x1d\x63om/baboea/models/users.proto\x1a\x1e\x63om/baboea/services/base.proto\"Z\n\x0fMealPlanDayList\x12\x30\n\x05items\x18\x01 \x03(\x0b\x32!.com.baboea.models.MealPlanDayRef\x12\x15\n\rnextPageToken\x18\x02 \x01(\t\"X\n\x18MealPlanDayUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x08newValue\x18\x02 \x01(\x0b\x32\x1e.com.baboea.models.MealPlanDay\"h\n\x10MealPlanDayQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12)\n\x05owner\x18\x04 \x01(\x0b\x32\x1a.com.baboea.models.UserRef2\x89\x04\n\x12MealPlanDayService\x12I\n\x03\x41\x64\x64\x12\x1e.com.baboea.models.MealPlanDay\x1a .com.baboea.services.AddResponse\"\x00\x12O\n\x06Remove\x12\x1e.com.baboea.models.MealPlanDay\x1a#.com.baboea.services.RemoveResponse\"\x00\x12T\n\x06GetAll\x12\".com.baboea.services.GetAllRequest\x1a$.com.baboea.services.MealPlanDayList\"\x00\x12W\n\x06Search\x12%.com.baboea.services.MealPlanDayQuery\x1a$.com.baboea.services.MealPlanDayList\"\x00\x12H\n\x03Get\x12\x1f.com.baboea.services.GetRequest\x1a\x1e.com.baboea.models.MealPlanDay\"\x00\x12^\n\x06Update\x12-.com.baboea.services.MealPlanDayUpdateRequest\x1a#.com.baboea.services.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.baboea.services.meal_plan_day_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MEALPLANDAYLIST']._serialized_start=165
  _globals['_MEALPLANDAYLIST']._serialized_end=255
  _globals['_MEALPLANDAYUPDATEREQUEST']._serialized_start=257
  _globals['_MEALPLANDAYUPDATEREQUEST']._serialized_end=345
  _globals['_MEALPLANDAYQUERY']._serialized_start=347
  _globals['_MEALPLANDAYQUERY']._serialized_end=451
  _globals['_MEALPLANDAYSERVICE']._serialized_start=454
  _globals['_MEALPLANDAYSERVICE']._serialized_end=975
# @@protoc_insertion_point(module_scope)
