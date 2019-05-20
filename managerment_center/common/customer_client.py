#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/22 11:44
"""
import grpc
import yaml
from proto.customercenter import CCCustomerListService_pb2,CCCustomerListService_pb2_grpc
from google.protobuf.json_format import MessageToDict
from proto import Common_pb2

with open('../datas/url.yaml', 'r', encoding= 'utf-8') as file:
    datas= yaml.safe_load(file)
    # print(datas)

class Customer():

    def __init__(self):
        self.base_url = datas['environments']['dev']['HOST'] + ':' + datas['environments']['dev']['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = CCCustomerListService_pb2_grpc.CustomerServiceStub(channel= self.conn)

    def searchCustomer(self, keyWord, customerType, businessId, dataStatus, page_number, result_per_page):
        response= self.client.searchCustomer(
            CCCustomerListService_pb2.RequestCustomerSearch(keyWord= keyWord, customerType= customerType,
                                                            businessId= businessId,dataStatus= dataStatus,
                                                            page_number= page_number, result_per_page= result_per_page))
        result = MessageToDict(response)
        # print(result)
        return result

    def insertCustomer(self, id, customerName, customerType, stageType, organizationId, logo, salesManagerId,
                       salesManagerName,operationManagerId,customerOfficerName, customerOfficerMobile,
                       customerLinkmanName, customerLinkmanMobile, schoolingLengthId, dataStatus,
                       status, superiorId, superiorType, customerManagerId, streetName, comment, addressId):
        response = self.client.insertCustomer(
            CCCustomerListService_pb2.CustomerVo(id=id, customerName=customerName, customerType=customerType,
                                                 stageType=stageType, organizationId=organizationId, logo=logo,
                                                 salesManagerId=salesManagerId,
                                                 salesManagerName=salesManagerName,
                                                 operationManagerId=operationManagerId,
                                                 customerOfficerName=customerOfficerName,
                                                 customerOfficerMobile=customerOfficerMobile,
                                                 customerLinkmanName=customerLinkmanName,
                                                 customerLinkmanMobile=customerLinkmanMobile,
                                                 schoolingLengthId=schoolingLengthId, dataStatus=dataStatus,
                                                 status=status,
                                                 superiorId=superiorId, superiorType=superiorType,
                                                 customerManagerId=customerManagerId, streetName=streetName,
                                                 comment=comment, addressId=addressId))
        result = MessageToDict(response)
        # print(result)
        return result

    def updateCustomer(self,id, customerName, customerType, stageType, organizationId, logo, salesManagerId,
                       salesManagerName,operationManagerId,customerOfficerName, customerOfficerMobile,
                       customerLinkmanName, customerLinkmanMobile, schoolingLengthId, dataStatus,
                       status, superiorId, superiorType, customerManagerId, streetName, comment, addressId):
        response = self.client.updateCustomer(
            CCCustomerListService_pb2.CustomerVo(id=id, customerName=customerName, customerType=customerType,
                                                 stageType=stageType, organizationId=organizationId, logo=logo,
                                                 salesManagerId=salesManagerId,
                                                 salesManagerName=salesManagerName,
                                                 operationManagerId=operationManagerId,
                                                 customerOfficerName=customerOfficerName,
                                                 customerOfficerMobile=customerOfficerMobile,
                                                 customerLinkmanName=customerLinkmanName,
                                                 customerLinkmanMobile=customerLinkmanMobile,
                                                 schoolingLengthId=schoolingLengthId, dataStatus=dataStatus,
                                                 status=status,
                                                 superiorId=superiorId, superiorType=superiorType,
                                                 customerManagerId=customerManagerId, streetName=streetName,
                                                 comment=comment, addressId=addressId))

        result = MessageToDict(response)
        # print(result)
        return result

    def deleteCustomer(self, id, customerName, customerType, stageType, organizationId, logo, salesManagerId,
                       salesManagerName, operationManagerId,
                       customerOfficerName, customerOfficerMobile, customerLinkmanName, customerLinkmanMobile,
                       schoolingLengthId, dataStatus,
                       status, superiorId, superiorType, customerManagerId, streetName, comment, addressId):
        response = self.client.deleteCustomer(
            CCCustomerListService_pb2.CustomerVo(id=id, customerName=customerName, customerType=customerType,
                                                 stageType=stageType, organizationId=organizationId, logo=logo,
                                                 salesManagerId=salesManagerId,
                                                 salesManagerName=salesManagerName,
                                                 operationManagerId=operationManagerId,
                                                 customerOfficerName=customerOfficerName,
                                                 customerOfficerMobile=customerOfficerMobile,
                                                 customerLinkmanName=customerLinkmanName,
                                                 customerLinkmanMobile=customerLinkmanMobile,
                                                 schoolingLengthId=schoolingLengthId, dataStatus=dataStatus,
                                                 status=status,
                                                 superiorId=superiorId, superiorType=superiorType,
                                                 customerManagerId=customerManagerId, streetName=streetName,
                                                 comment=comment, addressId=addressId))

        result = MessageToDict(response)
        # print(result)
        return result

    def listBusinessInfoByCustomerId(self, customerId):
        response= self.client.listBusinessInfoByCustomerId(
            CCCustomerListService_pb2.RequestListBusinessInfo(customerId= customerId))

        result = MessageToDict(response)
        # print(result)
        return result

    def updateBusinessStatus(self, businessId, status):
        response = self.client.updateBusinessStatus(
            CCCustomerListService_pb2.RequestupdateBusiness(businessId= businessId, status= status))

        result = MessageToDict(response)
        # print(result)
        return result

    def listSchoolingLength(self, id):
        response = self.client.listSchoolingLength(Common_pb2.RequestBMSubjectSchoolingLength(id= id))

        result = MessageToDict(response)
        # print(result)
        return result

if __name__ == '__main__':
        C= Customer()
        result= C.listSchoolingLength('1')
        print(result)