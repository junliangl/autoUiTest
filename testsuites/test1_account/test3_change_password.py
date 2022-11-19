# coding=utf-8
import os
import unittest
from common.browser_engine import BrowserEngine
from page_objects.account_management.change_password import Change_Password_Page
from common.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Change_Password(unittest.TestCase):
    """
    测试修改密码模块
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
        change_password_page = Change_Password_Page(cls.driver)
        change_password_page.restore_initial_password()
        cls.driver.close()

    def test1_cancel_change_password(self):
        """
        测试取消修改密码
        """
        change_password_page = Change_Password_Page(self.driver)
        change_password_page.login()
        result = change_password_page.get_cancel_result()
        # 如果找到取消元素那么判定取消修改密码页面失败
        if result:
            self.assertTrue(result, logger.info('取消修改密码成功'))
        else:
            self.assertTrue(result, logger.error('取消修改密码失败'))

    def test2_change_same_password(self):
        """
        测试修改相同的密码
        """
        change_password_page = Change_Password_Page(self.driver)
        result = change_password_page.change_same_password()
        if result:
            self.assertTrue(result, logger.info('不能修改成相同的密码'))
        else:
            self.assertTrue(result, logger.error('可以修改成相同的密码'))

    def test3_change_right_password(self):
        """
        测试修改密码
        """
        change_password_page = Change_Password_Page(self.driver)
        result = change_password_page.change_right_password()
        if result:
            self.assertTrue(result, logger.info('修改密码成功.'))
        else:
            self.assertTrue(result, logger.error('修改密码失败!'))


if __name__ == '__main__':
    unittest.main()
