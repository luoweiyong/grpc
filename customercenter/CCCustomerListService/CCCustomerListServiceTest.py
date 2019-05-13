#! usr/bin/env python3
#-*- coding:utf-8 -*-
import grpc,CCCustomerListService_pb2,CCCustomerListService_pb2_grpc,unittest
from google.protobuf.json_format import MessageToDict
from readData import yamlRead
class CCCustomerListServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = yamlRead.yamlRead()['host'] + ':' + yamlRead.yamlRead()['port']
        cls.conn = grpc.insecure_channel(cls.url)
        cls.CCCustomerListServiceClient = CCCustomerListService_pb2_grpc.CustomerListServiceStub(channel=cls.conn)
    def test01_searchCustomer(self):
        response = self.CCCustomerListServiceClient.searchCustomer(CCCustomerListService_pb2.RequestCustomerSearch(#keyWord='伟东',#关键字
                                                                                                                   #customerType=0,#客户类型,1伟东公司2学校3教育集团4教育局'
                                                                                                                   #businessId=4,#业务id int
                                                                                                                   #customerId=4403050134,
                                                                                                                   #status=1,#状态
                                                                                                                   pageNo= 1,#第几页
                                                                                                                   pageSize= 10#每页的结果数
                                                                                                                   ))
        # print(response)
        res = MessageToDict(response)
        print(res)
    def test02_insertCustomer(self):
        response = self.CCCustomerListServiceClient.insertCustomer(CCCustomerListService_pb2.RequestCustomerInsert(
                                                                                                         customerName = '伟东005',#客户名称
                                                                                                         customerType =1,#客户类型
                                                                                                         #stageType = '2,3',#学段配置id，学段id,1小学,2初中,3高中
                                                                                                         logo = '深圳伟东云教育',#logo地址
                                                                                                         salesManagerId = '95ad9ade-541e-11e9-ad7f-525400a29c3d',#销售经理id
                                                                                                         operationManagerId = '95ad9ade-541e-11e9-ad7f-525400a29c3d',#运营经理id
                                                                                                         customerOfficerName = '小罗',#客户负责人姓名
                                                                                                         customerOfficerMobile = '15612345678',#客户负责人手机
                                                                                                         customerLinkmanName = '笑笑',#客户联系人姓名
                                                                                                         customerLinkmanMobile = '15712345678',#客户联系人电话
                                                                                                         schoolingLengthId = 1,#学制配置id
                                                                                                         streetName = '深圳后海1006号',#街道（镇）名称
                                                                                                         comment = '中山大学',#备注
                                                                                                         addressId = '110000' #行政地址id  区/县
                                                                                                                  ))
        res = MessageToDict(response)
        print(res)
    def test03_updateCustomer(self):
        response = self.CCCustomerListServiceClient.updateCustomer(CCCustomerListService_pb2.RequestCustomerUpdate(id = 1100001011,
                                                                                                                   customerName='伟东006',
                                                                                                                   # 客户名称
                                                                                                                   customerType=2,
                                                                                                                   # 客户类型
                                                                                                                   stageType='1',
                                                                                                                   # 学段配置id
                                                                                                                   logo='深圳伟东云教育',
                                                                                                                   # logo地址
                                                                                                                   salesManagerId='ad9ade-541e-11e9-ad7f-525400a29c3d',
                                                                                                                   # 销售经理id
                                                                                                                   operationManagerId='d9ade-541e-11e9-ad7f-525400a29c3d',
                                                                                                                   # 运营经理id
                                                                                                                   customerOfficerName='罗',
                                                                                                                   # 客户负责人姓名
                                                                                                                   customerOfficerMobile='13512345678',
                                                                                                                   # 客户负责人手机
                                                                                                                   customerLinkmanName='小小',
                                                                                                                   # 客户联系人姓名
                                                                                                                   customerLinkmanMobile='15722345678',
                                                                                                                   # 客户联系人电话
                                                                                                                   schoolingLengthId=2,
                                                                                                                   # 学制配置id
                                                                                                                   streetName= '深',
                                                                                                                   # 街道（镇）名称
                                                                                                                   comment='21',
                                                                                                                   # 备注
                                                                                                                   addressId='11001'
                                                                                                                   # 行政地址id  区/县
                                                                                                                   ))
                                                                                                                   # 账号状态
        res = MessageToDict(response)
        print(res)
    def test04_deleteCustomer(self):
        response = self.CCCustomerListServiceClient.deleteCustomer(CCCustomerListService_pb2.RequestCustomerDelete(id = 12))
        res =MessageToDict(response)
        print(res)
    def test05_listOrgani(self):#组织机构列表查询
        response = self.CCCustomerListServiceClient.listOrgani(CCCustomerListService_pb2.RequestListOrgani(#organiId=10
                                                                                                           ))#组织机构id int
        res = MessageToDict(response)
        print(res)
    def test06_insertOrgani(self):#新增组织机构
        response = self.CCCustomerListServiceClient.insertOrgani(CCCustomerListService_pb2.RequestInsertOrgani(name='湖人区',#名称
                                                                                                               pId=6,#父组织id
                                                                                                               #组织机构管理员信息
                                                                                                               managerInfoMsg=[{
                                                                                                                   'managerId':'1e6db77c-6592-11e9-bc0d-525400a29c3d'#管理员ID
                                                                                                               }]))
        res = MessageToDict(response)
        print(res)
    def test07_searchOrgani(self):
        response = self.CCCustomerListServiceClient.searchOrgani(CCCustomerListService_pb2.RequestSearchOrgani(rule = 1,#1 搜索  2 选择
                                                                                                               #keyword = '深'#关键字
                                                                                                               ))

        res = MessageToDict(response)
        print(res)
    def test08_updateOrgani(self):#修改组织机构
        response = self.CCCustomerListServiceClient.updateOrgani(CCCustomerListService_pb2.RequestUpdateOrgani(id=11,
                                                                                                               name='南京市n',#名称
                                                                                                               pId=0,#父组织id
                                                                                                               #组织机构管理员信息
                                                                                                               managerInfoMsg=[{
                                                                                                                   'managerId':'fbf9713a-5b42-11e9-aaba-525400a29c3d'#管理员ID
                                                                                                               }]))
        res = MessageToDict(response)
        print(res)
    def test09_deleteOrgani(self):#删除组织机构
        response = self.CCCustomerListServiceClient.deleteOrgani(CCCustomerListService_pb2.RequestDeleteOrgani(id=15))
        res = MessageToDict(response)
        print(res)
    def test10_updateBusinessStatus(self):#根据客户id更新业务状态
        response = self.CCCustomerListServiceClient.updateBusinessStatus(CCCustomerListService_pb2.RequestUpdateBusiness(customerId=4,#客户id int
                                                                                                                         businessId=1,#业务id int
                                                                                                                         #（businessId为表t_bussiness_manage_rela_customer
                                                                                                                         # 中的bussiness_type_id）
                                                                                                                         status=2#1 开  2关 int
                                                                                                                         ))
        res = MessageToDict(response)
        print(res)
    def test11_listBusinessInfo(self):#业务管理列表查询(根据客户id)
        response = self.CCCustomerListServiceClient.listBusinessInfo(CCCustomerListService_pb2.RequestListBusinessInfo(#customerId=4
                                                                                                                       )) #客户id int
        res = MessageToDict(response)#查询t_business_manage_rela_customer  t_customer_center_config这两张表
        print(res)
    def test12_addUnderLingSchool(self):#增加下属学校
        response = self.CCCustomerListServiceClient.addUnderLingSchool(CCCustomerListService_pb2.RequestAddUnderLingSchool(customerId=7, #客户id int
                                                                                                                           underLingId=8 #下属学校id int
                                                                                                                           ))
        res = MessageToDict(response)
        print(res)
    def test13_deleteUnderLingSchool(self):#删除下属学校
        response = self.CCCustomerListServiceClient.deleteUnderLingSchool(CCCustomerListService_pb2.RequestDeleteUnderLingSchool(customerId=6,#客户id int
                                                                                                                           underLingId=8))#下属学校id int
        res = MessageToDict(response)
        print(res)
    def test14_listSchool(self):#列出所有学校
        response = self.CCCustomerListServiceClient.listSchool(CCCustomerListService_pb2.RequestListSchool(code='0'))
        res = MessageToDict(response)
        print(res)
    def test15_selectCustomerNumByIdParam(self):#根据运营经理id  查询他的客户数量,学校数量,学校id数组   暂为基础管理中心提供
        response = self.CCCustomerListServiceClient.selectCustomerNumByIdParam(CCCustomerListService_pb2.RequestSelectCustomerNumByIdParam(
                                                                                                                    #运营经理id
                                                                                                                    operationManagerId='db556091-6a2a-4d93-88b9-4c7c56c7f500'))
        res = MessageToDict(response)
        print(res)
    def test16_listSchoolByIdParam(self):#根据运营经理id  查询他所负责的所有学校名称及学校所属客户名称   暂为基础管理中心提供
        response = self.CCCustomerListServiceClient.listSchoolByIdParam(CCCustomerListService_pb2.RequestListSchoolByIdParam(
                                                                                                                    #运营经理id
                                                                                                                    operationManagerId='d9ade-541e-11e9-ad7f-525400a29c3d'))
        res = MessageToDict(response)
        print(res)
    def test17_updateRelationByIdParam(self):#根据运营经理id，多个学校id修改学校和运营经理的绑定关系   暂为基础管理中心提供
        response = self.CCCustomerListServiceClient.updateRelationByIdParam(CCCustomerListService_pb2.RequestUpdateRelationByIdParam(
                                                                                                                    # 运营经理id
                                                                                                                    operationManagerId='db556091-6a2a-4d93-88b9-4c7c56c7f500',
                                                                                                                    updateSchoolRelationMsg=[{
                                                                                                                        'schoolId':11,#学校id int
                                                                                                                        # 运营经理id
                                                                                                                        'newOperationManagerId':'0234ce84-7930-4517-9686-a9d13c73ce5c'
                                                                                                                    }]))
        res = MessageToDict(response)
        print(res)
    def test18_selectCustomerInfo(self):#根据客户id查询客户名称以及客户权限(教育局，教育集团下属学校数)  暂为用户中心提供（查询下属学校数量）
        response = self.CCCustomerListServiceClient.selectCustomerInfo(CCCustomerListService_pb2.RequestSelectCustomerInfo(#客户id string
                                                                                                                            customerId='4403050134'
                                                                                                                           ))
        res = MessageToDict(response)
        print(res)
    def test19_listCustomerByCustomerType(self):#根据客户类型查询客户列表   暂为用户中心提供
        response = self.CCCustomerListServiceClient.listCustomerByCustomerType(CCCustomerListService_pb2.RequestListCustomerByCustomerType(
                                                                                                                    #客户类型  1伟东公司 2学校 3教育集团 4教育局 5所有客户 int
                                                                                                                        customerType = 5
                                                                                                                                    ))
        res = MessageToDict(response)
        print(res)
    def test20_editCustomer(self):
        response = self.CCCustomerListServiceClient.editCustomer(CCCustomerListService_pb2.RequestCustomerEdit(customerId=4403050134))
        res = MessageToDict(response)
        print(res)
    def test21_editOrgani(self):
        response = self.CCCustomerListServiceClient.editOrgani(CCCustomerListService_pb2.RequestEditOrgani(organiId=1))
        res = MessageToDict(response)
        print(res)
    def test22_listCommonConfig(self):
        response = self.CCCustomerListServiceClient.listCommonConfig(CCCustomerListService_pb2.RequestCommonConfig(categoryId=2#类别id  1、客户类别 2、区域类别 3、区域等级 4、业务类别
                                                                                                                   ))
        res = MessageToDict(response)
        print(res)
    def test23_listUnderLingSchoolAllInfo(self):#根据客户id查询下属学校的信息
        response = self.CCCustomerListServiceClient.listUnderLingSchoolAllInfo(CCCustomerListService_pb2.RequestListUnderLingSchoolAllInfo(customerId=1102282000#int
                                                                                                                                           ))
        res = MessageToDict(response)
        print(res)
    def test24_listPcustomer(self):#根据客户id返回上级客户信息
        response = self.CCCustomerListServiceClient.listPcustomer(CCCustomerListService_pb2.RequestListPcustomer(customerId=1202230000#int
                                                                                                                 ))
        res = MessageToDict(response)
        print(res)
    def test25_listUnderLingSchool(self):#根据客户id返回下属学校数量(教育局,教育集团)
        response = self.CCCustomerListServiceClient.listUnderLingSchool(CCCustomerListService_pb2.RequestListUnderLingSchool(customerId=1201023000#int
                                                                                                                             ))
        res = MessageToDict(response)
        print(res)
    def test26_fuzzyQueryCustomer(self):#根据用户输入的学校名   模糊查询学校信息(id,学校名)
        response = self.CCCustomerListServiceClient.fuzzyQueryCustomer(CCCustomerListService_pb2.RequestFuzzyQueryCustomer(#keyWord='wy',#关键字 str
                                                                                                                           #customerId=1202230000,#int
                                                                                                                           customerType=2#int
                                                                                                                           ))
        res = MessageToDict(response)
        print(res)

if __name__ == '__main__':
    unittest.main()