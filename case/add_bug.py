#coding:utf-8

from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time

class AddBug(Base):  #继承
     #定位登录
    loc1=(By.ID,"account")
    loc2=(By.NAME,"password")
    loc3=(By.ID,"submit")
    #添加bug
    loc_test=(By.XPATH,".//*[@id='navbar']/ul/li[4]/a")   #进入测试
    loc_bug=(By.XPATH,".//*[@id='subNavbar']/ul/li[1]/a")     #进入bug页面
    loc_addbug=(By.XPATH,".//*[@id='mainMenu']/div[3]/a[4]")   #提交Bug
    loc_turck=(By.XPATH,".//*[@id='openedBuild_chosen']/ul")    #点击影响模块
    loc_turck_add=(By.XPATH,".//*[@id='openedBuild_chosen']/div/ul/li")   #选择影响模块
    loc_input_title=(By.ID,"title")                           #添加标题
     #切换iframe
    loc_input_body=(By.CLASS_NAME,"article-content")     #填写内容
    loc_sumbit_button=(By.ID,"submit")
    #新增bug标题
    loc_bug_title=(By.XPATH,".//*[@id='bugList']/tbody/tr[1]/td[5]/a")
    def login(self,user="admin",psw="Booway@123"):
        self.driver.get("http://127.0.0.1/biz/user-login.html")
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,psw)
        self.click(self.loc3)
    def add_bug(self,title="计划申报：无法提交审核"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_turck)
        self.click(self.loc_turck_add)
        self.sendKeys(self.loc_input_title,title)
        #输入body
        body='''第一步xxx
        结果正确
        期望结果是啥
        '''
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        #self.clear(self.loc_input_body)          #副文本不能clear
        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()
        self.click(self.loc_sumbit_button)


if __name__=="__main__":
    pass





