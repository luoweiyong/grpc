#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/5/20 9:30
"""
import grpc
import yaml
import os
from resourcecenter import RCWorkOrderService_pb2,RCWorkOrderService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Workorder(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCWorkOrderService_pb2_grpc.RCWorkOrderServiceStub(channel=self.conn)

    # 工单查询
    def listWorkOrder(self, stageId, subjectId):
        response = self.client.listWorkOrder(RCWorkOrderService_pb2.RequestWorkOrder
                                             (stageId= stageId, subjectId= subjectId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 工单详情信息查询
    def listWorkOrderDetail(self, optId):
        response = self.client.listWorkOrderDetail(RCWorkOrderService_pb2.RequestWorkOrderDetail(optId= optId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 工单编辑
    def editWorkOrder(self, optId):
        response = self.client.editWorkOrder(RCWorkOrderService_pb2.RequestEditWorkOrder(optId=optId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 工单新增
    def saveWorkOrder(self, optId, versionNewId, versionOldId, handleStatus, workOrderChapters):
        response = self.client.saveWorkOrder(RCWorkOrderService_pb2.RequestWorkOrderSaveOrUpdate
                                             (optId=optId, versionNewId= versionNewId, versionOldId= versionOldId,
                                              handleStatus= handleStatus, workOrderChapters= workOrderChapters))
        res = MessageToDict(response)
        # print(res)
        return res

    # 工单更新
    def updateWorkOrder(self, optId, versionNewId, versionOldId, handleStatus, workOrderChapters):
        response = self.client.updateWorkOrder(RCWorkOrderService_pb2.RequestWorkOrderSaveOrUpdate
                                               (optId= optId, versionNewId= versionNewId, versionOldId= versionOldId,
                                                handleStatus= handleStatus, workOrderChapters= workOrderChapters))
        res = MessageToDict(response)
        # print(res)
        return res

    # 工单删除
    def deleteWorkOrder(self, optId, ):
        response = self.client.deleteWorkOrder(RCWorkOrderService_pb2.RequestWorkOrderDetail(optId=optId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 版本章节匹配
    def mateWorkOrder(self, versionNewId, versionOldId):
        response = self.client.mateWorkOrder(RCWorkOrderService_pb2.RequestWorkOrderDetail
                                             (versionNewId= versionNewId, versionOldId= versionOldId))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    W= Workorder()
    # result = W.listWorkOrder(stageId= 1, subjectId= 117)
    # result = W.listWorkOrderDetail(optId= 1)
    # result = W.editWorkOrder(optId= 3)
    result = W.saveWorkOrder(optId= 1, versionNewId= 2, versionOldId= 3, handleStatus= 4, workOrderChapters= [{}])
    # result = W.updateWorkOrder(optId= 1, versionNewId= 2, versionOldId= 3, handleStatus= 4, workOrderChapters= [])
    # result = W.deleteWorkOrder(optId= 1)
    # result = W.mateWorkOrder(versionNewId= 1, versionOldId= 2)
    print(result)