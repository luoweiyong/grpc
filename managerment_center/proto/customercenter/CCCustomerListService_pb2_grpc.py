# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import CCCustomerListService_pb2 as CCCustomerListService__pb2
import proto.Common_pb2 as Common__pb2


class CustomerServiceStub(object):
  """///////////////////////////////service//////////////////////////////////////
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.searchCustomer = channel.unary_unary(
        '/customercenter.CustomerService/searchCustomer',
        request_serializer=CCCustomerListService__pb2.RequestCustomerSearch.SerializeToString,
        response_deserializer=CCCustomerListService__pb2.CustomerList.FromString,
        )
    self.insertCustomer = channel.unary_unary(
        '/customercenter.CustomerService/insertCustomer',
        request_serializer=CCCustomerListService__pb2.CustomerVo.SerializeToString,
        response_deserializer=CCCustomerListService__pb2.BooleanReply.FromString,
        )
    self.updateCustomer = channel.unary_unary(
        '/customercenter.CustomerService/updateCustomer',
        request_serializer=CCCustomerListService__pb2.CustomerVo.SerializeToString,
        response_deserializer=CCCustomerListService__pb2.BooleanReply.FromString,
        )
    self.deleteCustomer = channel.unary_unary(
        '/customercenter.CustomerService/deleteCustomer',
        request_serializer=CCCustomerListService__pb2.CustomerVo.SerializeToString,
        response_deserializer=CCCustomerListService__pb2.BooleanReply.FromString,
        )
    self.listBusinessInfoByCustomerId = channel.unary_unary(
        '/customercenter.CustomerService/listBusinessInfoByCustomerId',
        request_serializer=CCCustomerListService__pb2.RequestListBusinessInfo.SerializeToString,
        response_deserializer=CCCustomerListService__pb2.BusinessList.FromString,
        )
    self.updateBusinessStatus = channel.unary_unary(
        '/customercenter.CustomerService/updateBusinessStatus',
        request_serializer=CCCustomerListService__pb2.RequestupdateBusiness.SerializeToString,
        response_deserializer=CCCustomerListService__pb2.BooleanReply.FromString,
        )
    self.listSchoolingLength = channel.unary_unary(
        '/customercenter.CustomerService/listSchoolingLength',
        request_serializer=Common__pb2.RequestBMSubjectSchoolingLength.SerializeToString,
        response_deserializer=Common__pb2.BMSubjectResponseSchoolingLengthList.FromString,
        )


class CustomerServiceServicer(object):
  """///////////////////////////////service//////////////////////////////////////
  """

  def searchCustomer(self, request, context):
    """根据条件返回客户信息
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def insertCustomer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateCustomer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteCustomer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listBusinessInfoByCustomerId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateBusinessStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listSchoolingLength(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'searchCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.searchCustomer,
          request_deserializer=CCCustomerListService__pb2.RequestCustomerSearch.FromString,
          response_serializer=CCCustomerListService__pb2.CustomerList.SerializeToString,
      ),
      'insertCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.insertCustomer,
          request_deserializer=CCCustomerListService__pb2.CustomerVo.FromString,
          response_serializer=CCCustomerListService__pb2.BooleanReply.SerializeToString,
      ),
      'updateCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.updateCustomer,
          request_deserializer=CCCustomerListService__pb2.CustomerVo.FromString,
          response_serializer=CCCustomerListService__pb2.BooleanReply.SerializeToString,
      ),
      'deleteCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.deleteCustomer,
          request_deserializer=CCCustomerListService__pb2.CustomerVo.FromString,
          response_serializer=CCCustomerListService__pb2.BooleanReply.SerializeToString,
      ),
      'listBusinessInfoByCustomerId': grpc.unary_unary_rpc_method_handler(
          servicer.listBusinessInfoByCustomerId,
          request_deserializer=CCCustomerListService__pb2.RequestListBusinessInfo.FromString,
          response_serializer=CCCustomerListService__pb2.BusinessList.SerializeToString,
      ),
      'updateBusinessStatus': grpc.unary_unary_rpc_method_handler(
          servicer.updateBusinessStatus,
          request_deserializer=CCCustomerListService__pb2.RequestupdateBusiness.FromString,
          response_serializer=CCCustomerListService__pb2.BooleanReply.SerializeToString,
      ),
      'listSchoolingLength': grpc.unary_unary_rpc_method_handler(
          servicer.listSchoolingLength,
          request_deserializer=Common__pb2.RequestBMSubjectSchoolingLength.FromString,
          response_serializer=Common__pb2.BMSubjectResponseSchoolingLengthList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'customercenter.CustomerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))