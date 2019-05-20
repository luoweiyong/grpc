#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/11 15:56
"""
import time
from locust import (TaskSet,task,events,Locust)
from gevent._semaphore import Semaphore

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()

events.hatch_complete += on_hatch_complete

class GrpcClient(object):
    """重写self.client"""
    # def __init__(self):
    #     self.S= Subject()

    def connect(self, func, *args):
        # 记录开始时间
        start_time = int(time.time())
        try:
            #调用
            result =func(*args)
            total_time = int((time.time() - start_time) * 1000)
            if result['msg'] != '操作成功':
                raise Exception
            events.request_success.fire(
                request_type='grpc', name=r'/listSubject', response_time=total_time,response_length=0)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type='grpc', name='/listSubject', response_time=total_time, exception=e)
        # return result

class GrpcLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GrpcLocust, self).__init__(*args, **kwargs)
        self.client = GrpcClient()

class GrpcTask(TaskSet):
    """压测任务"""
    def on_start(self):
        from call_method.basicmanagement.BM_subject_client import Subject
        self.S= Subject()
        all_locusts_spawned.wait()

    @task
    def listSubject(self):
        #grpc接口响应数据
        self.client.connect(self.S.listSubject())
        # print(result)
        # print('errCode:{}'.format(result.errCode))
        # print('result:{}'.format(result.result))
        # print('errMsg:{}'.format(result.errMsg))

class WebsiteUser(GrpcLocust):
    task_set = GrpcTask
    min_wait = 5000
    max_wait = 9000

