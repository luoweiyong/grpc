#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/23 13:53
"""

import unittest
import yaml
import os
from call_method.resourcecenter.material_client import Material
from call_method.resourcecenter.RC_subject_client import Subject

BASE_DIR= os.path.dirname(os.path.dirname(__file__))
file_path= BASE_DIR+ '/datas/env.yml'

with open(file_path, 'r', encoding='utf-8') as file2:
    datas= yaml.safe_load(file2)

class PointTest(unittest.TestCase):
    def setUp(self):
        self.S = Subject()
        self.M = Material()
        self.pageNo= datas['page']['pageNo']
        self.pageSize= datas['page']['pageSize']

    def test_01_listMaterial(self):
        result = self.M.listMaterial(name= None, teacherId= None,  createType= None, categoryId= 4,
                                     customerId= 4403051000, subjectId= 102, chapterId= None, pointId= None,
                                     materialUsageStatistic= None,updateTimeStatistic= 2, searchContent= None,
                                     isBoutique= None, pageNo= 2, pageSize= 10)
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '获取素材失败')
        materialList= result['datas']['materialViews']
        for i in materialList:
            if i['subjectName'] == '小学语文':
                PointTest.subjectId= i['id']

    def test_02_updateMaterial(self):
        result= self.M.updateMaterial()
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '修改素材失败')
        PointTest.pointId= result['data']['value']

if __name__ == '__main__':
    unittest.main()