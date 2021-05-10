# -*- coding:utf-8 -*-

import logging,os

log_path = os.path.dirname(os.getcwd())
print("log_path:",log_path)
class Logger:
    def __init__(self,loggername):
        #创建一个logger
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logging.DEBUG)
        #创建一个handler，用于写入日志文件
        log_path = os.path.dirname(os.getcwd()+"/logs/") #指定文件输入的路径
        logname = log_path + 'out.log' #指定输出的日志文件名
        fh = logging.FileHandler(logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        #创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setLevel(logging.DEBUG)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        #定义一个函数，回调logger实例
        return self.logger

if __name__ == '__main__':
    t = Logger("season").get_log().debug("User %s is loging" % 'jeck')
