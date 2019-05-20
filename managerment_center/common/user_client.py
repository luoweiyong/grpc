#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/22 11:44
"""
import grpc
import yaml
from proto.platformserver import ServerUserService_pb2,ServerUserService_pb2_grpc
from google.protobuf.json_format import MessageToDict

with open('../datas/url.yaml', 'r', encoding= 'utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class User():
    def __init__(self):
        self.base_url = datas['my']['servers']['HOST'] + ':' + datas['my']['servers']['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = ServerUserService_pb2_grpc.ServerUserServiceStub(channel= self.conn)

    # 保存用户
    def save(self, username, sex, age, mobile, password, customerId, userPortrait, userType):
        response= self.client.save(
            ServerUserService_pb2.SaveRequest(username= username, sex= sex, age= age, mobile= mobile, password= password,
                                              customerId= customerId, userPortrait= userPortrait, userType= userType))
        result = MessageToDict(response)
        # print(result)
        return result

    # 更新用户
    def update(self, id, username, sex, age, mobile, password, customerId, userPortrait, status, dataStatus,userType):
        response= self.client.update(
            ServerUserService_pb2.UpdateRequest(id= id, username= username, sex= sex, age= age, mobile= mobile,
                                                password= password, customerId= customerId, userPortrait= userPortrait,
                                                status= status, dataStatus= dataStatus, userType= userType))
        result = MessageToDict(response)
        # print(result)
        return result

    # 删除用户
    def delete(self, id):
        response= self.client.delete(ServerUserService_pb2.DeleteRequest(id= id))

        result = MessageToDict(response)
        # print(result)
        return result

    def findOne(self, id):
        response= self.client.findOne(ServerUserService_pb2.FindOneUserRequest(id= id))

        result = MessageToDict(response)
        # print(result)
        return result

    # 查询用户
    def searchForBM(self, startPage, pageSize, userName, roleName):
        response= self.client.searchForBM(ServerUserService_pb2.SearchRequestForBM
                                     (startPage= startPage, pageSize= pageSize, userName= userName, roleName= roleName))

        result = MessageToDict(response)
        # print(result)
        return result

    # 用户重置密码
    def resetPassword(self, id, password):
        response= self.client.resetPassword(ServerUserService_pb2.ResetPasswordRequest(id= id, password= password))

        result = MessageToDict(response)
        print(result)
        return result

    # 用户绑定角色
    def AssociationRole(self, userId, roleId):
        response= self.client.associationRole(ServerUserService_pb2.AssociationRoleRequest
                                              (userId= userId, roleId= roleId))

        result = MessageToDict(response)
        # print(result)
        return result

    # 用户解绑角色
    def UnAssociationRole(self, id):
        response= self.client.unAssociationRole(ServerUserService_pb2.UnAssociationRoleRequest(id= id))

        result = MessageToDict(response)
        # print(result)
        return result

    # 账号的启用禁用
    def switchSign(self, id):
        response= self.client.switchSign(ServerUserService_pb2.SwitchSignRequest(id= id))

        result = MessageToDict(response)
        print(result)
        return result

    # 查询用户的所有角色
    def findRoles(self, username):
        response= self.client.findRoles(ServerUserService_pb2.FindRolesRequest(iusername= username))

        result = MessageToDict(response)
        # print(result)
        return result

    # 根据角色名和用户名模糊查询用户列表
    def listUserByCondition(self, pageNo, pageSize, roleName, name):
        response= self.client.listUserByCondition(
            ServerUserService_pb2.RequestUserListByCondition(pageNo= pageNo,pageSize= pageSize,
                                                             roleName= roleName,name= name))
        result = MessageToDict(response)
        # print(result)
        return result

    # 根据id查询用户信息
    def getUserById(self, userId):
        response= self.client.getUserById(ServerUserService_pb2.RequestUserById(userId= userId))

        result = MessageToDict(response)
        # print(result)
        return result

if __name__ == '__main__':
        U= User()
        # U.save('ryan',1, 1, '1', '1', 1, '1', 1)
        # U.update('f9073db6-6800-473c-a9b5-18b308bca492', 'ryan', 1, 32, '1388888888', '123456', 1, '1', 1, 1, 1)
        # U.resetPassword('5d233832-77ba-4a85-a2d5-ce078d0bb958', '666')