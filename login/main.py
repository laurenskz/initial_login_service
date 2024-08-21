from concurrent import futures

import grpc
import os

from com.baboea.models.days_pb2 import MealPlanDay
from com.baboea.services import login_service_pb2_grpc
from login.bmr import BaseBmrUseCase
import traceback
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
                except Exception as err:
                    traceback.print_exception(err)

            return new_behavior

        return _wrap_rpc_behavior(continuation(handler_call_details), latency_wrapper)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=[TracebackLoggerInterceptor()])
    login_service_pb2_grpc.add_UserInitServiceServicer_to_server(GrpcLoginService(
        channel=grpc.insecure_channel(os.getenv("CRUD_SERVICE_URL") or "localhost:50052"),
        use_case=BaseBmrUseCase()
    ), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
