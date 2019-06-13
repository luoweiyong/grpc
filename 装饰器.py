#! usr/bin/env python3
#-*- coding:utf-8 -*-
# import time
# def timer(func):
#     def deco(*args,**kwargs):
#         start_time = time.time()
#         func(*args,**kwargs)
#         stop_time = time.time()
#         print("the func run_time is %s"%(stop_time-start_time))
#     return deco
# @timer
# def test1():
#     time.sleep(3)
#     print("in the test1")
# # def test2():
# #     time.sleep(3)
# #     print("in the test2")
# test1()
from google.protobuf.json_format import MessageToDict
# import chardet
# s = b'\xE6\x95\x99\xE5\xAD\xA911\xE6\xA0\x87'
# print(chardet.detect(s))
# s1 = s.decode('utf-8')
# s2 = s1.encode('utf-8')
# print(s1)
# print(s2)

# print('\n'.join([''.join([('Love'[(x-y) % len('Love')]
#                            if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
#                           for x in range(-30, 30)]) for y in range(30, -30, -1)]))
from turtle import *
a2 = []
for y in range(15,-15,-1):
    a1 = []
    for x in range(-30,30):
        if -0.28<=((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=-0.0009:
            a1.append('\033[1;31;40mo\033[0m')
        elif (x == -15) and (y == (10 or 9)):
            a1.append('\b\033[1;34;40m的\033[0m')
        elif (x == -16) and (y == (9 or 8)):
            a1.append('\b\033[1;34;40m发')
        elif (x == -17) and (y == (8 or 7)):
            a1.append('\b\033[1;34;40m我')
        elif (x == 14) and (y == (10 or 9)):
            a1.append('\b\033[1;32;40m是')
        elif (x == 15) and (y == (9 or 8)):
            a1.append('\b\033[1;32;40m他')
        elif (x == 16) and (y == (8 or 7)):
            a1.append('\b\033[1;32;40m传')
        elif (x==0) and (y == 2):
            a1.append('相')
        elif (x==0) and (y == 1):
            a1.append('爱')
        elif (x==0) and (y == 0):
            a1.append('一')
        elif (x==0) and (y == -1):
            a1.append('生')
        else:
            a1.append(' ')
    a2.append(''.join(a1))

b = '\n'.join(a2)
print(b)


