#! usr/bin/env python3
#-*- coding:utf-8 -*-
#注意：列表是线程不安全的
#例子4
import threading,time

li=[1,2,3,4,5]

def pri():
    while li:
        a=li[-1]
        print(a)
        time.sleep(1)
        try:
            li.remove(a)
        except:
            print('----',a)

t1=threading.Thread(target=pri,args=())
t1.start()
