#-*- coding:utf-8 -*-
#! usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
class BasePage(object):
    def __init__(self,base_url,driver):
        self.base_url = base_url
        self.driver = driver
    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(u'%s 页面中未能找到 %s 该元素'%(self,loc))
    def open(self):
        self._open(self.base_url)
    def exe_script(self,scr):
        self.driver.execute_script(scr)





