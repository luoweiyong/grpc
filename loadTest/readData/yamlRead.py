#! usr/bin/env python3
# -*- coding:utf-8 -*-
import yaml


def yamlRead():
    with open('E:\PythonProject\grpc_interface\datas\data.yaml', 'rb') as f:
        data = yaml.safe_load(f)
    return data


