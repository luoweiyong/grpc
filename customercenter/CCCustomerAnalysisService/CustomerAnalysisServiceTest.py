#! usr/bin/env python3
#-*- coding:utf-8 -*-
import unittest,CustomerAnalysisService_pb2,CustomerAnalysisService_pb2_grpc,grpc
from readData import yamlRead
from google.protobuf.json_format import MessageToDict
class CustomerAnalysisServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' + yamlRead.yamlRead()['port']
        # print(cls.url)
        cls.conn = grpc.insecure_channel(cls.url)
        cls.CustomerAnalysisServiceClient = CustomerAnalysisService_pb2_grpc.CustomerAnalysisServiceStub(channel=cls.conn)
    def test01_countCustomer(self):#统计新增学校数
        response = self.CustomerAnalysisServiceClient.countCustomer(CustomerAnalysisService_pb2.RequestCountCustomer( #统计规则 1 根据月份 int
                                                                                                                     countRule=1,
                                                                                                                      # 类型   1伟东公司 2学校 3教育集团 4教育局 5 客户(所有客户)
                                                                                                                     type=1
                                                                                                                     ))
        res = MessageToDict(response)
        print(res)
    def test02_countEachMonthCustomer(self):#根据年份统计每月的客户数
        response = self.CustomerAnalysisServiceClient.countEachMonthCustomer(CustomerAnalysisService_pb2.RequestCountEachMonthCustomer(year=2019)) #年份
        res = MessageToDict(response)
        print(res)
if __name__ == '__main__':
    unittest.main()