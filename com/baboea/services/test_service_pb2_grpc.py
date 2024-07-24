# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from com.baboea.models import test_pb2 as com_dot_baboea_dot_models_dot_test__pb2
from com.baboea.services import base_pb2 as com_dot_baboea_dot_services_dot_base__pb2
from com.baboea.services import test_service_pb2 as com_dot_baboea_dot_services_dot_test__service__pb2

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
        + f' but the generated code in com/baboea/services/test_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/com.baboea.services.TestService/Add',
                request_serializer=com_dot_baboea_dot_models_dot_test__pb2.Test.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.AddResponse.FromString,
                _registered_method=True)
        self.Remove = channel.unary_unary(
                '/com.baboea.services.TestService/Remove',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveResponse.FromString,
                _registered_method=True)
        self.GetAll = channel.unary_unary(
                '/com.baboea.services.TestService/GetAll',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_test__service__pb2.TestList.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/com.baboea.services.TestService/Get',
                request_serializer=com_dot_baboea_dot_services_dot_base__pb2.GetRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_models_dot_test__pb2.Test.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/com.baboea.services.TestService/Update',
                request_serializer=com_dot_baboea_dot_services_dot_test__service__pb2.TestUpdateRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.FromString,
                _registered_method=True)


class TestServiceServicer(object):
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

    def GetAll(self, request, context):
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


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=com_dot_baboea_dot_models_dot_test__pb2.Test.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.AddResponse.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.RemoveResponse.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_test__service__pb2.TestList.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=com_dot_baboea_dot_services_dot_base__pb2.GetRequest.FromString,
                    response_serializer=com_dot_baboea_dot_models_dot_test__pb2.Test.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=com_dot_baboea_dot_services_dot_test__service__pb2.TestUpdateRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_base__pb2.UpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.baboea.services.TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.baboea.services.TestService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
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
            '/com.baboea.services.TestService/Add',
            com_dot_baboea_dot_models_dot_test__pb2.Test.SerializeToString,
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
            '/com.baboea.services.TestService/Remove',
            com_dot_baboea_dot_services_dot_base__pb2.RemoveRequest.SerializeToString,
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
            '/com.baboea.services.TestService/GetAll',
            com_dot_baboea_dot_services_dot_base__pb2.GetAllRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_test__service__pb2.TestList.FromString,
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
            '/com.baboea.services.TestService/Get',
            com_dot_baboea_dot_services_dot_base__pb2.GetRequest.SerializeToString,
            com_dot_baboea_dot_models_dot_test__pb2.Test.FromString,
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
            '/com.baboea.services.TestService/Update',
            com_dot_baboea_dot_services_dot_test__service__pb2.TestUpdateRequest.SerializeToString,
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
