# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_grpc_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17test_grpc_service.proto\"*\n\x17TestGrpcApiRouteRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"+\n\x18TestGrpcApiRouteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"=\n\x1a\x41uthenticateUserMFARequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"A\n\x1b\x41uthenticateUserMFAResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\x12\r\n\x05valid\x18\x02 \x01(\x08\"=\n\x1e\x41uthenticateUserMFACodeRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"E\n\x1f\x41uthenticateUserMFACodeResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\x12\r\n\x05valid\x18\x02 \x01(\x08\"/\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x66irst\x18\x02 \x01(\t\x12\x0c\n\x04last\x18\x03 \x01(\t2\x8a\x02\n\x0fTestGrpcService\x12G\n\x10TestGrpcApiRoute\x12\x18.TestGrpcApiRouteRequest\x1a\x19.TestGrpcApiRouteResponse\x12P\n\x13\x41uthenticateUserMFA\x12\x1b.AuthenticateUserMFARequest\x1a\x1c.AuthenticateUserMFAResponse\x12\\\n\x17\x41uthenticateUserMFACode\x12\x1f.AuthenticateUserMFACodeRequest\x1a .AuthenticateUserMFACodeResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_grpc_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TESTGRPCAPIROUTEREQUEST._serialized_start=27
  _TESTGRPCAPIROUTEREQUEST._serialized_end=69
  _TESTGRPCAPIROUTERESPONSE._serialized_start=71
  _TESTGRPCAPIROUTERESPONSE._serialized_end=114
  _AUTHENTICATEUSERMFAREQUEST._serialized_start=116
  _AUTHENTICATEUSERMFAREQUEST._serialized_end=177
  _AUTHENTICATEUSERMFARESPONSE._serialized_start=179
  _AUTHENTICATEUSERMFARESPONSE._serialized_end=244
  _AUTHENTICATEUSERMFACODEREQUEST._serialized_start=246
  _AUTHENTICATEUSERMFACODEREQUEST._serialized_end=307
  _AUTHENTICATEUSERMFACODERESPONSE._serialized_start=309
  _AUTHENTICATEUSERMFACODERESPONSE._serialized_end=378
  _USER._serialized_start=380
  _USER._serialized_end=427
  _TESTGRPCSERVICE._serialized_start=430
  _TESTGRPCSERVICE._serialized_end=696
# @@protoc_insertion_point(module_scope)
