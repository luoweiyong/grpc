#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/19 9:29
"""
import grpc
import yaml
import os
from google.protobuf import wrappers_pb2
from protos.hbase import HBQuestionDataExtentionProto_pb2, HBQuestionDataExtentionProto_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class QuestionData(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = HBQuestionDataExtentionProto_pb2_grpc.HBQuestionDataExtentionServiceStub(channel=self.conn)

    # 向表中写数据
    def insertData(self, id, body, selection, answer, errorType, errorAnalysis):
        response = self.client.insertData(HBQuestionDataExtentionProto_pb2.QuestionDataExtention
                                          (id= id, body= body, selection= selection,answer= answer,errorType= errorType,
                                           errorAnalysis= errorAnalysis))
        res = MessageToDict(response)
        # print(res)
        return res

    #通过id查询表中的字段
    def queryDataByRowkey(self, value):
        response = self.client.queryDataByRowkey(wrappers_pb2.StringValue(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    #通过id删除表中的字段
    # def deleteByRowkey(self, value):
    #     response = self.client.deleteByRowkey(wrappers_pb2.StringValue(value= value))
    #
    #     res = MessageToDict(response)
    #     # print(res)
    #     return res

if __name__ == '__main__':
    QD = QuestionData()
    # result = QD.insertData(id= '2-2', body= '1', selection= '',answer= '', errorType= 'type', errorAnalysis= '', dataStatus= '')
    result = QD.queryDataByRowkey(value= '1_1')
    # result = QD.deleteByRowkey(value= '1_1')
    print(result)