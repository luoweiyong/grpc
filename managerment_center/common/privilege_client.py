#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/23 10:13
"""
import grpc
import yaml
from proto.platformserver import ServerPrivilegeService_pb2,ServerPrivilegeService_pb2_grpc
from google.protobuf.json_format import MessageToDict

with open('../datas/url.yaml', 'r', encoding= 'utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Privilege():
     # 根据条件返回学制列表
    def __init__(self):
        self.base_url = datas['my']['servers']['HOST'] + ':' + datas['my']['servers']['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = ServerPrivilegeService_pb2_grpc.ServerPrivilegeServiceStub(channel= self.conn)

    def save(self, parentId, code, name, moduleName, systemCategory, type, url, createUser):
        response= self.client.save(
            ServerPrivilegeService_pb2.PrivilegeSaveRequest(parentId= parentId, code= code, name= name,
                                                            moduleName= moduleName,systemCategory= systemCategory,
                                                            type= type, url= url, createUser=createUser))
        result = MessageToDict(response)
        # print(result)
        return result

    def update(self, id, parentId, code, name, moduleName, systemCategory, type, url, createUser):
        response= self.client.update(
            ServerPrivilegeService_pb2.PrivilegeUpdateRequest(id= id, nparentId= parentId, code= code, name= name,
                                                              moduleName= moduleName,systemCategory= systemCategory,
                                                              type= type, url= url, createUser=createUser))
        result = MessageToDict(response)
        # print(result)
        return result

    def delete(self, id):
        response= self.client.delete(ServerPrivilegeService_pb2.PrivilegeDeleteRequest(id= id))

        result = MessageToDict(response)
        # print(result)
        return result

if __name__ == '__main__':
        P= Privilege()