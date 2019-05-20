#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/30 10:50
"""

import unittest
import yaml
import os
from call_method.basicmanagement.BM_subject_client import Subject

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file1_path= BASE_DIR+ '/datas/env.yml'
file2_path= BASE_DIR+ '/edition_datas.yml'

with open(file1_path, 'r', encoding='utf-8') as file1:
    baseDatas= yaml.safe_load(file1)

with open(file2_path, 'r', encoding='utf-8') as file2:
    datas= yaml.safe_load(file2)

class gradeTest(unittest.TestCase):
    def setUp(self):
        self.S = Subject()
        self.pageNo= baseDatas['page']['pageNo']
        self.pageSize= baseDatas['page']['pageSize']
        self.stageId= datas['chinese1']['four-one']['stageId']
        self.gradeId= datas['chinese1']['four-one']['gradeId']
        self.subjectId= datas['chinese1']['four-one']['subjectId']
        self.pressId= datas['chinese1']['four-one']['pressId']
        self.fascicleId= datas['chinese1']['four-one']['fascicleId']
        self.coverUrl= datas['chinese1']['four-one']['coverUrl']
        self.gradeName= datas['chinese1']['four-one']['gradeName']
        self.fascicleName= datas['chinese1']['four-one']['fascicleName']
        self.datas= datas['chinese1']['four-one']['chapter-datas']

    def test_01_listGrade(self):
        result = self.S.listGrade('0')
        # print(result)
        self.assertEqual(result['msg'], '成功', '获取年级失败')

    def test_02_insertEdition(self):
        result= self.S.insertEdition(self.stageId, self.gradeId, self.subjectId, self.pressId, self.fascicleId,
                                     self.coverUrl, self.gradeName, self.fascicleName, self.datas)
        # print(result)
        self.assertEqual(result['msg'], '成功', '新增教材失败')


    def test_03_listEdition(self):
        result = self.S.listEdition(self.pageNo, self.pageSize, self.gradeId, self.pressId, self.subjectId, self.stageId)
        # print(result)
        self.assertEqual(result['msg'], '成功', '获取教材失败')

        editionList= result['datas']
        # print(editionList)
        for i in editionList:
            if i['gradeName']== self.gradeName and i['fascicleName']== self.fascicleName:
                gradeTest.editionId= i['id']
        print(gradeTest.editionId)

    def test_04_updateEdition(self):
        result= self.S.updateEdition(gradeTest.editionId, self.stageId, self.gradeId, self.subjectId, self.pressId,
                                     self.fascicleId,self.coverUrl, self.gradeName, self.fascicleName, self.datas)
        # print(result)
        self.assertEqual(result['msg'], '成功', '修改教材失败')

    def test_05_listEdition(self):
        result = self.S.listEdition(self.pageNo, self.pageSize, self.gradeId, self.pressId, self.subjectId,
                                    self.stageId)
        editionList = result['datas']
        print(editionList)
        for i in editionList:
            if i['gradeName']== self.gradeName and i['fascicleName']== self.fascicleName:
                coverUrl= i['coverUrl']
        self.assertEqual(coverUrl, 'b.png', '修改教材失败')

    def test_06_deleteEdition(self):
        result= self.S.deleteSubject(gradeTest.editionId)
        print(result)
        self.assertEqual(result['msg'], '成功', '删除教材失败')


if __name__ == '__main__':
    unittest.main()