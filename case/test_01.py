# coding:utf-8
from selenium import webdriver
import unittest
import time


class LoginTest(unittest.TestCase):
    '''登录类的案例'''
    @classmethod
    def setUpClass(cls):
        print("启动浏览器")
        cls.driver=webdriver.Firefox()
    def setUp(self):
        # self.driver=webdriver.Firefox()  #需要编程全局变量
        print("进入登录页面")
        self.driver.get("http://127.0.0.1/biz/user-login.html")
        time.sleep(3)
    def tearDown(self):
        print("判断是否存在alert")
        self.is_alert_exist()
        print("清空cookie")
        self.driver.delete_all_cookies()  #清空cookie,退出登录
        print("刷新页面")
        self.driver.refresh()
        # self.driver.quit()

    def get_login_username(self):    #判断是否登录成功
        try:
            t=self.driver.find_element_by_xpath(".//*[@id='userNav']/li/a/span[1]").text
            print(t)
            return t
        except:
            return ""
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
    def login(self,user,psw):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()

    def test_01(self):
        ''' 登录成功的案例'''
        time.sleep(5)
        self.login("admin","Booway@123")
        time.sleep(3)
        t=self.get_login_username()
        print("获取的结果：%s"%t)
        self.assertTrue(t=="admin")
    def test_02(self):
        '''登录失败的案例'''
        time.sleep(5)
        self.login("1","")
        time.sleep(3)
        t=self.get_login_username()
        print("获取的结果：%s"%t)
        self.assertTrue(1 == 2)  #断言失败截图

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        cls.driver.quit()


if __name__=="__main__":
    unittest.main()
