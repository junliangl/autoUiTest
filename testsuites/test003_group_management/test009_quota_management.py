# coding=utf-8
import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)
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

    def test01_check_available_quota_info(self):
        """
        测试查看本用户组算力信息
        """
        quota_management_page = Quota_Management_Page(self.driver)
        quota_management_page.login()
        quota_management_page.get_available_quota_info()

    def test02_check_allocatable_quota_info(self):
        """
        测试查看本用户组可分配算力信息
        """
        quota_management_page = Quota_Management_Page(self.driver)
        quota_management_page.get_allocatable_quota_info()

    def test03_check_valid_only(self):
        """
        测试只查看有效
        """
        quota_management_page = Quota_Management_Page(self.driver)
        quota_management_page.check_valid_only()

    def test04_check_record(self):
        """
        测试查看记录
        """
        quota_management_page = Quota_Management_Page(self.driver)
        result = quota_management_page.check_record()
        if result:
            self.assertTrue(result, logger.info("查看记录成功!"))
        else:
            self.assertTrue(result, logger.error("查看记录失败!"))

    def test05_check_using_detail(self):
        """
        测试查看使用详情
        """
        quota_management_page = Quota_Management_Page(self.driver)
        result = quota_management_page.check_using_detail()
        if result:
            self.assertTrue(result, logger.info("查看使用详情成功!"))
        else:
            self.assertTrue(result, logger.error("查看使用详情失败!"))


if __name__ == '__main__':
    unittest.main()
