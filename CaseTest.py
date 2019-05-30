#-*- coding:utf-8 -*-
#! usr/bin/env python3
import unittest,time,readYml
from urllib import parse #拼接url
from LoginPage import *
from selenium import webdriver
class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    def testLogin(self):
        driver = self.driver
        url = readYml.readData()['url']
        username = readYml.readData()['username']
        password = readYml.readData()['password']
        login_Page = LoginPage(url,driver)
        login_Page.open()
        login_Page.input_username(username)
        login_Page.input_password(password)
        login_Page.login_sumbit()
        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print(12)
if __name__ == '__main__':
    suit = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    suit.addTest(CaseTest('testLogin'))
    runner.run(suit)

