# coding=utf-8
import os
import unittest
from common.browser_engine import BrowserEngine
from common.browser_info import Browser_Info
from page_objects.account_management.register import Register_Page
from common.logger import Logger

logger = Logger(logger='测试结果').get_log()
get_browser_info = Browser_Info()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Register(unittest.TestCase):
    """
    测试注册模块
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

    # 拿到json里的数据进行数据驱动测试
    # @file_data(data_path)
    def test1_register(self):
        """
        测试注册用例
        """
        register_page = Register_Page(self.driver)
        result = register_page.register_account()
        if result:
            self.assertTrue(result, logger.info("注册成功."))
        else:
            self.assertTrue(result, logger.error("注册失败!"))


if __name__ == '__main__':
    unittest.main()
