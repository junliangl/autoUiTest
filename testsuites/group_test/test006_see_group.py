# coding=utf-8
import os
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from framework.browser_info import Message
from page_objects.group_management.see_group import See_Group_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains

logger = Logger(logger='测试结果').get_log()
get_message = Message()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(os.path.join(project_path, 'data'), 'see_group_data.json')


@ddt
class Test_see_group(unittest.TestCase):
    """
    测试查看域
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
    def test_see_group(self, account, password):
        """
        测试查看当前用户的所有的域
        """
        see_group_page = See_Group_Page(self.driver)
        see_group_page.input_login_message_account(account)
        see_group_page.input_login_message_password(password)
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
        see_group_page.click_login_button()

        result = see_group_page.get_click_groups_result()
        if result is True:
            self.assertTrue(result, logger.info("进入所有域管理成功."))
        else:
            self.assertTrue(result, logger.warning("进入所有域失败!"))


if __name__ == '__main__':
    unittest.main()
