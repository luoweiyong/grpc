#! usr/bin/env python3
#-*- coding:utf-8 -*-
import grpc,unittest,RCSubjectService_pb2_grpc,RCSubjectService_pb2
from google.protobuf.json_format import MessageToDict
from readData import yamlRead
from google.protobuf import empty_pb2
from google.protobuf import wrappers_pb2
class RCSubjectServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' + yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.RCSubjectServiceClient = RCSubjectService_pb2_grpc.RCSubjectServiceStub(channel=cls.conn)
    def test01_listSubject(self):#查询所有科目
        response = self.RCSubjectServiceClient.listSubject(empty_pb2.Empty())
        res = MessageToDict(response)
        print(res)
    def test02_listSubjectByStage(self):#根据学段查询科目
        response = self.RCSubjectServiceClient.listSubjectByStage(wrappers_pb2.Int32Value(value = 1))
        res = MessageToDict(response)
        print(res)
if __name__ == '__mian__':
    unittest.main()