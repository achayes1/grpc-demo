
import test_grpc_service_pb2
import test_grpc_service_pb2_grpc
from pydash import get

class TestGrpcService(test_grpc_service_pb2_grpc.TestGrpcServiceServicer):

    def TestGrpcApiRoute(self, request, unused_context) -> test_grpc_service_pb2.TestGrpcApiRouteResponse:
        print(request)
        response = test_grpc_service_pb2.TestGrpcApiRouteResponse(message="PONG")

        return response
    
    def AuthenticateUserMFA(self, request, unused_context) -> test_grpc_service_pb2.AuthenticateUserMFAResponse:

        passed_email = get(request, 'email')
        passed_password = get(request, 'password')

        if (passed_email != "testemail@email.com" or passed_password != "testpassword123!"):
            return test_grpc_service_pb2.AuthenticateUserMFAResponse(valid=False)

        response = test_grpc_service_pb2.AuthenticateUserMFAResponse(user=test_grpc_service_pb2.User(id=1, first="Andy", last="Hayes"), valid=True)

        return response
    
    def AuthenticateUserMFACode(self, request, unused_context) -> test_grpc_service_pb2.AuthenticateUserMFACodeResponse:
        print(request)
        code = get(request, 'code')


        if (code != 123456):
            return test_grpc_service_pb2.AuthenticateUserMFACodeResponse(valid=False)
        response = test_grpc_service_pb2.AuthenticateUserMFACodeResponse(user=test_grpc_service_pb2.User(id=1, first="Andy", last="Hayes"), valid=True)

        return response