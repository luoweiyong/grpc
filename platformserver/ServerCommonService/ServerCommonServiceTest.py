#! usr/bin/env python3
#-*- coding:utf-8 -*-
import unittest,grpc,ServerCommonService_pb2,ServerCommonService_pb2_grpc,time
from readData import yamlRead
from readData import g_md5
from google.protobuf.json_format import MessageToDict
import hashlib,base64
class ServerCommonServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' +yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.ServerCommonServiceClient = ServerCommonService_pb2_grpc.ServerCommonServiceStub(channel=cls.conn)
        cls.pwd = g_md5.g_md5('13249061072','e10adc3949ba59abbe56e057f20f883e')
    def test01_login(self):
        response = self.ServerCommonServiceClient.login(ServerCommonService_pb2.LoginRequest(userId='13249061072',#用户的唯一标识  这里是电话号码
                                                                                             password=self.pwd,#密码md5(userId+时间戳+md5(真实密码))
                                                                                             token=str(int(time.time())),#时间戳
                                                                                             loginType=1,#登录分类（1密码 2手机验证码 3扫码）
                                                                                             loginSource=1#登录来源（1平台 2学校 3 Ios App 4 Andorid App 5授课端）
                                                                                             ))
        res = MessageToDict(response)
        print(res)
if __name__ == '__main__':
    unittest.main()