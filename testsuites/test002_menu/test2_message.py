# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.menu_management.message import Message_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Message(unittest.TestCase):
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

    def test01_check_message(self):
        """
        测试查看消息用例
        """
        message_page = Message_Page(self.driver)
        message_page.login()
        result = message_page.get_message_result()
        if result:
            self.assertTrue(result, logger.info('消息框成功打开，查看消息成功'))
        else:
            self.assertTrue(result, logger.info('查看消息失败'))


if __name__ == '__main__':
    unittest.main()
