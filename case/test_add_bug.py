import unittest
from selenium import webdriver
import time
from case.add_bug import AddBug

class TEST_ADD_BUG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.bug=AddBug(cls.driver)
        cls.bug.login()

    def test_add_bug(self):
        timestr=time.strftime("%Y_%m_%d_%H_%M_%S")
        self.bug.add_bug(title="计划申报：无法提交审核"+timestr)

if __name__=="__main__":
    unittest.main()