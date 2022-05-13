# coding=utf-8
import os
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from page_objects.account_management.change_password import Change_Password_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(os.path.join(project_path, 'data'), 'change_password_data.json')


@ddt
class Test_Change_Password(unittest.TestCase):
    """
    测试登录模块
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

    def test1_confirm_change_password(self):
        """
        测试修改密码取消用例
        """
        change_password_page = Change_Password_Page(self.driver)
        change_password_page.input_login_message_account("testauto")
        change_password_page.input_login_message_password()
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
        change_password_page.click_login_button()
        change_password_page.click_username_button()
        change_password_page.click_change_password_button()
        change_password_page.click_cancel_button()

        # 如果找到取消元素那么判定取消修改密码页面失败
        if change_password_page.get_cancel_result() is True:
            self.assertTrue(change_password_page.get_cancel_result(), logger.info('取消修改密码成功'))
        else:
            self.assertTrue(change_password_page.get_cancel_result(), logger.critical('取消修改密码失败'))

    @file_data(data_path)
    def test2_change_password(self, password, new_password, confirm_password):
        """
        测试修改密码取消用例
        """
        change_password_page = Change_Password_Page(self.driver)
        change_password_page.click_username_button()
        change_password_page.click_change_password_button()
        change_password_page.input_initial_password(password)
        change_password_page.input_new_password(new_password)
        change_password_page.input_confirm_password(confirm_password)
        change_password_page.click_confirm_button()

        # 如果找到确认按钮那么判定修改密码失败
        if change_password_page.get_change_result() is True:
            self.assertTrue(change_password_page.get_change_result(), logger.info('修改密码成功'))
        else:
            self.assertTrue(change_password_page.get_change_result(), logger.critical('修改密码失败'))


if __name__ == '__main__':
    unittest.main()
