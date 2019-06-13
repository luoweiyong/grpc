#! usr/bin/env python3
#-*- coding:utf-8 -*-
import unittest

class Test(unittest.TestCase):
    def  test01_calc(self):
        global a
        a = 4
        print('a=',a)
    def test02_sum(self):
        b = a + 1
        print(b)
if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # run = unittest.TextTestRunner()
    # suit.addTest(Test('test01_calc'))
    # suit.addTest(Test('test02_sum'))
    # run.run(suit)
    unittest.main()
