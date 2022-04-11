# _*_ coding:utf-8 _*_
import sys
import os
import unittest
import time
from selenium import webdriver

# 当前文件的绝对路径
now_path = os.path.dirname(os.path.abspath(__file__))
# 找到根目录
root_path = os.path.dirname(now_path)
# 添加进根目录
sys.path.append(root_path)

from Python_HTMLTestReportCN import HTMLTestReportCN

report_path = os.path.join(root_path, 'test_report')
now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

HtmlFile = os.path.join(report_path, now_time + "-test.html")

if __name__ == '__main__':
    with open(HtmlFile, 'wb') as file:
        print(os.path.abspath(__file__))
        suites = unittest.TestLoader().discover(
            os.path.join(root_path, 'testsuites'))
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=file,
            title=input('请输入测试报告名称：   '),
            description=u'执行情况',
            tester=input('请输入测试人名字：     '),
        )
        runner.run(suites)


# 测试结束后自动打开测试报告且不让它关闭
def open_report_html():
    global driver
    driver = webdriver.Chrome()
    driver.get(os.path.join('file://', HtmlFile))


open_report_html()
