from __future__ import print_function

import logging

import grpc

import test_grpc_service_pb2
import test_grpc_service_pb2_grpc

def call_grpc_api(stub):
    request = test_grpc_service_pb2.TestGrpcApiRouteRequest(message="PING")
    response = stub.TestGrpcApiRoute(request)
    return response


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_grpc_service_pb2_grpc.TestGrpcServiceStub(channel)
        print("-------------- Pinging API --------------")
        response = call_grpc_api(stub)
        print(response)

if __name__ == '__main__':
    logging.basicConfig()
    run()