#! usr/bin/env python3
#-*- coding:utf-8 -*-
import CCCommonMessage_pb2,CCCommonMessage_pb2_grpc,grpc,unittest
from google.protobuf.json_format import MessageToDict
from readData import yamlRead
class CCCommonMessageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' + yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.CCCommonMessageClient = CCCommonMessage_pb2_grpc.CommonServiceStub(channel=cls.conn)
    def test01_listProvince(self):#返回省份列表
        response = self.CCCommonMessageClient.listProvince(CCCommonMessage_pb2.RequestListProvince(code = '1'))
        res = MessageToDict(response)
        print(res)
    def test02_listCity(self):#返回城市列表
        response = self.CCCommonMessageClient.listCity(CCCommonMessage_pb2.RequestListCity(provinceId = '1'))#省份id
        res = MessageToDict(response)
        print(res)
    def test03_listDistrict(self):#返回区/县列表
        reponse = self.CCCommonMessageClient.listDistrict(CCCommonMessage_pb2.RequestListDistrict(cityId = '1'))#城市ID
        res = MessageToDict(reponse)
        print(res)
if __name__ == '__main__':
    unittest.main()



