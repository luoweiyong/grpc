#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/23 10:07
"""
import grpc
import yaml
import os
from protos.platformserver import ServerRoleService_pb2,ServerRoleService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Role(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = ServerRoleService_pb2_grpc.ServerRoleServiceStub(channel= self.conn)

    # 保存角色
    def save(self, name, type, privilegeId):
        response= self.client.save(ServerRoleService_pb2.RoleSaveRequest
                                   (name= name, type= type, privilegeId= privilegeId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 更新角色
    def update(self, id, type, name, privilegeId):
        response= self.client.update(ServerRoleService_pb2.RoleUpdateRequest
                                     (id= id, type= type, name= name, privilegeId= privilegeId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除角色
    def delete(self, id):
        response= self.client.delete(ServerRoleService_pb2.RoleDeleteRequest(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

    # 查询角色类型查询对应的所有的角色
    def findAllRoles(self, type):
        response= self.client.findAllRoles(ServerRoleService_pb2.FindAllRolesRequest(type= type))

        res = MessageToDict(response)
        # print(res)
        return res

    def queryRoles(self, roleId, privilegeId, type, pageNo, pageSize):
        response= self.client.queryRoles(ServerRoleService_pb2.RolesQueryRequest
                                         (roleId= roleId, privilegeId= privilegeId, type= type, pageNo= pageNo, pageSize= pageSize))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
        R= Role()
        # result= R.save(name= 'fake', type= 2, privilegeId= ['1', '2', '3'])
        # result= R.update(id= 31, type= 1, name= '德国', privilegeId= ['1'])
        # result= R.delete(id= 31)
        # result= R.findAllRoles(type= 1)
        result= R.queryRoles(roleId= 31, privilegeId= '1', type= 1, pageNo= 1, pageSize= 10)
        print(result)