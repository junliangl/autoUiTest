# _*_ coding:utf-8 _*_
import sys
import requests
import os
import unittest
import time

# 找到根目录
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加进根目录
sys.path.append(root_path)

from framework.logger import Logger

logger = Logger(logger="用例失败成功情况").get_log()
from Python_HTMLTestReportCN import HTMLTestReportCN

chrome_driver_path = os.path.join(os.path.join(root_path, 'tools'), 'chromedriver.exe')
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
            title='Ui_Auto_测试报告',
            description=u'执行情况',
            tester='CI/CD',
        )
        runner.run(suites)

    test_count = HTMLTestReportCN._TestResult()
    requests.post(
        url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=020eb2a4-78a4-47f2-90c3-fb97da4f7f4c',
        headers={'Content-Type': 'application/json;charset=UTF-8'},
        json={
            "msgtype": "markdown",
            "markdown": {
                "content": f"成功的用例数: {test_count.get_count()[0]}\n"
                           f"失败的用例数: {test_count.get_count()[1]}\n"
                           f"错误的用例数：{test_count.get_count()[2]}\n"
                           f"测试的用例总数：{test_count.get_count()[0] + test_count.get_count()[1] + test_count.get_count()[2]}\n"
                           f"测试报告地址: [10.1.1.156/ui-auto-test/{now_time}-test.html](10.1.1.156/ui-auto-test/{now_time}-test.html)"
            }
        }
    )
