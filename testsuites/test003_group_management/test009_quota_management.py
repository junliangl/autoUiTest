# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.group_management.quota_management import Quota_Management_Page
from framework.logger import Logger
logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Quota_Management(unittest.TestCase):
    """
    测试算力管理
    """

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        cls.driver.close()

    def test01_check_quota_management_info(self):
        """
        测试查看算力信息
        """
        quota_management_page = Quota_Management_Page(self.driver)
        quota_management_page.login()
        quota_management_page.get_quota_info()


if __name__ == '__main__':
    unittest.main()
