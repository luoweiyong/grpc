#! usr/bin/env python3
#-*- coding:utf-8 -*-
# a = [i+2 for i in range(2)] 列表生成式
# print(a)
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a,b = b ,a+b
        n = n +1
    return 'done'
f = fib(5)
# fib(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())