#! usr/bin/env python3
#-*- coding:utf-8 -*-
from locust import TaskSet,task,Locust,events
import grpc,time,os
from google.protobuf.json_format import MessageToDict
import BMSubjectService_pb2_grpc
import Common_pb2
from readData import yamlRead

class GrpcClient(object):
    def __init__(self):
        self.url = yamlRead.yamlRead()['host'] + ':' + yamlRead.yamlRead()['port']
        self.conn = grpc.insecure_channel(self.url)
        self.BMSubjectServiceClient = BMSubjectService_pb2_grpc.BMSubjectServiceStub(channel=self.conn)
    def conne(self):
        try:
            self.start_time = int(time.time())
            response = self.BMSubjectServiceClient.listSchoolingLength(Common_pb2.RequestBMSubjectSchoolingLength(id='0'))
            total_time = int((time.time() - self.start_time)*1000)
            self.res = MessageToDict(response)
            if self.res['code'] != 0:
                raise Exception
            events.request_success.fire(
                request_type='grpc',
                name='listSchoolingLength',
                response_time=total_time
            )
        except Exception as e:
            total_time = int((time.time() - self.start_time) * 1000)
            events.request_failure.fire(
                request_type='grpc',
                name='listSchoolingLength',
                response_time=total_time,
                exception=e
            )
        return self.res
class GrpcLocust(Locust):
    def __init__(self,*args,**kwargs):
        Locust.__init__(self,*args,**kwargs)
        # super(GrpcLocust,self).__init__()
        self.client = GrpcClient()

class GrpcTask(TaskSet):
    @task
    def test01_listSchoolingLength(self):
        res = self.client.conne()
class WebsiteUser(GrpcLocust):
    task_set = GrpcTask
    min_wait = 5000
    max_wait = 9000
if __name__ == '__main__':
    # os.system(r'locust -f loadTest.py')#locust网页：http://localhost:8089/
    os.system(r'locust -f loadTest.py --no-web --csv=foobar -c 1 -r 2 --run-time 10s')#命令行启动








