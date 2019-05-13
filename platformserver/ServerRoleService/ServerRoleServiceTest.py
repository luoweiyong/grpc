#! usr/bin/env python3
#-*- coding:utf-8 -*-
import unittest,grpc,ServerRoleService_pb2,ServerRoleService_pb2_grpc
from readData import yamlRead
import collections
from google.protobuf.json_format import MessageToDict
class ServerRoleServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' + yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.ServerRoleServiceClient = ServerRoleService_pb2_grpc.ServerRoleServiceStub(channel=cls.conn)
    def test01_save(self):#保存角色
        response = self.ServerRoleServiceClient.save(ServerRoleService_pb2.RoleSaveRequest(name = 'wy001',#角色名称 必传 string
                                                                                           type = 2,#角色类型  必传    平台角色：1,客户角色：2,用户角色：3 int
                                                                                           privilegeId = ['39728cfe-5a9e-11e9-aaba-525400a29c3d']#绑定权限ID
                                                                                           ))
        res = MessageToDict(response)
        print(res)#10f60619-550f-11e9-8f53-525400a29c3d
    def test02_update(self):#更新角色
        response = self.ServerRoleServiceClient.update(ServerRoleService_pb2.RoleUpdateRequest(id = 108,  #必传  角色ID int
                                                                                               name='管理员2',# 角色名称 必传 string
                                                                                               #type = 1,  #角色类型  必传    平台角色：1,客户角色：2,用户角色：3 int
                                                                                               #privilegeId = ['39728cfe-5a9e-11e9-aaba-525400a29c3d']
                                                                                               ))#绑定权限ID
        res = MessageToDict(response)
        print(res)
    def test03_delete(self):#删除角色
        response = self.ServerRoleServiceClient.delete(ServerRoleService_pb2.RoleDeleteRequest(id = '100'))#必传  角色ID int
        res = MessageToDict(response)
        print(res)
    # def test04_search(self):#查询角色(还未做完接口)
    #     response = self.ServerRoleServiceClient.search(ServerRoleService_pb2.RoleSearchRequest(id = '78',#string
    #                                                                                            name = '',#string
    #                                                                                            type = ''))#int
    #     res = MessageToDict(response)
    #     print(res)
    def test05_findAllRoles(self):#查询角色类型查询对应的所有的角色
        response = self.ServerRoleServiceClient.findAllRoles(ServerRoleService_pb2.FindAllRolesRequest(type =1))
        # 角色类型 非必须（但是要单纯获得某种类型的角色，需要传） 平台角色：1,客户角色：2,用户角色：3
        res = MessageToDict(response)
        print(res)
    def test06_queryRoles(self):#查询角色权限详情
        response = self.ServerRoleServiceClient.queryRoles(ServerRoleService_pb2.RolesQueryRequest(#roleId=84,#角色id
                                                                                                   privilegeId='e1ac4c01-59dc-11e9-aaba-525400a29c3d',#权限ID
                                                                                                   type=1,#模块类别：菜单，按钮
                                                                                                   pageNo=1,
                                                                                                   pageSize=5))
        res = MessageToDict(response)
        print(res)
if __name__ == '__main__':
    unittest.main()