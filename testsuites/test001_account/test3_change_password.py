# coding=utf-8
import os
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from page_objects.account_management.change_password import Change_Password_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
change_password_file = os.path.join(os.path.join(project_path, 'data'), 'change_password')
data_path = os.path.join(change_password_file, 'change_password_data.json')


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

    def test01_cancel_change_password(self):
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
            self.assertTrue(result, logger.critical('取消修改密码失败'))

    @file_data(data_path)
    def test02_change_password(self, password, new_password, confirm_password):
        """
        测试修改密码
        """
        change_password_page = Change_Password_Page(self.driver)
        result = change_password_page.get_change_result(password, new_password, confirm_password)

        # 如果找到确认按钮那么判定修改密码失败
        if result:
            self.assertTrue(result, logger.info('修改密码成功'))
        else:
            self.assertTrue(result, logger.critical('修改密码失败'))


if __name__ == '__main__':
    unittest.main()
