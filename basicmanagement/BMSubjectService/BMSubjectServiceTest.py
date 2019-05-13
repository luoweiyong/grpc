#-*- coding:utf-8 -*-
#! usr/bin/env python3
import BMSubjectService_pb2,BMSubjectService_pb2_grpc,grpc,unittest
from google.protobuf.json_format import MessageToDict
import Common_pb2
from readData import yamlRead
class BMSubjectServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' + yamlRead.yamlRead()['port']
        # print(cls.url)
        # cls.url = '192.168.15.191:9191'
        cls.conn = grpc.insecure_channel(cls.url)
        cls.BMSubjectServiceClient = BMSubjectService_pb2_grpc.BMSubjectServiceStub(channel=cls.conn)
    def test01_listSchoolingLength(self):#返回学制列表,id传个0吧
        #参数：string id
        respons = self.BMSubjectServiceClient.listSchoolingLength(Common_pb2.RequestBMSubjectSchoolingLength(id='0'))
        res = MessageToDict(respons)
        print(res)
    def test02_insertSubject(self):
        # 参数：int32   id = 1 ;
        #     string  code = 2;
        #     string  subjectName = 3;
        #     string  gradeRange = 4;     //  多个以,隔开------格式为   1,2,3,4
        #     string  stageId = 5;
        response = self.BMSubjectServiceClient.insertSubject(BMSubjectService_pb2.SubjectP(#id=1,
                                                                                           code='003',
                                                                                           subjectName='js',
                                                                                           gradeRange='7,8',
                                                                                           stageId='2'))
        res = MessageToDict(response)
        print(res)
    def test05_deleteSubject(self):
        # 参数：string id    可不传
        response = self.BMSubjectServiceClient.deleteSubject(BMSubjectService_pb2.RequestSubjectId(id='155'))

        res = MessageToDict(response)
        print(res)
    def test04_updateSubject(self):
        #参数：int32   id = 1 ;
            # string  code = 2;
            # string  subjectName = 3;
            # string  gradeRange = 4;     //  多个以,隔开------格式为   1,2,3,4
            # string  stageId
        response = self.BMSubjectServiceClient.updateSubject(BMSubjectService_pb2.SubjectP(id=1,
                                                                                           code='wy003',
                                                                                           subjectName='ps',
                                                                                           gradeRange='7,8,9',
                                                                                           stageId='1'))
        res = MessageToDict(response)
        print(res)
    def test03_listSubject(self):#查询科目数据,传0表示获取全部
        response = self.BMSubjectServiceClient.listSubject(BMSubjectService_pb2.RequestSubjectList(stageId=3))
        res = MessageToDict(response)
        print(res)


    def test06_listGrade(self):
        #参数：string stageId
        response = self.BMSubjectServiceClient.listGrade(BMSubjectService_pb2.RequestGradeList(stageId = '0'))
        # res = MessageToDict(response)
        # print(type(response))
        # self.assertEqual(res['msg'],u'成功',"断言失败")
        res = MessageToDict(response)
        print(res)
    def test07_listConfigData(self):
        response = self.BMSubjectServiceClient.listConfigData(BMSubjectService_pb2.RequestConfigDataList(id=3))
        res = MessageToDict(response)
        print(res)
    def test09_listEdition(self):
        response = self.BMSubjectServiceClient.listEdition(BMSubjectService_pb2.RequestEditionList(pageNo = 1,#页码
                                                                                                   pageSize = 10,
                                                                                                   gradeId = 1,
                                                                                                   pressId = 1,
                                                                                                   subjectId = 107,
                                                                                                   stageId = 1))
        res = MessageToDict(response)
        print(res)
    def test08_insertEdition(self):
        response = self.BMSubjectServiceClient.insertEdition(BMSubjectService_pb2.RequestInsertEdition(stageId = 1,
                                                                                                       gradeId = 1,
                                                                                                       subjectId = 107,
                                                                                                       pressId = 1,
                                                                                                       fascicleId =1,
                                                                                                       coverUrl = 'D:\图片和视频\荣誉.jpg',
                                                                                                       gradeName = '一年级',
                                                                                                       fascicleName = '上册',
                                                                                                       datas = [{'id':'039',
                                                                                                                 'chapterName':'力学3',
                                                                                                                 'chapterIndex':0,
                                                                                                                 'parentId':'0'}]))
        res = MessageToDict(response)
        print(res)
    def test10_updateEdition(self):
        response = self.BMSubjectServiceClient.updateEdition(BMSubjectService_pb2.RequestUpdateEdition(id = 63,
                                                                                                       stageId = 2,
                                                                                                       gradeId = 7,
                                                                                                       subjectId = 127,
                                                                                                       pressId = 1,
                                                                                                       fascicleId =2,
                                                                                                       coverUrl = 'D:\图片和视频\荣誉.jpg',
                                                                                                       gradeName = '七年级',
                                                                                                       fascicleName = 'v',
                                                                                                       datas = [{'id':'040',
                                                                                                                 'chapterName':'力学3',
                                                                                                                 'parentId':'0'}]))
        res = MessageToDict(response)
        print(res)
    def test11_deleteEdition(self):
        response = self.BMSubjectServiceClient.deleteEdition(BMSubjectService_pb2.RequestDeleteEdition(id=60))
        res = MessageToDict(response)
        print(res)
    def test12_listChapter(self):#根据教材版本获取某个教材的章节
        response = self.BMSubjectServiceClient.listChapter(BMSubjectService_pb2.RequestChapterList(editionId=93,
                                                                                                   parentId=''))
        res = MessageToDict(response)
        print(res)
    def test13_getConfigDataById(self):#根据typeId和categoryId查某条数据
        response = self.BMSubjectServiceClient.getConfigDataById(BMSubjectService_pb2.RequestConfigDataById(typeId=3,
                                                                                                            categoryId=1))
        res = MessageToDict(response)
        print(res)

if __name__ == '__main__':
    unittest.main()