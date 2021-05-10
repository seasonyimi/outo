import unittest
import os
from common import HTMLTestRunner_cn

#用例的路径
casePath=r"C:\Users\seaso\Desktop\study\outopython\case"
rule="test*.py"   #匹配test开头，py结尾的文件
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)
reportPath=r"C:\Users\seaso\Desktop\study\outopython\report"+"result.html"
fp=open(reportPath,"wb")                                         #以二进制去写入
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                     title="报告的title",
                                     description="描述干啥用的",
                                     # retry=1                  #失败重跑一次
                                        )
runner.run(discover)
fp.close()