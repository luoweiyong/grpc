#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/9 18:30
"""
import grpc
import yaml
import os
from google.protobuf import wrappers_pb2
from protos.resourcecenter import RCChapterPointRelationService_pb2, RCChapterPointRelationService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class ChapterPoint(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCChapterPointRelationService_pb2_grpc.RCChapterPointRelationServiceStub(channel= self.conn)

    # 根据章节查询知识点
    def listRelationsByChapterId(self, value):
        response= self.client.listRelationsByChapterId(wrappers_pb2.Int32Value(value= value))
        res = MessageToDict(response)
        # print(res)
        return res

    # 新建章节与知识点的关联
    def createRelation(self, values):
        response= self.client.createRelation(RCChapterPointRelationService_pb2.CPRelationCreateReq(values= values))

        res = MessageToDict(response)
        # print(res)
        return res

    # 删除章节与知识点的关联
    def deleteRelation(self, chapterId, pointId, pointName):
        response= self.client.deleteRelation(RCChapterPointRelationService_pb2.CPRelation
                                             (chapterId= chapterId, pointId= pointId, pointName= pointName))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    CP= ChapterPoint()
    # result= CP.listRelationsByChapterId(value= 2)
    # result= CP.createRelation([{'chapterId':2, 'pointId':20, 'pointName':'易读错的汉字'},
    #                            {'chapterId':2, 'pointId':21, 'pointName':'汉字读音'}])
    result= CP.deleteRelation(chapterId= 110, pointId= 12, pointName= None)
    print(result)