#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/13 14:31
"""
import grpc
import yaml
import os
from protos.resourcecenter import RCCoursewareService_pb2, RCCoursewareService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Courseware(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT1']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCCoursewareService_pb2_grpc.RCCoursewareServiceStub(channel= self.conn)

    # 新增课件
    def insertCourseware(self, teacherId, name, customerId, editionId, chapterIds, pointIds):
        response= self.client.insertCourseware(RCCoursewareService_pb2.ReqInsertCourseware
                                               (teacherId= teacherId, name= name, customerId= customerId,
                                                editionId=editionId, chapterIds= chapterIds, pointIds= pointIds))
        res = MessageToDict(response)
        # print(res)
        return res

    # 课件加精/取消加精
    def isJingCourseware(self, id, tag):
        response= self.client.isJingCourseware(RCCoursewareService_pb2.ReqCoursewareIsJing(id= id, tag= tag))

        res = MessageToDict(response)
        # print(res)
        return res

    # 新增课件的页
    def insertCoursewarePage(self, coursewareId, text, contentId, contentType, pageNum):
        response= self.client.insertCoursewarePage(RCCoursewareService_pb2.CoursewarePageVo
                                               (coursewareId= coursewareId, text= text, contentId= contentId,
                                                contentType= contentType, pageNum= pageNum))
        res = MessageToDict(response)
        # print(res)
        return res

    # 修改课件的页
    def updateCoursewarePage(self, coursewareId, text, contentId, contentType, pageNum):
        response= self.client.updateCoursewarePage(RCCoursewareService_pb2.CoursewarePageVo
                                               (coursewareId= coursewareId, text= text, contentId= contentId,
                                                contentType= contentType, pageNum= pageNum))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除课件的页.只传coursewareId,pageNum字段
    def deleteCoursewarePage(self, coursewareId, text, contentId, contentType, pageNum):
        response= self.client.deleteCoursewarePage(RCCoursewareService_pb2.CoursewarePageVo
                                               (coursewareId= coursewareId, text= text, contentId= contentId,
                                                contentType= contentType, pageNum= pageNum))
        res = MessageToDict(response)
        # print(res)
        return res

    # 条件查询课件列表
    def listCourseware(self, isBoutique, name, subjectId, editionVersionId, stageId, gradeId, fascicleId, orderType,
                       pageNo, pageSize):
        response= self.client.listCourseware(RCCoursewareService_pb2.ReqCoursewareList
                                               (isBoutique= isBoutique, name= name, subjectId= subjectId,
                                                editionVersionId= editionVersionId, stageId= stageId, gradeId= gradeId,
                                                fascicleId= fascicleId, orderType= orderType,pageNo=pageNo,
                                                pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    C= Courseware()
    # result= C.insertCourseware(teacherId= '1', name= '2', customerId= '3', subjectId= 4, editionId=5,
    #                            chapterIds= [6], pointIds= [7])
    # result= C.isJingCourseware(id= '1', tag= 2)
    # result= C.insertCoursewarePage(coursewareId= '1', text= '2', contentId= '3', contentType= 4, pageNum= 5)
    # result= C.updateCoursewarePage(coursewareId= '1', text= '2', contentId= '3', contentType= 4, pageNum= 5)
    # result= C.deleteCoursewarePage(coursewareId= '1', text= '2', contentId= '3', contentType= 4, pageNum= 5)
    result= C.listCourseware(isBoutique= 1, name= '2', subjectId= 3, editionVersionId= 4, stageId= 5, gradeId= 6,
                             fascicleId= 7, orderType= 8,pageNo=1, pageSize= 10)
    print(result)