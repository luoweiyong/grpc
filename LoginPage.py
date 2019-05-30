#-*- coding:utf-8 -*-
#! usr/bin/env python3
from BasePage import *
from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage(BasePage):
    username_loc = (By.ID,'userName')
    password_loc = (By.ID,'password')
    login_loc = (By.ID,'check')
    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def login_sumbit(self):
        self.find_element(*self.login_loc).click()


