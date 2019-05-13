#! usr/bin/env python3
#-*- coding:utf-8 -*-
import ServerPrivilegeService_pb2,ServerPrivilegeService_pb2_grpc,unittest,grpc
from google.protobuf.json_format import MessageToDict
from readData import yamlRead
class ServerPrivilegeServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' +yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.ServerPrivilegeServiceClient = ServerPrivilegeService_pb2_grpc.ServerPrivilegeServiceStub(channel=cls.conn)
    def test01_save(self):
        response = self.ServerPrivilegeServiceClient.save(ServerPrivilegeService_pb2.PrivilegeSaveRequest(parentId = '3eb8aafa-59d2-11e9-aaba-525400a29c3d',#string
                                                                                                          code = 'wy001',#string
                                                                                                          name = '打开',#string
                                                                                                          systemCategory =1,#int
                                                                                                          type = 1,#int
                                                                                                          url = 'http://www.sohu'))#int
        res = MessageToDict(response)
        print(res)
    def test02_update(self):
        response = self.ServerPrivilegeServiceClient.update(ServerPrivilegeService_pb2.PrivilegeUpdateRequest(id ='4a3d12fb-5a8c-11e9-aaba-525400a29c3d',#string
                                                                                                          parentId = '59acf3bc-5a8b-11e9-aaba-525400a29c3d',#string
                                                                                                          code = 'wy003',#string
                                                                                                          name = '打开',#string
                                                                                                          moduleName = '112',#string
                                                                                                          systemCategory =2,#int
                                                                                                          type = 1,#int
                                                                                                          url = 'http://www'))#int
        res = MessageToDict(response)
        print(res)
    def test03_delete(self):
        response = self.ServerPrivilegeServiceClient.delete(ServerPrivilegeService_pb2.PrivilegeDeleteRequest(id='4a3d12fb-5a8c-11e9-aaba-525400a29c3d'))#string
        res = MessageToDict(response)
        print(res)
    def test04_findChild(self):
        response = self.ServerPrivilegeServiceClient.findChild(ServerPrivilegeService_pb2.FindChildRequest(systemId=1,#int 平台 1 授课端 2 教师端App 3 家长端 4
                                                                                                           parentid='df388c9e-64a0-11e9-aaba-525400a29c3d',#string 想获得最上层父类可以不传这个字段。获得所有子节点，就传父节点ID
                                                                                                           #parentName=''
                                                                                                           ))
        res = MessageToDict(response)
        print(res)
    def test05_findAll(self):#查询平台角色
        response = self.ServerPrivilegeServiceClient.findAll(ServerPrivilegeService_pb2.FindAllPrivilegeRequest(systemId='1',
                                                                                                                  #module='df388c9e-64a0-11e9-aaba-525400a29c3d',#权限id（权限管理表）
                                                                                                                  content='management',
                                                                                                                  pageNo=1,
                                                                                                                  pageSize=10))
        res = MessageToDict(response)
        print(res)
    def test06_findPrivilegeSelective(self):
        response = self.ServerPrivilegeServiceClient.findPrivilegeSelective(ServerPrivilegeService_pb2.FindPrivilegesRequest(#systemId=1,
                                                                                                                             #type=1
                                                                                                                             ))#为module_category
        res = MessageToDict(response)
        print(res)
    def test07_findOne(self):
        response = self.ServerPrivilegeServiceClient.findOne(ServerPrivilegeService_pb2.FindOneRequest(id='8eaff1c2-5a9a-11e9-aaba-525400a29c3d' #string
                                                                                                     ))
        res = MessageToDict(response)
        print(res)
if __name__ == '__main__':
    unittest.main()