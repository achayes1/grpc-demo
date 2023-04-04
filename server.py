import asyncio
import logging

import grpc
from sdks.python import test_grpc_service_pb2
from sdks.python import test_grpc_service_pb2_grpc

class TestGrpcService(test_grpc_service_pb2_grpc.TestGrpcServiceServicer):

    def __init__(self) -> None:
        self.num_calls = 0

    def TestGrpcApiRoute(self, request, unused_context) -> test_grpc_service_pb2.TestGrpcApiRouteResponse:
        print(request)
        print(f"Request: {request['message']}")

        response = test_grpc_service_pb2.TestGrpcApiRouteResponse(message="PONG")

        return response

async def serve() -> None:
    server = grpc.aio.server()
    test_grpc_service_pb2_grpc.add_TestGrpcServiceServicer_to_server(
        TestGrpcService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())