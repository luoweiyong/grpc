#! usr/bin/env python3
#-*- coding:utf-8 -*-
import RSstatistic_pb2,RSstatistic_pb2_grpc,grpc,unittest
from google.protobuf.json_format import MessageToDict
from readData.yamlRead import yamlRead
from google.protobuf import empty_pb2
class RSstatisticTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead()['host'] + ':' + yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.RSstatisticTestClient = RSstatistic_pb2_grpc.RSstatisticServiceStub(channel=cls.conn)
    def test01_getResourceUseCount(self):#获取资源使用次数
        response = self.RSstatisticTestClient.getResourceUseCount(RSstatistic_pb2.ReqResourceUseCount(resourceType=10,#int 资源类型,1视频,2音频,3教案,4PPT,5学案,6图片,7包,8文本,9其他,10题,11课件
                                                                                                      resourceId='2e05cc5c-f483-4adf-a8d6-212d8ac186ee'#资源id
                                                                                                      ))
        res = MessageToDict(response)
        print(res)
    def test02_increaseResourceUseCount(self):#增加资源使用记录
        response = self.RSstatisticTestClient.increaseResourceUseCount(RSstatistic_pb2.ReqIncreaseResourceUseCount(statisticsType=1,#1表示一般使用统计,2表示上课统计
                                                                                                                   resourceType=10,
                                                                                                                   resourceId='2e05cc5c-f483-4adf-a8d6-212d8ac186ee',
                                                                                                                   userId='8ef029c1-6734-11e9-bc0d-525400a29c3d',#使用者id
                                                                                                                   classId='78',#使用的班级id     可不填
                                                                                                                   customerId=11#使用的客户id     可不填
                                                                                                                   ))
        res = MessageToDict(response)
        print(res)
    def test03_getQuestionTotalCount(self):#试题总量统计
        response = self.RSstatisticTestClient.getQuestionTotalCount(empty_pb2.Empty())
        res = MessageToDict(response)
        print(res)
    def test04_listInsertQuestionDetail(self):#新增试题明细
        response = self.RSstatisticTestClient.listInsertQuestionDetail(RSstatistic_pb2.RequestInsertQuestionDetailList(pageNo=1,
                                                                                                                       pageSize=2,
                                                                                                                       startTime=3,
                                                                                                                       endTime=4,
                                                                                                                       name=5#模糊查询
                                                                                                                       ))
        res = MessageToDict(response)
        print(res)