# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.group_management.matching_management import Matching_Management_Page
from framework.logger import Logger
logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_User_Management(unittest.TestCase):
    """
    测试用户管理
    """

    # @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.driver.close()

    def test01_check_account_info(self):
        """
        测试查看用户账号信息信息
        """
        matching_management_page = Matching_Management_Page(self.driver)
        matching_management_page.login()
        result = matching_management_page.change_matching_management()
        if result:
            self.assertTrue(result, logger.info("修改app比对库没有问题."))
        else:
            self.assertTrue(result, logger.error("修改app比对库存在问题!"))


if __name__ == '__main__':
    unittest.main()