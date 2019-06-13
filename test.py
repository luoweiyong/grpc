#! usr/bin/env python3
#-*- coding:utf-8 -*-
import random
'''
@author:
@time:
'''
import uuid
# import time

name = 'test_name'
# namespace = 'test_namespace'
namespace = uuid.NAMESPACE_URL
print('\033[5;33m "%s" \033[0m',end=',')
print(uuid.uuid3(namespace, name),end=',')
print(uuid.uuid4(),end=',')
print(uuid.uuid5(namespace, name),end=',')
print(uuid.uuid1())
# num = random.randint(0,9999999)
# print(num)
#递归
# def calc(n):
#     print(n)
#     if n<5:
#         return calc(n+1)
#     print('-->',n)
# calc(2)

a = [22,58,42,1,3,66]
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# b = (2,5,6)
# a.sort(reverse = True)
# print(a)
# def px():
#     for i in range(0,len(a)):
#         for j in range(0,len(a)-i-1):
#             if a[j] > a[j+1]:
#                 t = a[j+1]
#                 a[j+1] = a[j]
#                 a[j] = t
# px()
# for i in range(len(a)):
#     print(a[i],end=" ")
# print(list(range(1,5)))
# for k in range(10):
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'%(j,i,j*i),end='\t')
#     print()
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print('%s*%s=%s'%(j,i,j*i),end='\t')
#     print()

# for i in range(10):
#     print(i,end=' ')

