#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/22 11:44
"""
import grpc
import yaml
import os
from protos.platformserver import ServerUserService_pb2,ServerUserService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class User(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = ServerUserService_pb2_grpc.ServerUserServiceStub(channel= self.conn)

    # 保存用户
    def save(self, username, mobile, customerId, customerType, userType, status, roleId):
        response= self.client.save(
            ServerUserService_pb2.SaveRequest(username= username, mobile= mobile,customerId= customerId,
                                              customerType=  customerType, userType= userType, status= status, roleId= roleId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 更新用户
    def update(self, id, username, mobile, customerId, customerType, status, roleId):
        response= self.client.update(ServerUserService_pb2.UpdateRequest(id= id, username= username, mobile= mobile,
                                                                         customerId= customerId,customerType= customerType,
                                                                         status= status, roleId= roleId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除用户
    def delete(self, id):
        response= self.client.delete(ServerUserService_pb2.DeleteRequest(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据用户ID查询用户
    def findOne(self, id):
        response= self.client.findOne(ServerUserService_pb2.FindOneUserRequest(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

    # 重置密码
    def resetPassword(self, id, password):
        response= self.client.resetPassword(ServerUserService_pb2.ResetPasswordRequest(id= id, password= password))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据角色名和用户名模糊查询用户列表
    def listUserByCondition(self, pageNo, pageSize, roleName, name):
        response= self.client.listUserByCondition(
            ServerUserService_pb2.RequestUserListByCondition(pageNo= pageNo,pageSize= pageSize, roleName= roleName,name= name))
        res = MessageToDict(response)
        # print(res)
        return res

    # 查询平台列表
    def searchPlatFormUser(self, roleId, content, pageNo, pageSize):
        response= self.client.searchPlatFormUser(ServerUserService_pb2.PlatformUserSearchRequest
                                                 (roleId= roleId, content= content, pageNo= pageNo, pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

    # 查询客户列表
    def searchCustomerUser(self, roleId, customerId, content, pageNo, pageSize):
        response= self.client.searchCustomerUser(ServerUserService_pb2.CustomerUserSearchRequest
                                                 (roleId= roleId, customerId= customerId,content= content,
                                                  pageNo= pageNo, pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

    # 运营经理,销售经理的关联查询(查询他的客户数,学校数,班级数,学生数)
    def listRoleUserData(self, pageNo, pageSize, roleName, name, roleType):
        response= self.client.listRoleUserData(ServerUserService_pb2.RequestUserListByCondition
                                                 (pageNo= pageNo, pageSize= pageSize, roleName= roleName, name= name,
                                                  roleType= roleType))
        res = MessageToDict(response)
        # print(res)
        return res

    # 查询某个运营经理的相关信息,他负责的学校,教师数,班级数,学生数
    def listOperationManagerData(self, id):
        response= self.client.listOperationManagerData(ServerUserService_pb2.RequestId(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
        U= User()
        # result= U.save(username= 'jack', mobile= '1388888888', customerId= 1, customerType= 1, userType= 1, status= 1,  roleId= [1])
        # result= U.update(id= '0234ce84-7930-4517-9686-a9d13c73ce5c', username= 'ryan', mobile= '1388888888',
        #                  customerId= 6, customerType= 1, status= 1, roleId= [1])
        # result= U.delete(id= '0234ce84-7930-4517-9686-a9d13c73ce5c')
        result= U.findOne(id= '069d5c8b34b611e9b4c200163e084fc1')
        # result= U.resetPassword(id= '0234ce84-7930-4517-9686-a9d13c73ce5c', password= '666')
        # result= U.listUserByCondition(pageNo= 1, pageSize= 10, roleName= '狗哥', name= '')
        # result= U.searchPlatFormUser(roleId= 1, content= '', pageNo= 1, pageSize= 10)
        # result= U.searchCustomerUser(roleId= 1, customerId= 1, content= '', pageNo= 1, pageSize= 10)
        print(result)