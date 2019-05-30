#-*- coding:utf-8 -*-
#! usr/bin/env python3
import time

def timer(func):    #timer(test1) func = test1
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("func run time is %s"%(stop_time-start_time))
    return deco

@timer  #test1 = timer(test1)
def test1():
    time.sleep(1)
    print("in the test1")
@timer
def test2(name):
    time.sleep(1)
    print("in the test1",name)
test1()
test2("666")


