# coding=utf-8
import os
import unittest
from common.browser_engine import BrowserEngine
from page_objects.group_management.check_group import Check_Group_Page
from common.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Check_Group(unittest.TestCase):
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

    def test1_check_group(self):
        """
        测试查看当前用户的所有的域
        """
        see_group_page = Check_Group_Page(self.driver)
        see_group_page.login()
        result = see_group_page.get_check_groups_result()
        if result is True:
            self.assertTrue(result, logger.info("进入所有域管理成功."))
        else:
            self.assertTrue(result, logger.error("进入所有域失败!"))


if __name__ == '__main__':
    unittest.main()
