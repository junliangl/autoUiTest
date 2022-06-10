# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.menu_management.help import Help_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Help(unittest.TestCase):
    """
    测试查看帮助
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

    def test01_look_help(self):
        """
        测试查看帮助菜单
        """
        help_page = Help_Page(self.driver)
        help_page.login()
        result = help_page.look_help()
        if result:
            self.assertTrue(result, logger.info('查看帮助菜单成功.'))
        else:
            self.assertTrue(result, logger.info('查看帮助菜单失败!'))


if __name__ == '__main__':
    unittest.main()
