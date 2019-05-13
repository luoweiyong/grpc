#! usr/bin/env python3
#-*- coding:utf-8 -*-
import unittest,BMManagerService_pb2,BMManagerService_pb2_grpc,grpc
from readData import yamlRead
from google.protobuf.json_format import MessageToDict
class BMManagerServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' +yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.BMManagerServiceClient = BMManagerService_pb2_grpc.BMManagerServiceStub(channel=cls.conn)
    def test01_listRoleUserData(self):
        response = self.BMManagerServiceClient.listRoleUserData(BMManagerService_pb2.RequestRoleUserData(pageNo = 1,#int
                                                                                                         pageSize=10,#int
                                                                                                         roleName = '运营',#角色名，string
                                                                                                         #name = ''#用户名模糊查询   非必传
                                                                                                         ))
        res = MessageToDict(response)
        print(res)
    def test02_listOperationManagerData(self):
        response = self.BMManagerServiceClient.listOperationManagerData(BMManagerService_pb2.RequestId(id='cbe7e51a-5ab1-11e9-aaba-525400a29c3d'
                                                                                                       ))
        res = MessageToDict(response)
        print(res)
if __name__ == '__main__':
    unittest.main()