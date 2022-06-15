# coding=utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.account_management.accept_invite import Accept_Invite_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Accept_Invite(unittest.TestCase):
    """
    测试接受邀请入组
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

    def test1_create_new_group(self):
        """
        测试superadmin创建新的域
        """
        accept_invite_page = Accept_Invite_Page(self.driver)
        accept_invite_page.login()
        result = accept_invite_page.accept_invite()
        if result is True:
            self.assertTrue(result, logger.info('接受入组成功.'))
        else:
            self.assertTrue(result, logger.error('接受入组失败!'))


if __name__ == '__main__':
    unittest.main()
