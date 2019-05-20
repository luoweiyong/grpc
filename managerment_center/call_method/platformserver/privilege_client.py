#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/23 10:13
"""
import grpc
import yaml
import os
from protos.platformserver import ServerPrivilegeService_pb2,ServerPrivilegeService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Privilege(object):
     # 根据条件返回学制列表
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = ServerPrivilegeService_pb2_grpc.ServerPrivilegeServiceStub(channel= self.conn)

    def save(self, parentId, code, name, moduleName, systemCategory, type, url, createUser):
        response= self.client.save(
            ServerPrivilegeService_pb2.PrivilegeSaveRequest(parentId= parentId, code= code, name= name,
                                                            moduleName= moduleName,systemCategory= systemCategory,
                                                            type= type, url= url, createUser=createUser))
        res = MessageToDict(response)
        # print(res)
        return res

    def update(self, id, parentId, code, name, moduleName, systemCategory, type, url, createUser):
        response= self.client.update(
            ServerPrivilegeService_pb2.PrivilegeUpdateRequest(id= id, nparentId= parentId, code= code, name= name,
                                                              moduleName= moduleName,systemCategory= systemCategory,
                                                              type= type, url= url, createUser= createUser))
        res = MessageToDict(response)
        # print(res)
        return res

    def delete(self, id):
        response= self.client.delete(ServerPrivilegeService_pb2.PrivilegeDeleteRequest(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

    def findChild(self, systemId, parentid, parentName):
        response= self.client.findChild(ServerPrivilegeService_pb2.FindChildRequest
                                        (systemId= systemId, parentid= parentid, parentName= parentName))
        res = MessageToDict(response)
        # print(res)
        return res

    def findAll(self, systemId, module, content, pageNo, pageSize):
        response= self.client.findAll(ServerPrivilegeService_pb2.FindAllPrivilegeRequest
                                        (systemId= systemId, module= module, content= content, pageNo= pageNo, pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

    def findPrivilegeSelective(self, systemId, type):
        response = self.client.findPrivilegeSelective(ServerPrivilegeService_pb2.FindPrivilegesRequest
                                    (systemId=systemId, type= type))
        res = MessageToDict(response)
        # print(res)
        return res

    def findOne(self, id):
        response = self.client.findOne(ServerPrivilegeService_pb2.FindOneRequest(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
        P= Privilege()
        # result= P.save(parentId= '1', code= '2', name= '3', moduleName= '4', systemCategory= 5, type= 6, url= '7', createUser= '9')
        # result= P.update(id= '1', parentId= '1', code= '2', name= '3', moduleName= '4', systemCategory= 5, type= 6,
        #                  url= '7', createUser= '9')
        # result= P.delete(id= '1')
        # result= P.findChild(systemId= 1, parentid= '2', parentName= '3')
        # result= P.findAll(systemId= 1, module= '2', content= '3', pageNo= 1, pageSize= 10)
        result= P.findPrivilegeSelective(systemId= 1, type= 2)
        # result= P.findOne(id= '1')
        print(result)