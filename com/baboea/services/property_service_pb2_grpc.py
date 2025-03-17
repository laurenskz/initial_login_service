# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from com.baboea.models import property_pb2 as com_dot_baboea_dot_models_dot_property__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2
from com.baboea.services import property_service_pb2 as com_dot_baboea_dot_services_dot_property__service__pb2

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
        + f' but the generated code in com/baboea/services/property_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PropertyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/com.baboea.services.PropertyService/Add',
                request_serializer=com_dot_baboea_dot_models_dot_property__pb2.Property.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.AddResponse.FromString,
                _registered_method=True)
        self.FindByHandle = channel.unary_unary(
                '/com.baboea.services.PropertyService/FindByHandle',
                request_serializer=com_dot_baboea_dot_services_dot_property__service__pb2.FindByHandleRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_property__service__pb2.FindByHandleResponse.FromString,
                _registered_method=True)
        self.ByHandleOrCreate = channel.unary_unary(
                '/com.baboea.services.PropertyService/ByHandleOrCreate',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.FindSingleHandleRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_models_dot_property__pb2.PropertyRef.FromString,
                _registered_method=True)
        self.Remove = channel.unary_unary(
                '/com.baboea.services.PropertyService/Remove',
                request_serializer=com_dot_baboea_dot_models_dot_property__pb2.Property.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveResponse.FromString,
                _registered_method=True)
        self.GetAll = channel.unary_unary(
                '/com.baboea.services.PropertyService/GetAll',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyList.FromString,
                _registered_method=True)
        self.Search = channel.unary_unary(
                '/com.baboea.services.PropertyService/Search',
                request_serializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyQuery.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyList.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/com.baboea.services.PropertyService/Get',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.GetRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_models_dot_property__pb2.Property.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/com.baboea.services.PropertyService/Update',
                request_serializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyUpdateRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.FromString,
                _registered_method=True)


class PropertyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindByHandle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ByHandleOrCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
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


def add_PropertyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=com_dot_baboea_dot_models_dot_property__pb2.Property.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.AddResponse.SerializeToString,
            ),
            'FindByHandle': grpc.unary_unary_rpc_method_handler(
                    servicer.FindByHandle,
                    request_deserializer=com_dot_baboea_dot_services_dot_property__service__pb2.FindByHandleRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_property__service__pb2.FindByHandleResponse.SerializeToString,
            ),
            'ByHandleOrCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.ByHandleOrCreate,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.FindSingleHandleRequest.FromString,
                    response_serializer=com_dot_baboea_dot_models_dot_property__pb2.PropertyRef.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=com_dot_baboea_dot_models_dot_property__pb2.Property.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveResponse.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyList.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyQuery.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyList.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.GetRequest.FromString,
                    response_serializer=com_dot_baboea_dot_models_dot_property__pb2.Property.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=com_dot_baboea_dot_services_dot_property__service__pb2.PropertyUpdateRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.baboea.services.PropertyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.baboea.services.PropertyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PropertyService(object):
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
            '/com.baboea.services.PropertyService/Add',
            com_dot_baboea_dot_models_dot_property__pb2.Property.SerializeToString,
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
    def FindByHandle(request,
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
            '/com.baboea.services.PropertyService/FindByHandle',
            com_dot_baboea_dot_services_dot_property__service__pb2.FindByHandleRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_property__service__pb2.FindByHandleResponse.FromString,
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
            '/com.baboea.services.PropertyService/ByHandleOrCreate',
            com_dot_baboea_dot_services_dot_base__pb2.FindSingleHandleRequest.SerializeToString,
            com_dot_baboea_dot_models_dot_property__pb2.PropertyRef.FromString,
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
            '/com.baboea.services.PropertyService/Remove',
            com_dot_baboea_dot_models_dot_property__pb2.Property.SerializeToString,
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
            '/com.baboea.services.PropertyService/GetAll',
            com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_property__service__pb2.PropertyList.FromString,
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
            '/com.baboea.services.PropertyService/Search',
            com_dot_baboea_dot_services_dot_property__service__pb2.PropertyQuery.SerializeToString,
            com_dot_baboea_dot_services_dot_property__service__pb2.PropertyList.FromString,
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
            '/com.baboea.services.PropertyService/Get',
            com_dot_baboea_dot_services_dot_base__pb2.GetRequest.SerializeToString,
            com_dot_baboea_dot_models_dot_property__pb2.Property.FromString,
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
            '/com.baboea.services.PropertyService/Update',
            com_dot_baboea_dot_services_dot_property__service__pb2.PropertyUpdateRequest.SerializeToString,
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
