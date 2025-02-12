# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from com.baboea.services import build_a_recipe_service_pb2 as com_dot_baboea_dot_services_dot_build__a__recipe__service__pb2

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
        + f' but the generated code in com/baboea/services/build_a_recipe_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class BuildARecipeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BuildARecipe = channel.stream_stream(
                '/com.baboea.services.BuildARecipeService/BuildARecipe',
                request_serializer=com_dot_baboea_dot_services_dot_build__a__recipe__service__pb2.BuildARecipeRequest.SerializeToString,
                response_deserializer=com_dot_baboea_dot_services_dot_build__a__recipe__service__pb2.BuildARecipeResponse.FromString,
                _registered_method=True)


class BuildARecipeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BuildARecipe(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BuildARecipeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BuildARecipe': grpc.stream_stream_rpc_method_handler(
                    servicer.BuildARecipe,
                    request_deserializer=com_dot_baboea_dot_services_dot_build__a__recipe__service__pb2.BuildARecipeRequest.FromString,
                    response_serializer=com_dot_baboea_dot_services_dot_build__a__recipe__service__pb2.BuildARecipeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.baboea.services.BuildARecipeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.baboea.services.BuildARecipeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BuildARecipeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BuildARecipe(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/com.baboea.services.BuildARecipeService/BuildARecipe',
            com_dot_baboea_dot_services_dot_build__a__recipe__service__pb2.BuildARecipeRequest.SerializeToString,
            com_dot_baboea_dot_services_dot_build__a__recipe__service__pb2.BuildARecipeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
