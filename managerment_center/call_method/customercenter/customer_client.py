#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/22 11:44
"""
import grpc
import yaml
import os
from protos.customercenter import CCCustomerListService_pb2,CCCustomerListService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Customer(object):

    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = CCCustomerListService_pb2_grpc.CustomerListServiceStub(channel= self.conn)

    # 查询客户信息
    def searchCustomer(self, keyWord, customerType, businessId, dataStatus, pageNo, pageSize):
        response= self.client.searchCustomer(
            CCCustomerListService_pb2.RequestCustomerSearch(keyWord= keyWord, customerType= customerType,
                                                            businessId= businessId,dataStatus= dataStatus,
                                                            pageNo= pageNo, pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

    # 新增客户信息
    def insertCustomer(self, customerName, customerType, stageType, streetName, addressId, logo, salesManagerId,
                       operationManagerId, customerOfficerName, customerOfficerMobile, customerLinkmanName,
                       customerLinkmanMobile, schoolingLengthId, comment):
        response = self.client.insertCustomer(
            CCCustomerListService_pb2.RequestCustomerInsert(customerName=customerName, customerType=customerType,
                                                 stageType=stageType, streetName= streetName,addressId= addressId,
                                                 logo=logo, salesManagerId=salesManagerId,
                                                 operationManagerId=operationManagerId,
                                                 customerOfficerName=customerOfficerName,
                                                 customerOfficerMobile=customerOfficerMobile,
                                                 customerLinkmanName=customerLinkmanName,
                                                 customerLinkmanMobile=customerLinkmanMobile,
                                                 schoolingLengthId=schoolingLengthId, comment=comment))
        res = MessageToDict(response)
        # print(res)
        return res


    # 编辑客户信息户
    def editCustomer(self, customerId):
        response = self.client.editCustomer(CCCustomerListService_pb2.RequestCustomerEdit(customerId= customerId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 更新客户信息
    def updateCustomer(self, customerName, customerType, stageType, streetName, addressId, logo, salesManagerId,
                       operationManagerId,customerOfficerName, customerOfficerMobile,customerLinkmanName,
                       customerLinkmanMobile, schoolingLengthId, comment, id, status):
        response = self.client.updateCustomer(
            CCCustomerListService_pb2.RequestCustomerUpdate(customerName=customerName, customerType=customerType,
                                                 stageType=stageType, streetName= streetName,addressId= addressId,
                                                 logo= logo, salesManagerId= salesManagerId,
                                                 operationManagerId= operationManagerId,
                                                 customerOfficerName= customerOfficerName,
                                                 customerOfficerMobile= customerOfficerMobile,
                                                 customerLinkmanName= customerLinkmanName,
                                                 customerLinkmanMobile= customerLinkmanMobile,
                                                 schoolingLengthId= schoolingLengthId,
                                                 comment= comment, id= id, status= status))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除客户信息
    def deleteCustomer(self, id):
        response = self.client.deleteCustomer(CCCustomerListService_pb2.RequestCustomerDelete(id=id))

        res = MessageToDict(response)
        # print(res)
        return res

    # 查询组织机构信息
    def listOrgani(self, organiId, pageNo, pageSize):
        response = self.client.listOrgani(CCCustomerListService_pb2.RequestListOrgani
                                          (organiId= organiId, pageNo= pageNo,pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

    # 查询组织机构信息
    def searchOrgani(self, rule, keyword):
        response = self.client.searchOrgani(CCCustomerListService_pb2.RequestSearchOrgani(rule= rule, keyword= keyword))

        res = MessageToDict(response)
        # print(res)
        return res

    # 新增组织机构信息
    def insertOrgani(self, name, pId, managerInfoMsg):
        response = self.client.listOrgani \
            (CCCustomerListService_pb2.RequestInsertOrgani(name= name, pId= pId, managerInfoMsg= managerInfoMsg))

        res = MessageToDict(response)
        # print(res)
        return res

    # 更新组织机构信息
    def updateOrgani(self, id, name, pId, managerInfoMsg):
        response = self.client.updateOrgani(CCCustomerListService_pb2.RequestUpdateOrgani
                                            (id= id, name= name, pId= pId, managerInfoMsg= managerInfoMsg))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除组织机构信息
    def deleteOrgani(self, id):
        response = self.client.deleteOrgani(CCCustomerListService_pb2.RequestDeleteOrgani(id= id))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据客户id更新业务状态
    def updateBusinessStatus(self, customerId, businessId, status):
        response = self.client.updateBusinessStatus(CCCustomerListService_pb2.RequestUpdateBusiness
                                                    (customerId= customerId, businessId= businessId, status= status))
        res = MessageToDict(response)
        # print(res)
        return res

    # 业务管理列表查询(根据客户id)
    def listBusinessInfo(self, customerId, pageNo, pageSize):
        response = self.client.listBusinessInfo(CCCustomerListService_pb2.RequestListBusinessInfo
                                                (customerId= customerId, pageNo= pageNo,  pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

    # 增加下属学校
    def addUnderLingSchool(self, customerId, underLingId):
        response = self.client.addUnderLingSchool(CCCustomerListService_pb2.RequestAddUnderLingSchool
                                                  (customerId= customerId, underLingId= underLingId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除下属学校
    def deleteUnderLingSchool(self, customerId, underLingId):
        response = self.client.deleteUnderLingSchool(CCCustomerListService_pb2.RequestDeleteUnderLingSchool
                                                  (customerId= customerId, underLingId= underLingId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 列出所有学校,任意值 建议0
    def listSchool(self, code):
        response = self.client.listSchool(CCCustomerListService_pb2.RequestListSchool(code= code))
        res = MessageToDict(response)
        # print(res)
        return res

    # 根据运营经理id,查询他的客户数量, 学校数量, 学校id数组,暂为基础管理中心提供
    def selectCustomerNumByIdParam(self, operationManagerId):
        response= self.client.selectCustomerNumByIdParam(
            CCCustomerListService_pb2.RequestSelectCustomerNumByIdParam(operationManagerId= operationManagerId))

        res = MessageToDict(response)
        # print(res)
        return res

    #根据运营经理id查询他所负责的所有学校名称(包括教育局，教育集团)及学校所属客户名称暂为基础管理中心提供
    def listSchoolByIdParam(self, operationManagerId):
        response = self.client.listSchoolByIdParam(
            CCCustomerListService_pb2.RequestListSchoolByIdParam(operationManagerId= operationManagerId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据运营经理id,查询他所负责的所有学校名称及学校所属客户名称,暂为基础管理中心提供
    def updateRelationByIdParam(self, operationManagerId, updateSchoolRelationMsg):
        response = self.client.updateRelationByIdParam(CCCustomerListService_pb2.RequestUpdateRelationByIdParam
                                                       (operationManagerId= operationManagerId,
                                                        updateSchoolRelationMsg= updateSchoolRelationMsg))
        res = MessageToDict(response)
        # print(res)
        return res

    # 根据运营经理id，多个学校id修改学校和运营经理的绑定关系   暂为基础管理中心提供
    def selectCustomerInfo(self, customerId):
        response = self.client.selectCustomerInfo\
            (CCCustomerListService_pb2.RequestSelectCustomerInfo(customerId= customerId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据客户类型查询客户列表   暂为用户中心提供
    def listCustomerByCustomerType(self, customerType):
        response = self.client.listCustomerByCustomerType(CCCustomerListService_pb2.RequestListCustomerByCustomerType
                                                          (customerType= customerType))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
        C= Customer()
        # result= C.searchCustomer(keyWord= '小学', customerType= 1, businessId= 1, dataStatus= 1, pageNo= 1, pageSize= 10)
        # result= C.insertCustomer(customerName= '1', customerType= 2, stageType= '3', streetName= '4', addressId= '5',
        #                          logo= '6', salesManagerId= '7',operationManagerId= '8', customerOfficerName= '9',
        #                          customerOfficerMobile= '10', customerLinkmanName= '11',customerLinkmanMobile= '12',
        #                          schoolingLengthId= 13, comment= '14')
        result= C.editCustomer(4403050161)
        # result = C.updateCustomer(customerName= '1', customerType= 2, stageType= '3', streetName= '4', addressId= '5',
        #                           logo= '6',salesManagerId= '7', operationManagerId= '8', customerOfficerName= '9',
        #                           customerOfficerMobile= '10', customerLinkmanName= '11', customerLinkmanMobile= '12',
        #                           schoolingLengthId= 13, comment= '14', id= 15, status= 16)
        # result= C.deleteCustomer(id= '1')
        # result= C.listOrgani(organiId= 1, pageNo= 1, pageSize= 10)
        # result= C.seachOrgani(rule= 1, keyword= '2')
        # result= C.insertOrgani(name= '1', pId= 2, managerInfoMsg= ['3'])
        # result= C.updateOrgani(id= 1, name= '2', pId= 3, managerInfoMsg= ['4'])
        # result= C.deleteOrgani(id= 1)
        # result= C.updateBusinessStatus(customerId= 1, businessId= 2, status= 3)
        # result= C.listBusinessInfo(customerId= 1, pageNo= 1, pageSize= 10)
        # result= C.addUnderLingSchool(customerId= 1, underLingId= 2)
        # result= C.deleteUnderLingSchool(customerId= 1, underLingId= 2)
        # result= C.listSchool(code= '1')
        # result= C.selectCustomerNumByIdParam(operationManagerId= '1')
        # result= C.listSchoolByIdParam(operationManagerId= '1')
        # result= C.updateRelationByIdParam(operationManagerId= '1', updateSchoolRelationMsg= ['2'])
        # result= C.selectCustomerInfo(customerId= '1')
        # result= C.listCustomerByCustomerType(customerType= 2)

        print(result)