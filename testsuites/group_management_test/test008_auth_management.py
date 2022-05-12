# coding=utf-8
import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from framework.browser_info import Message
from page_objects.group_management.auth_management import Auth_Management_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains
logger = Logger(logger='测试结果').get_log()
get_message = Message()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(os.path.join(project_path, 'data'), 'auth_management_data.json')


@ddt
class Test_Auth_Management(unittest.TestCase):
    """
    测试 license 授权管理
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

    @file_data(data_path)
    def test01_check_license_info(self, account, password):
        """
        测试查看域授权码信息
        """
        auth_management_page = Auth_Management_Page(self.driver)
        auth_management_page.input_login_message_account(account)
        auth_management_page.input_login_message_password(password)
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
        auth_management_page.click_login_button()
        auth_management_page.click_setting_button()
        auth_management_page.click_group_button()
        auth_management_page.click_auth_management()
        auth_management_page.sleep(6)
        auth_management_page.get_used_info()

    def test02_generate_auth_code(self):
        """
        测试生成授权码
        """
        auth_management_page = Auth_Management_Page(self.driver)
        result = auth_management_page.generate_authorization_code()
        if result:
            self.assertTrue(result, logger.info("生成授权码没有问题"))
        else:
            self.assertTrue(result, logger.error("生成授权码存在问题"))

    def test03_ban_auth_code(self):
        """
        测试禁用授权码
        """
        auth_management_page = Auth_Management_Page(self.driver)
        result = auth_management_page.ban_auth_code()
        if result:
            self.assertTrue(result, logger.info("禁用授权码没有问题"))
        else:
            self.assertTrue(result, logger.error("禁用授权码存在问题"))

    def test04_recover_auth_code(self):
        """
        测试恢复授权码
        """
        auth_management_page = Auth_Management_Page(self.driver)
        result = auth_management_page.recover_auth_code()
        if result:
            self.assertTrue(result, logger.info("恢复授权码没有问题"))
        else:
            self.assertTrue(result, logger.error("恢复授权码存在问题"))

    def test05_check_qrcode(self):
        """
        测试查看授权码
        """
        auth_management_page = Auth_Management_Page(self.driver)
        result = auth_management_page.check_qrcode()
        if result:
            self.assertTrue(result, logger.info("查看授权码没有问题"))
        else:
            self.assertTrue(result, logger.error("查看授权码码存在问题"))

    def test06_search_first_auth_code(self):
        """
        测试搜索结果
        """
        auth_management_page = Auth_Management_Page(self.driver)
        result = auth_management_page.search_first_auth_code()
        if result:
            self.assertTrue(result, logger.info("搜索结果没有问题"))
        else:
            self.assertTrue(result, logger.error("搜索结果存在问题"))


if __name__ == '__main__':
    unittest.main()
