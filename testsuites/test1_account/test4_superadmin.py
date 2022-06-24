# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.account_management.superadmin import Superadmin_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Login_And_Logout(unittest.TestCase):
    """
    测试superadmin模块
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
        superadmin_page = Superadmin_Page(self.driver)
        superadmin_page.login()
        result = superadmin_page.create_new_group()
        if result is True:
            self.assertTrue(result, logger.info('创建新域成功.'))
        else:
            self.assertTrue(result, logger.error('创建新域失败!'))

    def test2_create_private_db(self):
        """
        测试superadmin创建私有库
        """
        superadmin_page = Superadmin_Page(self.driver)
        result = superadmin_page.create_private_db()
        if result:
            self.assertTrue(result, logger.info('创建私有库成功.'))
        else:
            self.assertTrue(result, logger.error('创建私有库失败!'))

    def test3_invite_to_group(self):
        """
        测试superadmin邀请入组
        """
        superadmin_page = Superadmin_Page(self.driver)
        result = superadmin_page.invite_to_group()
        if result:
            self.assertTrue(result, logger.info('邀请用户入组成功.'))
        else:
            self.assertTrue(result, logger.error('邀请用户入组失败.'))


if __name__ == '__main__':
    unittest.main()
