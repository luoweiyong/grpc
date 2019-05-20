#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/9 18:30
"""
import grpc
import yaml
import os
from protos.resourcecenter import RCGradeService_pb2, RCGradeService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)


class Grade(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCGradeService_pb2_grpc.RCGradeServiceStub(channel=self.conn)

    # 查询年级列表
    def listGrade(self, stageId):
        response = self.client.listGrade(RCGradeService_pb2.RequestGradeList(stageId= stageId))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    G= Grade()
    result= G.listGrade(stageId= 2)
    print(result)