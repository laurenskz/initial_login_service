import os
import sys
from concurrent import futures

import grpc
from loguru import logger

from com.baboea.models.concepts_pb2 import ConceptRef
from com.baboea.services import login_service_pb2_grpc
from com.baboea.services.application_level_service_pb2_grpc import ApplicationLevelServiceStub
from com.baboea.services.base_pb2 import FindSingleHandleRequest
from com.baboea.services.concept_service_pb2_grpc import ConceptServiceStub
from com.baboea.services.concept_tag_service_pb2_grpc import ConceptTagServiceStub
from com.baboea.services.property_service_pb2_grpc import PropertyServiceStub
from login.bmr import BaseBmrUseCase
from login.dependencies import Concepts, ConceptTags, ApplicationLevels, InitProperties, GrpcPropertyByHandleResolver
from login.impl import GrpcLoginService


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
    channel = grpc.insecure_channel(os.getenv("CRUD_SERVICE_URL") or "localhost:50052")
    prop_service = PropertyServiceStub(channel)
    tag_service = ConceptTagServiceStub(channel)
    concept_service = ConceptServiceStub(channel)
    application_service = ApplicationLevelServiceStub(channel)

    login_service_pb2_grpc.add_UserInitServiceServicer_to_server(GrpcLoginService(
        channel=channel,
        use_case=BaseBmrUseCase(),
        concepts=Concepts(
            root=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="root")).id),
            fat=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="fat")).id),
            pantry=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="pantry")).id),
            water=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="water")).id),
            fruit=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="fruit")).id),
            vegetable=ConceptRef(id=concept_service.ByHandle(FindSingleHandleRequest(handle="vegetable")).id),
        ),
        tags=ConceptTags(
            common_item=tag_service.ByHandleOrCreate(FindSingleHandleRequest(handle="common_supermarket")),
            side_dish=tag_service.ByHandleOrCreate(FindSingleHandleRequest(handle="normal_side_food")),
        ),
        application_levels=ApplicationLevels(
            meal=application_service.ByHandleOrCreate(FindSingleHandleRequest(handle="meal")),
            day=application_service.ByHandleOrCreate(FindSingleHandleRequest(handle="day")),
        ),
        properties=InitProperties(
            kcal=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="kcal")),
            protein=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="protein")),
            net_carbs=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="net_carbs")),
            fat=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="fat")),
            fiber=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="fiber")),
            recipe_count=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="recipe_count")),
            food_weight=prop_service.ByHandleOrCreate(FindSingleHandleRequest(handle="food_weight"))
        ),
        property_resolver=GrpcPropertyByHandleResolver(prop_service)
    ), server)
    server.add_insecure_port("[::]:50053")
    # start_http_server(8000)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stdout, format="{message}", serialize=True, level="INFO")
    serve()
