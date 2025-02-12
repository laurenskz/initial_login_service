import os
import sys
from concurrent import futures

import grpc
from injector import Injector
from loguru import logger

from com.baboea.models.concepts_pb2 import ConceptRef
from com.baboea.services import login_service_pb2_grpc
from com.baboea.services.application_level_service_pb2_grpc import ApplicationLevelServiceStub
from com.baboea.services.base_pb2 import FindSingleHandleRequest
from com.baboea.services.concept_service_pb2_grpc import ConceptServiceStub
from com.baboea.services.concept_tag_service_pb2_grpc import ConceptTagServiceStub
from com.baboea.services.login_service_pb2_grpc import UserInitServiceServicer
from com.baboea.services.property_service_pb2_grpc import PropertyServiceStub
from login.bmr import BaseBmrUseCase
from login.dependencies import Concepts, ConceptTags, ApplicationLevels, InitProperties, GrpcPropertyByHandleResolver
from login.impl import GrpcLoginService
from login.modules import ObjectiveModule, UseCaseModule, DataModule, NetworkingModule, CreatorModule


def _wrap_rpc_behavior(handler, fn):
    if handler is None:
        return None

    if handler.request_streaming and handler.response_streaming:
        behavior_fn = handler.stream_stream
        handler_factory = grpc.stream_stream_rpc_method_handler
    elif handler.request_streaming and not handler.response_streaming:
        behavior_fn = handler.stream_unary
        handler_factory = grpc.stream_unary_rpc_method_handler
    elif not handler.request_streaming and handler.response_streaming:
        behavior_fn = handler.unary_stream
        handler_factory = grpc.unary_stream_rpc_method_handler
    else:
        behavior_fn = handler.unary_unary
        handler_factory = grpc.unary_unary_rpc_method_handler

    return handler_factory(fn(behavior_fn,
                              handler.request_streaming,
                              handler.response_streaming),
                           request_deserializer=handler.request_deserializer,
                           response_serializer=handler.response_serializer)


class TracebackLoggerInterceptor(grpc.ServerInterceptor):

    def intercept_service(self, continuation, handler_call_details):
        def latency_wrapper(behavior, request_streaming, response_streaming):

            def new_behavior(request_or_iterator, servicer_context):
                try:
                    return behavior(request_or_iterator, servicer_context)
                except Exception:
                    logger.exception("Failed processing request")

            return new_behavior

        return _wrap_rpc_behavior(continuation(handler_call_details), latency_wrapper)


def serve():
    logger.info("Starting login service")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=[TracebackLoggerInterceptor()])

    injector = Injector(modules=[
        ObjectiveModule(),
        UseCaseModule(),
        DataModule(),
        NetworkingModule(),
        CreatorModule()
    ])
    servicer = injector.get(UserInitServiceServicer)
    login_service_pb2_grpc.add_UserInitServiceServicer_to_server(servicer, server)
    server.add_insecure_port("[::]:50053")
    # start_http_server(8000)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    # logger.remove()
    # logger.add(sys.stdout, format="{message}", serialize=True, level="INFO")
    serve()
