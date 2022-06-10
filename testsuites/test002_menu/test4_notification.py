# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.menu_management.notification import Notification_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Notification(unittest.TestCase):
    """
    测试提醒设置
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

    def test01_check_default_reminder(self):
        """
        测试查看默认提醒设置
        """
        notification_page = Notification_Page(self.driver)
        notification_page.login()
        result = notification_page.check_default_reminder_button()
        if result:
            self.assertTrue(result, logger.info('默认提醒设置没有问题.'))
        else:
            self.assertTrue(result, logger.info('默认提醒设置没有问题!'))

    def test02_change_settings(self):
        """
        测试修改提醒设置
        """
        notification_page = Notification_Page(self.driver)
        result = notification_page.change_setting()
        if result:
            self.assertTrue(result, logger.info('修改提醒设置没有问题.'))
        else:
            self.assertTrue(result, logger.info('修改提醒设置存在问题!'))


if __name__ == '__main__':
    unittest.main()
