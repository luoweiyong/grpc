#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/21 17:47
"""
import grpc
import yaml
from proto.basicmanagement import BMSubjectService_pb2, BMSubjectService_pb2_grpc
from google.protobuf.json_format import MessageToDict
from proto import Common_pb2

with open('../datas/url.yaml', 'r', encoding= 'utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Subject():
    def __init__(self):
        self.base_url = datas['my']['servers']['HOST'] + ':' + datas['my']['servers']['PORT2']
        self.conn= grpc.insecure_channel(self.base_url)
        self.client= BMSubjectService_pb2_grpc.BMSubjectServiceStub(channel= self.conn)

    # 返回学制列表, id传个0吧
    def listSchoolingLength(self, id):
        response= self.client.listSchoolingLength(Common_pb2.RequestBMSubjectSchoolingLength(id= id))

        result= MessageToDict(response)
        # print(result)
        return result

    # 除id字段, 其他字段需全部赋值
    def insertSubject(self, id, code, subjectName, gradeRange, stageId):
        response= self.client.insertSubject(BMSubjectService_pb2.SubjectP
                                            (id= id, code= code, subjectName= subjectName,
                                             gradeRange= gradeRange, stageId= stageId))

        result= MessageToDict(response)
        # print(result)
        return result

    def deleteSubject(self, id):
        response= self.client.deleteSubject(BMSubjectService_pb2.RequestSubjectId(id= id))

        result= MessageToDict(response)
        # print(result)
        return result

    def updateSubject(self, id, code, subjectName, gradeRange, stageId):
        response= self.client.updateSubject(BMSubjectService_pb2.SubjectP
                                            (id= id, code= code, subjectName= subjectName,
                                             gradeRange= gradeRange, stageId= stageId))
        result= MessageToDict(response)
        print(result)
        return result

    # 查询科目数据, 传0表示获取全部
    def listSubject(self, id):
        response= self.client.listSubject(BMSubjectService_pb2.RequestSubjectId(id= id))

        result= MessageToDict(response)
        # print(result)
        return result

    # 根据学段查年级列表 学段id, 1 小学, 2 初中, 3高中, 传0则为获取所有年级
    def listGrade(self, stageId):
        response= self.client.listGrade(BMSubjectService_pb2.RequestGradeList(stageId = stageId))

        result= MessageToDict(response)
        # print(result)
        return result

    # 获取基础配置数据, 对应数据库t_basic_management_config表 id 1、学段类型 2、分册类型 3、出版社 ,传0则为获取所有
    def listConfigData(self, id):
        response= self.client.listConfigData(BMSubjectService_pb2.RequestConfigDataList(id=id))

        result= MessageToDict(response)
        # print(result)
        return result

    # 获取教材列表
    def listEdition(self, pageNo, pageSize, gradeId, pressId, subjectId, stageId):
        response= self.client.listEdition(
            BMSubjectService_pb2.RequestEditionList(pageNo= pageNo, pageSize= pageSize, gradeId= gradeId,
                                                    pressId= pressId, subjectId= subjectId, stageId= stageId))
        result= MessageToDict(response)
        # print(result)
        return result

    # 新增教材
    def insertEdition(self, stageId, gradeId, subjectId, pressId, fascicleId, coverUrl, gradeName, fascicleName, datas):
        response= self.client.insertEdition(
            BMSubjectService_pb2.RequestInsertEdition(stageId= stageId, gradeId= gradeId, subjectId= subjectId,
                                                      pressId= pressId, fascicleId= fascicleId, coverUrl= coverUrl,
                                                      gradeName= gradeName, fascicleName= fascicleName,
                                                      datas= datas))
        result= MessageToDict(response)
        # print(result)
        return  result

    # 修改教材
    def updateEdition(self, id, stageId, gradeId, subjectId, pressId, fascicleId, coverUrl, gradeName, fascicleName, datas):
        response = self.client.updateEdition(
            BMSubjectService_pb2.RequestUpdateEdition(id= id, stageId= stageId, gradeId= gradeId, subjectId= subjectId,
                                                      pressId= pressId, fascicleId= fascicleId, coverUrl= coverUrl,
                                                      gradeName= gradeName, fascicleName= fascicleName,
                                                      datas= datas))
        result= MessageToDict(response)
        # print(result)
        return result

    # 删除教材
    def deleteEdition(self):
        response= self.client.deleteEdition(BMSubjectService_pb2.RequestDeleteEdition(id=id))

        result= MessageToDict(response)
        # print(result)
        return result

    # 获取某个教材的章节列表
    def listChapter(self, editionId, parentId):
        response= self.client.listChapter(BMSubjectService_pb2.RequestChapterList(editionId= editionId, parentId= parentId))

        result= MessageToDict(response)
        # print(result)
        return result

    # 根据typeId和categoryId查某条数据 如根据学段id查询学段名
    def getConfigDataById(self, typeId, categoryId):
        response= self.client.getConfigDataById(
            BMSubjectService_pb2.RequestConfigDataById(typeId= typeId, categoryId= categoryId))

        result= MessageToDict(response)
        # print(result)
        return result

if __name__ == '__main__':
        S= Subject()
        result= S.listSchoolingLength('1')
        # S.insertSubject(0, '201', '初中化学', '7,8,9', '2')
        # S.deleteSubject('82')
        # result= S.listGrade('0')
        # result= S.listSubject('0')
        # print(result)
        # S.updateSubject(127,'110', '初中政治','7,8,9', '2')
        # result= S.listChapter(7, '0')
        # result= S.insertEdition(1, 3, 1, 1, 1, 'a.png', '三年级', '上册',
        #                         [{'id': 'p1', 'chapterName': '第3章 力学', 'editionId': 7, 'parentId': '0'},
        #                          {'id': 'p2', 'chapterName': '第4章 光学', 'chapterIndex': 1, 'editionId': 7, 'parentId': '0'}])
        print(result)