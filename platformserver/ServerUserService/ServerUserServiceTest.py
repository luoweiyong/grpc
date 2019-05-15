#! usr/bin/env python3
#-*- coding:utf-8 -*-
import ServerUserService_pb2_grpc,ServerUserService_pb2,unittest,grpc
from readData import yamlRead
from google.protobuf.json_format import MessageToDict
class ServerUserServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ":" + yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.ServerUserServiceClient = ServerUserService_pb2_grpc.ServerUserServiceStub(channel=cls.conn)
    def test01_save(self): #保存用户
        response = self.ServerUserServiceClient.save(ServerUserService_pb2.SaveRequest( username = 'pt003',#用戶名 必传
                                                                                        # 电话 必传
                                                                                         mobile = '18912345678',
                                                                                        # 新增平台用户可传可不传  新增客户用户必传  默认 伟东公司  1
                                                                                         customerId = 6211241298,
                                                                                        # 新增平台用户可传可不传  新增客户用户必传 1伟东公司，2学校，3教育集团，4教育局
                                                                                        #  customerType = 2,
                                                                                        #必传  平台用户传1，客户用户传2，用户传3
                                                                                         userType = 2,
                                                                                        #必传  启用传1  禁用传0
                                                                                         status = 1,
                                                                                         # stage_type = 1,
                                                                                        #角色ID 必传
                                                                                         roleId = [83]))
        res = MessageToDict(response)
        print(res)
    def test02_update(self):#更新用户
        response = self.ServerUserServiceClient.update(ServerUserService_pb2.UpdateRequest( id = '6768e10d-656e-11e9-bc0d-525400a29c3d', #用户ID  必传
                                                                                            #用户名 必传
                                                                                             username = '销售003_1',
                                                                                            #电话 必传
                                                                                             mobile = '18912345678',
                                                                                            #客户ID
                                                                                             customerId = 6211241298,
                                                                                             #customeType=2,
                                                                                            status=1,
                                                                                             roleId = [83]))
        res = MessageToDict(response)
        print(res)
    def test03_delete(self):#删除用户
        response = self.ServerUserServiceClient.delete(ServerUserService_pb2.DeleteRequest(id='236a1f86-5b3c-11e9-aaba-525400a29c3d'))
        res = MessageToDict(response)
        print(res)
    def test04_findOne(self):#查询用户
        response = self.ServerUserServiceClient.findOne(ServerUserService_pb2.FindOneUserRequest(id='73754b91303d11e9a6cc525400a29c3d'))
        res = MessageToDict(response)
        print(res)
    def test05_resetPassword(self):#用户重置密码
        response = self.ServerUserServiceClient.resetPassword(ServerUserService_pb2.ResetPasswordRequest(id='0a79c0bf-5b38-11e9-aaba-525400a29c3d',
                                                                                                         password='123456'))
        res = MessageToDict(response)
        print(res)
    def test06_listUserByCondition(self):#根据角色名和用户名模糊查询用户列表
        response = self.ServerUserServiceClient.listUserByCondition(ServerUserService_pb2.RequestUserListByCondition(#pageNo = 1, # 页码   从1开始
                                                                                                                     #pageSize = 10,# 每页大小
                                                                                                                     roleName = '运营',# 角色名
                                                                                                                     #name = '运营', #用户名
                                                                                                                     #roleType=1
                                                                                                                     ))
        res = MessageToDict(response)
        print(res)
    def test07_searchPlatFormUser(self):#查询平台列表
        response = self.ServerUserServiceClient.searchPlatFormUser(ServerUserService_pb2.PlatformUserSearchRequest(roleId=144,
                                                                                                                   #content='15912345679',
                                                                                                                   pageNo=1,
                                                                                                                   pageSize=10))
        res = MessageToDict(response)
        print(res)
        # print("code是:%s"%(res['code']))
    def test08_searchCustomerUser(self):#查询客户列表
        response = self.ServerUserServiceClient.searchCustomerUser(ServerUserService_pb2.CustomerUserSearchRequest(#roleId=88,
                                                                                                                   #customerId=6211241296,
                                                                                                                   #content='2',
                                                                                                                   pageNo=1,
                                                                                                                   pageSize=20))
        res = MessageToDict(response)
        print(res)
    def test09_listOperationManagerData(self):
        response = self.ServerUserServiceClient.listOperationManagerData(ServerUserService_pb2.RequestId(id='4bca4954-658d-11e9-bc0d-525400a29c3d'))
        res = MessageToDict(response)
        print(res)
    def test10_listRoleUserData(self):#运营经理,销售经理的关联查询(查询他的客户数,学校数,班级数,学生数)
        #目前的需求是只查运营经理的,roleName传"运营",条件查询用户,所有字段都是可以不传,不传pageSize默认10
        response = self.ServerUserServiceClient.listRoleUserData(ServerUserService_pb2.RequestUserListByCondition(pageNo = 1, # 页码   从1开始
                                                                                                                     #pageSize = 10,# 每页大小
                                                                                                                     roleName = '运营',# 角色名
                                                                                                                     #name = '运营', #用户名
                                                                                                                     #roleType=2
                                                                                                                    ))
if __name__ == '__main__':
    unittest.main()
