#-*- coding:utf-8 -*-
#! usr/bin/env python3
import time,unittest,HTMLTestRunner
from appium import webdriver
class calc_add(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.ibox.calculators'
        desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
        desired_caps['noReset'] = False
        desired_caps['resetKeyboard'] = False
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    def test_add(self):
        driver = self.driver
        time.sleep(8)
        driver.find_element_by_id("com.ibox.calculators:id/digit8").click()
        driver.find_element_by_id("com.ibox.calculators:id/plus").click()
        driver.find_element_by_id("com.ibox.calculators:id/digit9").click()
        driver.find_element_by_id("com.ibox.calculators:id/equal").click()
        time.sleep(3)
        print(driver.find_element_by_id("com.ibox.calculators:id/output_month").text)
        self.assertEqual(u"17",driver.find_element_by_id("com.ibox.calculators:id/output_month").text)
    def tearDown(self):
        self.driver.quit()
if  __name__  == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(calc_add('test_add'))
    runner = unittest.TextTestRunner()
    runner.run(suit)




