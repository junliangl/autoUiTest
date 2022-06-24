# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.account_management.login_and_logout import Login_And_Logout_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Login_And_Logout(unittest.TestCase):
    """
    测试登录注销模块
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

    def test1_login(self):
        """
        测试登录
        """
        login_and_logout_page = Login_And_Logout_Page(self.driver)
        login_and_logout_page.login()
        # 如果找到登录的元素那么判定登录成功
        result = login_and_logout_page.get_login_result()
        if result is True:
            self.assertTrue(result, logger.info('登录成功'))
        else:
            self.assertTrue(result, logger.error('登录失败'))

    def test2_cancel_logout(self):
        """
        测试取消注销
        """
        login_and_logout_page = Login_And_Logout_Page(self.driver)
        result = login_and_logout_page.get_cancel_result()
        if result:
            self.assertTrue(result, logger.info('取消注销成功'))
        else:
            self.assertTrue(result, logger.error('发生未知异常，取消注销失败'))

    def test3_logout(self):
        """
        测试注销
        """
        login_and_logout_page = Login_And_Logout_Page(self.driver)
        result = login_and_logout_page.get_logout_result()
        if result:
            self.assertTrue(result, logger.info('注销成功'))
        else:
            self.assertTrue(result, logger.error('注销失败'))


if __name__ == '__main__':
    unittest.main()
