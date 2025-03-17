# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from com.baboea.models import food_source_pb2 as com_dot_baboea_dot_models_dot_food__source__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2
from com.baboea.services import food_source_service_pb2 as com_dot_baboea_dot_services_dot_food__source__service__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in com/baboea/services/food_source_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FoodSourceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/com.baboea.services.FoodSourceService/Add',
                request_serializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.AddResponse.FromString,
                _registered_method=True)
        self.Remove = channel.unary_unary(
                '/com.baboea.services.FoodSourceService/Remove',
                request_serializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveResponse.FromString,
                _registered_method=True)
        self.ByHandleOrCreate = channel.unary_unary(
                '/com.baboea.services.FoodSourceService/ByHandleOrCreate',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.FindSingleHandleRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSourceRef.FromString,
                _registered_method=True)
        self.GetAll = channel.unary_unary(
                '/com.baboea.services.FoodSourceService/GetAll',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceList.FromString,
                _registered_method=True)
        self.Search = channel.unary_unary(
                '/com.baboea.services.FoodSourceService/Search',
                request_serializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceQuery.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceList.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/com.baboea.services.FoodSourceService/Get',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.GetRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/com.baboea.services.FoodSourceService/Update',
                request_serializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceUpdateRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.FromString,
                _registered_method=True)


class FoodSourceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ByHandleOrCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FoodSourceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.AddResponse.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveResponse.SerializeToString,
            ),
            'ByHandleOrCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.ByHandleOrCreate,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.FindSingleHandleRequest.FromString,
                    response_serializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSourceRef.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceList.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceQuery.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceList.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.GetRequest.FromString,
                    response_serializer=com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceUpdateRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.baboea.services.FoodSourceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.baboea.services.FoodSourceService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FoodSourceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Add(request,
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
            '/com.baboea.services.FoodSourceService/Add',
            com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.SerializeToString,
            com_dot_baboea_dot_services_dot_base__pb2.AddResponse.FromString,
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
    def Remove(request,
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
            '/com.baboea.services.FoodSourceService/Remove',
            com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.SerializeToString,
            com_dot_baboea_dot_services_dot_base__pb2.RemoveResponse.FromString,
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
    def ByHandleOrCreate(request,
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
            '/com.baboea.services.FoodSourceService/ByHandleOrCreate',
            com_dot_baboea_dot_services_dot_base__pb2.FindSingleHandleRequest.SerializeToString,
            com_dot_baboea_dot_models_dot_food__source__pb2.FoodSourceRef.FromString,
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
    def GetAll(request,
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
            '/com.baboea.services.FoodSourceService/GetAll',
            com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceList.FromString,
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
    def Search(request,
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
            '/com.baboea.services.FoodSourceService/Search',
            com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceQuery.SerializeToString,
            com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceList.FromString,
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
    def Get(request,
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
            '/com.baboea.services.FoodSourceService/Get',
            com_dot_baboea_dot_services_dot_base__pb2.GetRequest.SerializeToString,
            com_dot_baboea_dot_models_dot_food__source__pb2.FoodSource.FromString,
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
    def Update(request,
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
            '/com.baboea.services.FoodSourceService/Update',
            com_dot_baboea_dot_services_dot_food__source__service__pb2.FoodSourceUpdateRequest.SerializeToString,
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
