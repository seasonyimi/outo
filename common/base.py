#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import Logger
import time,logging
class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver=driver
        self.timeout=10
        self.t=0.5
    #定位元素的等待时间写法
    def waitTime(self,locator):
        ele= WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele
    # 输入内容
    def sendKeys(self,locator,text):
        ele=self.waitTime(locator)
        ele.send_keys(text)
    # 点击按钮
    def click(self,locator):
        ele=self.waitTime(locator)
        ele.click()
    # 清除
    def clear(self,locator):
        ele=self.waitTime(locator)
        ele.clear()
    def is_alert_exist(self):
        ''' 判断是否alert'''
        try:
            time.sleep(2)
            alert=self.driver.switch_to.alert
            text=alert.text
            alert.accept()   #用alert 点alert
            return text
        except:
            return ""
