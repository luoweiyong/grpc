#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/5/9 16:58
"""
import grpc
import yaml
import os
from google.protobuf import empty_pb2
from protos.resourcecenterstatistic import RSstatistic_pb2,RSstatistic_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Statistic(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RSstatistic_pb2_grpc.RSstatisticServiceStub(channel=self.conn)

    # 获取资源使用次数
    def getResourceUseCount(self, resourceType, resourceId):
        response = self.client.getResourceUseCount(RSstatistic_pb2.ReqResourceUseCount
                                              (resourceType= resourceType, resourceId= resourceId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 增加资源使用记录
    def increaseResourceUseCount(self, statisticsType, resourceType, resourceId, userId, classId, customerId):
        response = self.client.increaseResourceUseCount(RSstatistic_pb2.ReqIncreaseResourceUseCount
                                              (statisticsType= statisticsType, resourceType= resourceType,
                                               resourceId= resourceId, userId= userId, classId= classId,
                                               customerId= customerId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 试题总量统计
    def getQuestionTotalCount(self):
        response = self.client.getQuestionTotalCount(empty_pb2.Empty())
        res = MessageToDict(response)
        # print(res)
        return res

    # 新增试题明细
    def listInsertQuestionDetail(self, pageNo, pageSize, startTime, endTime, name):
        response = self.client.listInsertQuestionDetail(RSstatistic_pb2.RequestInsertQuestionDetailList
                                                        (pageNo= pageNo, pageSize= pageSize, startTime= startTime,
                                                         endTime= endTime, name= name))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    S= Statistic()
    # result = S.getResourceUseCount(resourceType= 1, resourceId= '2')
    # result = S.increaseResourceUseCount(statisticsType= 1, resourceType= 2, resourceId= '3', userId= '4', classId= '5',
    #                                     customerId= 6)
    result = S.getQuestionTotalCount()
    # result = S.listInsertQuestionDetail(pageNo= 1, pageSize= 10, startTime= 20190501,endTime= 20190509, name= '')

    print(result)