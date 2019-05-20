#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/9 18:31
"""
import grpc
import yaml
import os
import time
from google.protobuf import wrappers_pb2, empty_pb2
from protos.resourcecenter import RCQuestionPropService_pb2, RCQuestionPropService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class QuestionProp(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCQuestionPropService_pb2_grpc.RCQuestionPropServiceStub(channel=self.conn)

    # 根据科目查询题目类型
    def listStylesBySubjectId(self, value):
        response = self.client.listStylesBySubjectId(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    # 查询能力层次
    def listAbility(self):
        response = self.client.listAbility(empty_pb2.Empty())

        res = MessageToDict(response)
        # print(res)
        return res

    # 查询难度系数
    def listHardDegree(self):
        response = self.client.listHardDegree(empty_pb2.Empty())

        res = MessageToDict(response)
        # print(res)
        return res

    # 查询概念题类
    def listConceptType(self):
        response = self.client.listConceptType(empty_pb2.Empty())

        res = MessageToDict(response)
        # print(res)
        return res

    # 查询试题来源
    def listSource(self):
        response = self.client.listSource(empty_pb2.Empty())

        res = MessageToDict(response)
        # print(res)
        return res

    # 查询练习题类
    def listExerciseType(self):
        response = self.client.listExerciseType(empty_pb2.Empty())

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据能力层次id查能力层次信息
    def getAbilityById(self, value):
        response = self.client.getAbilityById(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    QP = QuestionProp()
    t1 = time.time()
    # result = QP.listStylesBySubjectId(value= 101)
    result = QP.listAbility()
    # result = QP.listHardDegree()
    # result = QP.listConceptType()
    # result = QP.listSource()
    # result = QP.listExerciseType()
    # result = QP.getAbilityById(1)
    print(time.time() - t1)
    print(result)