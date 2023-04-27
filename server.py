import asyncio
import logging
import grpc
import test_grpc_service_pb2_grpc
from libs.grpc_service import TestGrpcService

async def serve() -> None:
    server = grpc.aio.server()
    test_grpc_service_pb2_grpc.add_TestGrpcServiceServicer_to_server(
        TestGrpcService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("Server started")
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())