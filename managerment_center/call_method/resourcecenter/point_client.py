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
from google.protobuf import wrappers_pb2
from protos.resourcecenter import RCPointService_pb2, RCPointService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Point(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCPointService_pb2_grpc.RCPointServiceStub(channel=self.conn)

    # 根据科目查知识点
    def listPointsBySubjectId(self, value):
        response = self.client.listPointsBySubjectId(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    # 新建知识点
    def createPoint(self, id, parentId, pointIndex, subjectId, pointName):
        response = self.client.createPoint(RCPointService_pb2.Point
                                           (id= id, parentId= parentId, pointIndex= pointIndex, subjectId= subjectId,
                                            pointName= pointName))
        res = MessageToDict(response)
        # print(res)
        return res

    # 修改知识点
    def updatePoint(self, id, pointName):
        response = self.client.updatePoint(RCPointService_pb2.Point(id= id, pointName= pointName))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除知识点
    def deletePoint(self, value):
        response = self.client.deletePoint(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    # 升级知识点
    def upGradePoint(self, value):
        response = self.client.upGradePoint(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    # 降级知识点
    def downGradePoint(self, value):
        response = self.client.downGradePoint(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    # 升序知识点
    def upOrderPoint(self, value):
        response = self.client.upOrderPoint(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res


    # 降序序知识点
    def downOrderPoint(self, value):
        response = self.client.downOrderPoint(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据多个章节id查询关联的知识点列表
    def listPointByChapterIds(self, chapterIds):
        response = self.client.listPointByChapterIds(RCPointService_pb2.ReqPointListByChapterIds(chapterIds= chapterIds))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据知识点id查知识点信息
    def getPointById(self, value):
        response = self.client.getPointById(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    P= Point()
    t1 = time.time()
    # result= P.listPointsBySubjectId(value= 317)
    # result= P.createPoint(id= None, parentId= 0, pointIndex= 1, subjectId= 317, pointName= '拥挤踩踏')
    # result= P.updatePoint(id= 4987, pointName= '1-1-1-4-改')
    # result= P.deletePoint(value= 4987)
    # result= P.upGradePoint(value= 4981)
    # result= P.downGradePoint(value= 4981)
    # result= P.upOrderPoint(value= 4987)
    # result= P.downOrderPoint(value= 4987)
    # result= P.listPointByChapterIds(chapterIds= [1,2])
    # result= P.getPointById(value= 1)
    print(time.time() - t1)
    print(result)