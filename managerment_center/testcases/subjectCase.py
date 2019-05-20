#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/22 9:31
"""
import unittest
from call_method.basicmanagement.BM_subject_client import Subject

class SubjectTest(unittest.TestCase):
    def setUp(self):
        self.S = Subject()

    def test_01_listSchoolingLength(self):
        result= self.S.listSchoolingLength('0')
        # print(result)
        self.assertEqual(result['msg'], '成功', '获取学制失败')

    def test_02_insertSubject(self):
        result = self.S.insertSubject(0, '201', '初中地理', '7,8,9', '2')
        # print(result)
        self.assertEqual(result['msg'], '成功', '插入学科失败')

    def test_03_listSubject(self):
        result= self.S.listSubject('0')
        print(result)
        self.assertEqual(result['msg'], '成功', '获取学科失败')

        subjectList= result['datas']
        for subject in subjectList:
            if subject['subjectName'] == '初中地理':
                SubjectTest.subjectId= subject['id']

    def test_04_updateSubject(self):
        result= self.S.updateSubject(SubjectTest.subjectId, '201', '初中地理', '6,7,8,9', '2')
        # print(result)
        self.assertEqual(result['msg'], '成功', '插入学科失败')

    def test_05_listSubject(self):
        result= self.S.listSubject('0')
        # print(result)
        self.assertEqual(result['msg'], '成功', '获取学科失败')

    def test_06_deleteSubject(self):
        result = self.S.deleteSubject(str(SubjectTest.subjectId))
        # print(result)
        self.assertEqual(result['msg'], '成功', '删除学科失败')

if __name__ == '__main__':
    unittest.main()