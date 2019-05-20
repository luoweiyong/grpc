#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/9 18:32
"""
import grpc
import yaml
import os
from google.protobuf import wrappers_pb2, empty_pb2
from protos.resourcecenter import RCSubjectService_pb2_grpc,RCSubjectService_pb2
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Subject(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCSubjectService_pb2_grpc.RCSubjectServiceStub(channel=self.conn)

    # 获取科目列表
    def listSubject(self):
        response = self.client.listSubject(empty_pb2.Empty())

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据学段获取科目列表
    def listSubjectByStage(self, value):
        response = self.client.listSubjectByStage(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    S= Subject()
    # result = S.listSubject()
    result = S.listSubjectByStage(value= 2)
    print(result)