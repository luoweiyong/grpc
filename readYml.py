#! usr/bin/env python3
#-*- coding:utf-8 -*-
import yaml
def readData():
    with open(r'./env.yml','rb') as  f:
        data = yaml.safe_load(f)
    return data
print(readData())