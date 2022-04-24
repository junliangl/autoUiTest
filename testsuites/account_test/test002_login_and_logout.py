# coding=utf-8
import os
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from page_objects.account_management.login_and_logout import Login_And_Logout_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(os.path.join(project_path, 'data'), 'login_and_logout_data.json')


@ddt
class Test_Login_And_Logout(unittest.TestCase):
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

    @file_data(data_path)
    def test_login_and_logout(self, account, password):
        """
        测试登录和退出用例
        """
        login_and_logout_page = Login_And_Logout_Page(self.driver)
        login_and_logout_page.input_login_message_account(account)
        login_and_logout_page.input_login_message_password(password)
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
        login_and_logout_page.click_login_button()
        login_and_logout_page.get_windows_img()

        # 如果找到登录的元素那么判定登录成功
        if login_and_logout_page.get_login_result() is True:
            self.assertTrue(login_and_logout_page.get_login_result(), logger.info('登录成功'))
        else:
            self.assertTrue(login_and_logout_page.get_login_result(), logger.critical('登录失败'))

        # 点击取消注销
        login_and_logout_page.click_username_button()
        login_and_logout_page.click_logout_button()
        login_and_logout_page.click_cancel_button()
        try:
            if login_and_logout_page.get_cancel_result() is True:
                self.assertTrue(login_and_logout_page.get_cancel_result(), logger.info('取消注销成功'))
            else:
                self.assertTrue(login_and_logout_page.get_cancel_result(), logger.critical('发生未知异常，取消注销失败'))
        except Exception as e:
            logger.warning(e)

        # 点击注销前刷新一下网页
        login_and_logout_page.refresh_browser()
        login_and_logout_page.click_username_button()
        login_and_logout_page.click_logout_button()
        login_and_logout_page.click_confirm_button()

        if login_and_logout_page.get_logout_result() is True:
            self.assertTrue(login_and_logout_page.get_logout_result(), logger.info('注销成功'))
        else:
            self.assertTrue(login_and_logout_page.get_logout_result(), logger.critical('注销失败'))


if __name__ == '__main__':
    unittest.main()
