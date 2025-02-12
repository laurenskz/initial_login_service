# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from com.baboea import generaterequest_pb2 as com_dot_baboea_dot_generaterequest__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2
from com.baboea.services import food_log_service_pb2 as com_dot_baboea_dot_services_dot_food__log__service__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in com/baboea/services/food_log_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FoodLogServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetDayToPending = channel.unary_unary(
                '/com.baboea.services.FoodLogService/SetDayToPending',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.SetDayToPendingRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.FromString,
                _registered_method=True)
        self.SaveDay = channel.unary_unary(
                '/com.baboea.services.FoodLogService/SaveDay',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.SaveDayRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.FromString,
                _registered_method=True)
        self.GetDay = channel.unary_unary(
                '/com.baboea.services.FoodLogService/GetDay',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetFoodLogDayRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_generaterequest__pb2.GeneratedMetaDay.FromString,
                _registered_method=True)
        self.GetDetailedDay = channel.unary_unary(
                '/com.baboea.services.FoodLogService/GetDetailedDay',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetFoodLogDayRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GeneratedDayWithReferencedFoods.FromString,
                _registered_method=True)
        self.AddFood = channel.unary_unary(
                '/com.baboea.services.FoodLogService/AddFood',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.AddFoodRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.FromString,
                _registered_method=True)
        self.UpdateFood = channel.unary_unary(
                '/com.baboea.services.FoodLogService/UpdateFood',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.UpdateFoodRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.FromString,
                _registered_method=True)
        self.DeleteFood = channel.unary_unary(
                '/com.baboea.services.FoodLogService/DeleteFood',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.DeleteFoodRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.FromString,
                _registered_method=True)
        self.GetShoppingListFoods = channel.unary_unary(
                '/com.baboea.services.FoodLogService/GetShoppingListFoods',
                request_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetShoppingListFoodsRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetShoppingListFoodsResponse.FromString,
                _registered_method=True)


class FoodLogServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetDayToPending(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveDay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDetailedDay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddFood(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFood(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFood(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShoppingListFoods(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FoodLogServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetDayToPending': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDayToPending,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.SetDayToPendingRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.SerializeToString,
            ),
            'SaveDay': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveDay,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.SaveDayRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.SerializeToString,
            ),
            'GetDay': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDay,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetFoodLogDayRequest.FromString,
                    response_serializer=com_dot_baboea_dot_generaterequest__pb2.GeneratedMetaDay.SerializeToString,
            ),
            'GetDetailedDay': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDetailedDay,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetFoodLogDayRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GeneratedDayWithReferencedFoods.SerializeToString,
            ),
            'AddFood': grpc.unary_unary_rpc_method_handler(
                    servicer.AddFood,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.AddFoodRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.SerializeToString,
            ),
            'UpdateFood': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFood,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.UpdateFoodRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.SerializeToString,
            ),
            'DeleteFood': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFood,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.DeleteFoodRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.SerializeToString,
            ),
            'GetShoppingListFoods': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShoppingListFoods,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetShoppingListFoodsRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_food__log__service__pb2.GetShoppingListFoodsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.baboea.services.FoodLogService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.baboea.services.FoodLogService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FoodLogService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetDayToPending(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/SetDayToPending',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.SetDayToPendingRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SaveDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/SaveDay',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.SaveDayRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/GetDay',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.GetFoodLogDayRequest.SerializeToString,
            com_dot_baboea_dot_generaterequest__pb2.GeneratedMetaDay.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDetailedDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/GetDetailedDay',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.GetFoodLogDayRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_food__log__service__pb2.GeneratedDayWithReferencedFoods.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddFood(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/AddFood',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.AddFoodRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateFood(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/UpdateFood',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.UpdateFoodRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteFood(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/DeleteFood',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.DeleteFoodRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_food__log__service__pb2.NewDailyPropertiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetShoppingListFoods(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.baboea.services.FoodLogService/GetShoppingListFoods',
            com_dot_baboea_dot_services_dot_food__log__service__pb2.GetShoppingListFoodsRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_food__log__service__pb2.GetShoppingListFoodsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
