#! usr/bin/env python3
#-*- coding:utf-8 -*-

class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eating %s"%(self.name,food))
d = Dog('Smith')
# d.eat()
choice = input('>>:').strip()

if hasattr(d,choice):
    func = getattr(d,choice)
    func(u'面包')
else:
    print("Have no this attr")

#hasattr(object,str)：判断一个对象中是否有str属性
# getattr(object,str)：获取该对象中的str属性


