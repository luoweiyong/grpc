#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/9 18:30
"""
import grpc
import yaml
import os
import json
import time
from google.protobuf import wrappers_pb2, empty_pb2
from resourcecenter import RCEditionService_pb2, RCEditionService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Edition(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCEditionService_pb2_grpc.RCEditionServiceStub(channel=self.conn)

    # 获取出版社列表
    def listPress(self):
        response = self.client.listPress(empty_pb2.Empty())

        res = MessageToDict(response)
        # print(res)
        return res

    # 增删改教材版本
    def manageEditionVersion(self, id, name, detailName, press, versionNum, dataStatus, manageType):
        response = self.client.manageEditionVersion(RCEditionService_pb2.EditionVersionVo
                                                    (id= id, name= name, detailName= detailName, press= press,
                                                     versionNum= versionNum, dataStatus= dataStatus,
                                                     manageType= manageType))
        res = MessageToDict(response)
        # print(res)
        return res

    # 分页查询教材版本列表
    def listEditionVersionAA(self, pageNo, pageSize,dataStatus,versionName,versionNum,subjectId,stage):
        response = self.client.listEditionVersionAA(RCEditionService_pb2.RequestEditionVersionListAA
                                                    (pageNo= pageNo, pageSize= pageSize,dataStatus=dataStatus,
                                                     versionName=versionName,versionNum=versionNum,subjectId=subjectId,stage=stage))
        res = MessageToDict(response)
        # print(res)
        return res

    # 条件查询教材版本.沪教版,人教版...
    def listEditionVersion(self, id, name):
        response = self.client.listEditionVersion(RCEditionService_pb2.RequestEditionVersionList(id= id, name= name))

        res = MessageToDict(response)
        # print(res)
        return res

    # 获取教材列表
    def listEdition(self, pageNo, pageSize, gradeId, editionVersionId, subjectId, stageId):
        response = self.client.listEdition(RCEditionService_pb2.RequestEditionList
                                           (pageNo= pageNo, pageSize= pageSize, gradeId= gradeId,
                                            editionVersionId= editionVersionId, subjectId= subjectId, stageId= stageId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 新增教材
    def insertEdition(self, stageId, gradeId, subjectId, editionVersionId, fascicleId, coverUrl, gradeName,
                      editionVersionName, chapterJson):
        response = self.client.insertEdition(RCEditionService_pb2.RequestInsertEdition
                                             (stageId= stageId, gradeId= gradeId, editionVersionId= editionVersionId,
                                              subjectId= subjectId, fascicleId= fascicleId, coverUrl= coverUrl,
                                              gradeName= gradeName, editionVersionName= editionVersionName,
                                              chapterJson= json.dumps(chapterJson)))
        res = MessageToDict(response)
        # print(res)
        return res

    # 修改教材
    def updateEdition(self, id, stageId, gradeId, subjectId, editionVersionId, fascicleId, coverUrl, gradeName,
                      editionVersionName, chapterJson):
        response = self.client.updateEdition(RCEditionService_pb2.RequestUpdateEdition
                                             (id= id, stageId= stageId, gradeId= gradeId,
                                              editionVersionId= editionVersionId, subjectId= subjectId,
                                              fascicleId= fascicleId, coverUrl= coverUrl,gradeName= gradeName,
                                              editionVersionName= editionVersionName,
                                              chapterJson= json.dumps(chapterJson)))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除教材
    def deleteEdition(self, id):
        response = self.client.deleteEdition(RCEditionService_pb2.RequestDeleteEdition(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

    # 获取某个教材的章节列表
    def listChapter(self, editionId, parentId):
        response = self.client.listChapter(RCEditionService_pb2.RequestChapterList(editionId= editionId, parentId= parentId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据科目查教材版本
    def listEditionBySubject(self, value):
        response = self.client.listEditionBySubject(wrappers_pb2.Int32Value(value= value))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据科目教材查年级
    def listGradeByEdition(self, subjectId, editionVersionId):
        response = self.client.listGradeByEdition(RCEditionService_pb2.SubjectEditionReq
                                                  (subjectId= subjectId, editionVersionId= editionVersionId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 根据科目教材年级查章节包含知识点(结果message StringValue)
    def listChapterByEdition(self, subjectId, editionVersionId, gradeId, fascicleId):
        response = self.client.listChapterByEdition(RCEditionService_pb2.EditionGradeReq
                                                    (subjectId= subjectId, editionVersionId= editionVersionId,
                                                     gradeId= gradeId, fascicleId= fascicleId))
        res = MessageToDict(response)
        # print(res)
        return res

    def listChapterNoPointByEdition(self, subjectId, editionVersionId, gradeId, fascicleId):
        response = self.client.listChapterNoPointByEdition(RCEditionService_pb2.EditionGradeReq
                                                    (subjectId= subjectId, editionVersionId= editionVersionId,
                                                     gradeId= gradeId, fascicleId= fascicleId))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    E = Edition()
    t1 = time.time()
    # result= E.listPress()
    # result= E.manageEditionVersion(id= 1, name= '2', detailName= '3', press= '4', versionNum= '5', dataStatus= 6,
    #                                manageType= 7)
    result= E.listEditionVersionAA(pageNo= 1,pageSize= 10,dataStatus=1,versionName='2',versionNum='1',subjectId=101,stage=None)
    # result= E.listEditionVersion(id= None, name= '')
    # result= E.listEdition(pageNo= 1, pageSize= 10, gradeId= None, editionVersionId= None, subjectId= 101, stageId= 1)
    # result= E.insertEdition(stageId= 2, gradeId= 3, subjectId= 4, editionVersionId= 5, fascicleId= 6,
    #                          coverUrl= '7', gradeName= '8', editionVersionName= '9', chapterJson=
    #                         {'id': 'p1', 'chapterName': '第3章 力学', 'editionId': 7, 'parentId': '0'})
    # result= E.updateEdition(id= 1021, stageId= 2, gradeId= 3, subjectId= 101, editionVersionId= 5, fascicleId= 2,
    #                          coverUrl= '7', gradeName= '8', editionVersionName= '9', chapterJson=
    #                          {'id': 'p1', 'chapterName': '第3章 力学', 'editionId': 7, 'parentId': '0'})
    # result= E.deleteEdition(id= 1020)
    """
    这个接口作用？
    """
    # result= E.listChapter(editionId= 9, parentId= -1)
    # result= E.listEditionBySubject(value= 201)
    # result= E.listGradeByEdition(subjectId= 102, editionVersionId= 1)
    # result= E.listChapterByEdition(subjectId= 117, editionVersionId= 1, gradeId= 13, fascicleId= 3)
    # result= E.listChapterNoPointByEdition(subjectId= 317, editionVersionId= 1, gradeId= 31, fascicleId= 3)
    print(time.time()-t1)
    print(result)