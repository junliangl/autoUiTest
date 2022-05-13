# coding=utf-8
import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from framework.browser_info import Message
from page_objects.group_management.quota_management import Quota_Management_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains
logger = Logger(logger='测试结果').get_log()
get_message = Message()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(os.path.join(project_path, 'data'), 'quota_management_data.json')


@ddt
class Test_Quota_Management(unittest.TestCase):
    """
    测试算力管理
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
    def test01_check_quota_management_info(self, account, password):
        """
        测试查看算力信息
        """
        quota_management_page = Quota_Management_Page(self.driver)
        quota_management_page.input_login_message_account(account)
        quota_management_page.input_login_message_password(password)
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
        quota_management_page.click_login_button()
        quota_management_page.click_setting_button()
        quota_management_page.click_group_button()
        quota_management_page.click_quota_management()
        quota_management_page.sleep(6)
        quota_management_page.get_quota_info()


if __name__ == '__main__':
    unittest.main()
