# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ServerCommonMessage_pb2 as ServerCommonMessage__pb2
import ServerCommonService_pb2 as ServerCommonService__pb2


class ServerCommonServiceStub(object):
  """///////////////////////////////response//////////////////////////////////////
  公共服务模块通用服务
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.login = channel.unary_unary(
        '/platformserver.ServerCommonService/login',
        request_serializer=ServerCommonService__pb2.LoginRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )


class ServerCommonServiceServicer(object):
  """///////////////////////////////response//////////////////////////////////////
  公共服务模块通用服务
  """

  def login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServerCommonServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'login': grpc.unary_unary_rpc_method_handler(
          servicer.login,
          request_deserializer=ServerCommonService__pb2.LoginRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'platformserver.ServerCommonService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
