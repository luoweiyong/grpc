#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/10 14:08
"""
import unittest
import yaml
import os
from call_method.resourcecenter.point_client import Point
from call_method.resourcecenter.RC_subject_client import Subject

BASE_DIR= os.path.dirname(os.path.dirname(__file__))
file_path= BASE_DIR+ '/datas/env.yml'

with open(file_path, 'r', encoding='utf-8') as file2:
    datas= yaml.safe_load(file2)

class PointTest(unittest.TestCase):
    def setUp(self):
        self.S = Subject()
        self.P = Point()
        self.pageNo= datas['page']['pageNo']
        self.pageSize= datas['page']['pageSize']

    def test_01_listSubject(self):
        result = self.S.listSubject()
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '获取学科失败')
        subjectList= result['datas']
        for i in subjectList:
            if i['subjectName'] == '小学语文':
                PointTest.subjectId= i['id']

    def test_02_createPoint(self):
        result= self.P.createPoint(id= 0,parentId= 0, pointIndex= 2, subjectId= PointTest.subjectId, pointName= '小学语文知识点测试数据2')
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '新增知识点失败')
        PointTest.pointId= result['data']['value']

    def test_03_listPointsBySubjectId(self):
        result = self.P.listPointsBySubjectId(value= PointTest.subjectId)
        # print(result)
        # self.assertEqual(result['msg'], '操作成功', '查询知识点失败')
        pointList= result['datas']
        for i in pointList:
            if i['id'] == PointTest.pointId:
                self.assertEqual(i['id'], PointTest.pointId, '插入知识点失败')

    def test_04_updatePoint(self):
        result = self.P.updatePoint(id= PointTest.pointId, parentId= 0, pointIndex= 0, subjectId= PointTest.subjectId,
                                    pointName= '小学语文知识点测试数据-改')
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '修改知识点失败')

    def test_05_listPointsBySubjectId(self):
        result= self.P.listPointsBySubjectId(value= PointTest.subjectId)
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '查询知识点失败')
        pointList = result['datas']
        for i in pointList:
            if i['id'] == PointTest.pointId:
                self.assertEqual(i['pointName'], '小学语文知识点测试数据-改', '插入知识点失败')

    def test_06_deletePoint(self):
        result = self.P.deletePoint(value= PointTest.pointId)
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '删除知识点失败')

    def test_07_listPointsBySubjectId(self):
        result= self.P.listPointsBySubjectId(value= PointTest.subjectId)
        # print(result)
        self.assertEqual(result['msg'], '操作成功', '查询知识点失败')
        pointList = result['datas']
        idList= []
        for i in pointList:
            idList.append(i['id'])
        # print(idList)
        self.assertNotIn(PointTest.pointId, idList, '知识点删除失败')

if __name__ == '__main__':
    unittest.main()