#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/1 13:53
"""
import grpc
import yaml
import os
from protos.customercenter import CustomerAnalysisService_pb2,CustomerAnalysisService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Analysis(object):

    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = CustomerAnalysisService_pb2_grpc.CustomerAnalysisServiceStub(channel= self.conn)

    # 统计客户数(实时统计本月数据)
    def countCustomer(self, countRule, type):
        response= self.client.countCustomer(CustomerAnalysisService_pb2.RequestCountCustomer
                                            (countRule= countRule, type= type))
        res = MessageToDict(response)
        # print(res)
        return res

    # 根据年份统计每月的客户数
    def countEachMonthCustomer(self, year):
        response= self.client.countEachMonthCustomer(CustomerAnalysisService_pb2.RequestCountEachMonthCustomer(year= year))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    A= Analysis()
    # result= A.countCustomer(countRule= 1, type= 2)
    result= A.countEachMonthCustomer(year= 2017)
    print(result)