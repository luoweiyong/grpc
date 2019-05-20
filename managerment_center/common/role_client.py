#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/23 10:07
"""
import grpc
import yaml
from proto.platformserver import ServerRoleService_pb2,ServerRoleService_pb2_grpc
from google.protobuf.json_format import MessageToDict

with open('../datas/url.yaml', 'r', encoding= 'utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Role():
    def __init__(self):
        self.base_url = datas['my']['servers']['HOST'] + ':' + datas['my']['servers']['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = ServerRoleService_pb2_grpc.ServerRoleServiceStub(channel= self.conn)
    # 保存角色
    def save(self, name, type):
        response= self.client.save(ServerRoleService_pb2.RoleSaveRequest(name= name, type= type))
        result = MessageToDict(response)
        # print(result)
        return result

    # 更新角色
    def update(self, id, name, type):
        response= self.client.update(ServerRoleService_pb2.RoleUpdateRequest(id= id, name= name, type= type))
        result = MessageToDict(response)
        # print(result)
        return result

    # 删除角色
    def delete(self, id):
        response= self.client.delete(ServerRoleService_pb2.RoleDeleteRequest(id= id))

        result = MessageToDict(response)
        # print(result)
        return result

    # 查询角色
    def search(self, id, name, type):
        response= self.client.search(ServerRoleService_pb2.RoleSearchRequest(id= id, name= name, type= type))

        result = MessageToDict(response)
        # print(result)
        return result

    # 关联权限
    def associationPrivilege(self, privilegeId, roleId):
        response= self.client.associationPrivilege(
            ServerRoleService_pb2.AssociationPrivilegeRequest(privilegeId= privilegeId, roleId= roleId))

        result = MessageToDict(response)
        # print(result)
        return result

    # 解除权限
    def unAssociationPrivilege(self, id):
        response= self.client.unAssociationPrivilege(ServerRoleService_pb2.UnAssociationPrivilegeRequest(id= id))

        result = MessageToDict(response)
        # print(result)
        return result

    # 查询角色类型查询对应的所有的角色
    def findAllRoles(self, type):
        response= self.client.findAllRoles(ServerRoleService_pb2.FindAllRolesRequest(type= type))

        result = MessageToDict(response)
        # print(result)
        return result

if __name__ == '__main__':
        R= Role()
        # R.save('fake', 2)
        R.update('6', '管理员', 2)