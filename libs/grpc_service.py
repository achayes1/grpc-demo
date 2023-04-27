
import test_grpc_service_pb2
import test_grpc_service_pb2_grpc

class TestGrpcService(test_grpc_service_pb2_grpc.TestGrpcServiceServicer):

    def TestGrpcApiRoute(self, request, unused_context) -> test_grpc_service_pb2.TestGrpcApiRouteResponse:
        print(request)
        response = test_grpc_service_pb2.TestGrpcApiRouteResponse(message="PONG")

        return response