#! usr/bin/env python3
#-*- coding:utf-8 -*-
import unittest,grpc,RCEditionService_pb2,RCEditionService_pb2_grpc
from google.protobuf.json_format import MessageToDict
from readData import yamlRead
from google.protobuf import wrappers_pb2
from google.protobuf import empty_pb2
class RCEditionServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] +':' +yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.RCEditionServiceClient = RCEditionService_pb2_grpc.RCEditionServiceStub(channel=cls.conn)
    def test01_listEditionVersion(self):#条件查询教材版本.沪教版,人教版...,
        response = self.RCEditionServiceClient.listEditionVersion(RCEditionService_pb2.RequestEditionVersionList(#id=1,#主键id  非必填
                                                                                                                 #name = ''#名称模糊查询 非必填
                                                                                                                 ))
        res = MessageToDict(response)
        print(res)
    def test02_listEdition(self):#获取教材列表数据
        response = self.RCEditionServiceClient.listEdition(RCEditionService_pb2.RequestEditionList(pageNo=1,#  页码   从1开始
                                                                                                   pageSize=10,#  每页大小
                                                                                                #下面几个字段传0表示获取所有
                                                                                                   gradeId=None,#  年级
                                                                                                   editionVersionId=None,#  教材版本id,对应的是t_edition_version 表,教版,湘教版这样的
                                                                                                   subjectId=None,#  科目
                                                                                                   stageId=None))#学段
        res = MessageToDict(response)
        print(res)
    def test03_insertEdition(self):#新增教材
        response = self.RCEditionServiceClient.insertEdition(RCEditionService_pb2.RequestInsertEdition(stageId = 1,        #  学段id
                                                                                                        gradeId = 2,        #  年级id
                                                                                                        subjectId = 3,      #  科目id
                                                                                                        editionVersionId = 4,        #  教材版本id,对应的是t_edition_version 表,教版,湘教版这样的
                                                                                                        fascicleId = 5,     #  分册id
                                                                                                        coverUrl = 6,       #  封面地址
                                                                                                        gradeName = 7,      #  年级名
                                                                                                        editionVersionName = 8,   #  教材版本名,人教版,湘教版这样的
                                                                                                        datas = [{
                                                                                                            'id':1,
                                                                                                            'chapterName':'',
                                                                                                            'chapterIndex':2,
                                                                                                            'editionId':3,
                                                                                                            'parentId':4
                                                                                                        }]   #  章节列表
                                                                                                       ))
        res = MessageToDict(response)
        print(res)
    def test04_updateEdition(self):#修改教材
        response = self.RCEditionServiceClient.updateEdition(RCEditionService_pb2.RequestUpdateEdition( id=1,
                                                                                                        stageId = 1,        #  学段id
                                                                                                        gradeId = 2,        #  年级id
                                                                                                        subjectId = 3,      #  科目id
                                                                                                        editionVersionId = 4,        #  教材版本id,对应的是t_edition_version 表,教版,湘教版这样的
                                                                                                        fascicleId = 5,     #  分册id
                                                                                                        coverUrl = 6,       #  封面地址
                                                                                                        gradeName = 7,      #  年级名
                                                                                                        editionVersionName = 8,   #  教材版本名,人教版,湘教版这样的
                                                                                                        datas = [{
                                                                                                            'id':1,
                                                                                                            'chapterName':'',
                                                                                                            'chapterIndex':2,
                                                                                                            'editionId':3,
                                                                                                            'parentId':4
                                                                                                        }]   #  章节列表
                                                                                                        ))
        res = MessageToDict(response)
        print(res)
    def test05_deleteEdition(self):#删除教材
        response = self.RCEditionServiceClient.deleteEdition(RCEditionService_pb2.RequestDeleteEdition(id=1029))
        res = MessageToDict(response)
        print(res)
    def test06_listChapter(self):#获取某个教材的章节列表
        response = self.RCEditionServiceClient.listChapter(RCEditionService_pb2.RequestChapterList(editionId=1,#教材id,必传的哈
                                                                                                   parentId=2#非必填,传0或者不传则是获取一级节点
                                                                                                    ))
        res = MessageToDict(response)
        print(res)
    def test07_listEditionBySubject(self):#根据科目查教材版本
        response = self.RCEditionServiceClient.listEditionBySubject(wrappers_pb2.Int32Value(value = 201))
        res = MessageToDict(response)
        print(res)
    def test08_listGradeByEdition(self):#根据科目教材查年级
        response = self.RCEditionServiceClient.listGradeByEdition(RCEditionService_pb2.SubjectEditionReq(subjectId=201,#科目id
                                                                                                         editionVersionId=1#教材版本
                                                                                                         ))
        res = MessageToDict(response)
        print(res)
    def test09_listChapterByEdition(self):#根据科目教材年级查章节
        response = self.RCEditionServiceClient.listChapterByEdition(RCEditionService_pb2.EditionGradeReq(subjectId=1,
                                                                                                         editionVersionId=2,
                                                                                                         gradeId=3,
                                                                                                         fascicleId=4#上下学期
                                                                                                         ))
        res = MessageToDict(response)
        print(res)
    def test10_listPress(self):#获取出版社列表
        response = self.RCEditionServiceClient.listPress(empty_pb2.Empty())
        res = MessageToDict(response)
        print(res)
    def test11_manageEditionVersion(self):
        response = self.RCEditionServiceClient.manageEditionVersion(RCEditionService_pb2.EditionVersionVo(id=1,#主键id,新增不传,修改删除必传 int
                                                                                                         name=2,#string 简称
                                                                                                         detailName=3,#string 详细名称
                                                                                                         press=4,#string 出版社名称
                                                                                                         versionNum=5,#string 版次,2008年12第二版
                                                                                                         dataStatus=6,#int 1:正常，2：冻结，3：删除',    启用传1,禁用传2
                                                                                                         manageType=7#1表示新增,2表示删除,3表示修改,,增删改操作必传
                                                                                                         ))
        res = MessageToDict(response)
        print(res)
    def test12_listEditionVersionAA(self):
        response = self.RCEditionServiceClient.listEditionVersionAA(RCEditionService_pb2.RequestEditionVersionListAA(pageNo=1,
                                                                                                                     pageSize=10))
        res = MessageToDict(response)
        print(res)
if __name__ == '__main__':
    unittest.main()
