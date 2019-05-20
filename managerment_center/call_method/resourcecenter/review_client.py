#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/28 17:27
"""
import grpc
import yaml
import os
from protos.resourcecenter import RCReviewService_pb2,RCReviewService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Review(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCReviewService_pb2_grpc.RCReviewServiceStub(channel=self.conn)

    # 提交审核
    def submitResource(self, id, resourceType, subjectId, customerId):
        response = self.client.submitResource(RCReviewService_pb2.Resource2ReviewReq
                                              (id= id, resourceType= resourceType, subjectId= subjectId,
                                               customerId= customerId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 审核资源
    def reviewResource(self, id, resourceType, subjectId, customerId, userId, remark, reviewStatus):
        response = self.client.reviewResource(RCReviewService_pb2.ReviewResourceReq
                                              (id= id, resourceType= resourceType, subjectId= subjectId,
                                               customerId= customerId, userId= userId, remark= remark,
                                               reviewStatus= reviewStatus))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    R= Review()
    # result = R.submitResource(id= '1', resourceType= 2, subjectId= 3, customerId= 4403051000)
    result = R.reviewResource(id= "3386b66ba187412ba09246f6e68977a4", resourceType= 10, subjectId= 101,
                              customerId= 4403050161, userId= '73754b91303d11e9a6cc525400a29c3d', remark= '审核通过',
                              reviewStatus= 1)
    print(result)