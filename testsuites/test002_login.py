# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from framework.browser_info import Message
from page_objects.login import Login_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By

logger = Logger(logger='登录测试结果').get_log()
get_message = Message()

# 登录按钮
login_button_element = (
    By.XPATH, '/html/body/app-root/app-login/div/form/nz-form-item[3]/nz-form-control/div/div/button')


class Test_Login(unittest.TestCase):
    """
    测试登录模块
    """

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, *login_button_element)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        pass

    # 判断是用的哪个 driver
    def test_login(self):
        """
        测试登录用例
        """
        login_page = Login_Page(self.driver)  # 把 setup 的 driver 传下来
        if get_message.get_driver() == "Chrome":
            login_page.input_login_message_account('testauto')
            login_page.input_login_message_password('aA123456')  # 调用页面对象中的方法
            action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
            login_page.click_login_button()
            login_page.get_windows_img()

        elif get_message.get_driver() == "Firefox":
            login_page.input_login_message_account('testauto')
            login_page.input_login_message_password('aA123456')  # 调用页面对象中的方法
            action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
            login_page.click_login_button()
            login_page.get_windows_img()

            # 如果找到登录的元素那么判定登录成功
        if login_page.get_result() is True:
            self.assertTrue(login_page.get_result(), logger.info('登录成功'))
        else:
            self.assertTrue(login_page.get_result(), logger.critical('登录失败'))


if __name__ == '__main__':
    unittest.main()
