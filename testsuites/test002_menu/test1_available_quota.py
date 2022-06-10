# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.menu_management.available_quota import Available_Quota_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Available_Quota(unittest.TestCase):
    """
    测试登录模块
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

    def test_available_quota(self):
        """
        测试未加入域查看算力用例
        """
        available_quota_page = Available_Quota_Page(self.driver)
        available_quota_page.login()

        # 如果找到登录的元素那么判定登录成功
        result = available_quota_page.get_result()
        if result is True:
            self.assertTrue(result, logger.info("查看算力成功，且当前角色未加入域."))
        else:
            self.assertTrue(result, logger.critical('查看算力失败!'))


if __name__ == '__main__':
    unittest.main()
