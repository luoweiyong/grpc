# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ServerCommonMessage_pb2 as ServerCommonMessage__pb2
import ServerUserService_pb2 as ServerUserService__pb2


class ServerUserServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.save = channel.unary_unary(
        '/platformserver.ServerUserService/save',
        request_serializer=ServerUserService__pb2.SaveRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.update = channel.unary_unary(
        '/platformserver.ServerUserService/update',
        request_serializer=ServerUserService__pb2.UpdateRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.delete = channel.unary_unary(
        '/platformserver.ServerUserService/delete',
        request_serializer=ServerUserService__pb2.DeleteRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.findOne = channel.unary_unary(
        '/platformserver.ServerUserService/findOne',
        request_serializer=ServerUserService__pb2.FindOneUserRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.searchForBM = channel.unary_unary(
        '/platformserver.ServerUserService/searchForBM',
        request_serializer=ServerUserService__pb2.SearchRequestForBM.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.resetPassword = channel.unary_unary(
        '/platformserver.ServerUserService/resetPassword',
        request_serializer=ServerUserService__pb2.ResetPasswordRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.associationRole = channel.unary_unary(
        '/platformserver.ServerUserService/associationRole',
        request_serializer=ServerUserService__pb2.AssociationRoleRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.unAssociationRole = channel.unary_unary(
        '/platformserver.ServerUserService/unAssociationRole',
        request_serializer=ServerUserService__pb2.UnAssociationRoleRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.switchSign = channel.unary_unary(
        '/platformserver.ServerUserService/switchSign',
        request_serializer=ServerUserService__pb2.SwitchSignRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.findRoles = channel.unary_unary(
        '/platformserver.ServerUserService/findRoles',
        request_serializer=ServerUserService__pb2.FindRolesRequest.SerializeToString,
        response_deserializer=ServerCommonMessage__pb2.Response.FromString,
        )
    self.listUserByCondition = channel.unary_unary(
        '/platformserver.ServerUserService/listUserByCondition',
        request_serializer=ServerUserService__pb2.RequestUserListByCondition.SerializeToString,
        response_deserializer=ServerUserService__pb2.ResponseUserListByCondition.FromString,
        )
    self.getUserById = channel.unary_unary(
        '/platformserver.ServerUserService/getUserById',
        request_serializer=ServerUserService__pb2.RequestUserById.SerializeToString,
        response_deserializer=ServerUserService__pb2.ResponseUserById.FromString,
        )


class ServerUserServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def save(self, request, context):
    """保存用户
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def update(self, request, context):
    """更新用户
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    """删除用户
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findOne(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def searchForBM(self, request, context):
    """查询用户
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def resetPassword(self, request, context):
    """用户重置密码
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def associationRole(self, request, context):
    """用户绑定角色
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def unAssociationRole(self, request, context):
    """用户解绑角色
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def switchSign(self, request, context):
    """账号的启用禁用
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findRoles(self, request, context):
    """查询用户的所有角色
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listUserByCondition(self, request, context):
    """根据角色名和用户名模糊查询用户列表  lb
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUserById(self, request, context):
    """根据id查询用户信息  lb
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServerUserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'save': grpc.unary_unary_rpc_method_handler(
          servicer.save,
          request_deserializer=ServerUserService__pb2.SaveRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=ServerUserService__pb2.UpdateRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=ServerUserService__pb2.DeleteRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'findOne': grpc.unary_unary_rpc_method_handler(
          servicer.findOne,
          request_deserializer=ServerUserService__pb2.FindOneUserRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'searchForBM': grpc.unary_unary_rpc_method_handler(
          servicer.searchForBM,
          request_deserializer=ServerUserService__pb2.SearchRequestForBM.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'resetPassword': grpc.unary_unary_rpc_method_handler(
          servicer.resetPassword,
          request_deserializer=ServerUserService__pb2.ResetPasswordRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'associationRole': grpc.unary_unary_rpc_method_handler(
          servicer.associationRole,
          request_deserializer=ServerUserService__pb2.AssociationRoleRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'unAssociationRole': grpc.unary_unary_rpc_method_handler(
          servicer.unAssociationRole,
          request_deserializer=ServerUserService__pb2.UnAssociationRoleRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'switchSign': grpc.unary_unary_rpc_method_handler(
          servicer.switchSign,
          request_deserializer=ServerUserService__pb2.SwitchSignRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'findRoles': grpc.unary_unary_rpc_method_handler(
          servicer.findRoles,
          request_deserializer=ServerUserService__pb2.FindRolesRequest.FromString,
          response_serializer=ServerCommonMessage__pb2.Response.SerializeToString,
      ),
      'listUserByCondition': grpc.unary_unary_rpc_method_handler(
          servicer.listUserByCondition,
          request_deserializer=ServerUserService__pb2.RequestUserListByCondition.FromString,
          response_serializer=ServerUserService__pb2.ResponseUserListByCondition.SerializeToString,
      ),
      'getUserById': grpc.unary_unary_rpc_method_handler(
          servicer.getUserById,
          request_deserializer=ServerUserService__pb2.RequestUserById.FromString,
          response_serializer=ServerUserService__pb2.ResponseUserById.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'platformserver.ServerUserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))