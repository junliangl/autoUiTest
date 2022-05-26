# coding=utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.group_management.moqi_check_management import Moqi_Check_Management_Page
from framework.logger import Logger
logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Moqi_Check_Management(unittest.TestCase):
    """
    测试用户管理
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

    def test01_cancel_change(self):
        """
        测试取消修改墨奇检视
        """
        moqi_check_management_page = Moqi_Check_Management_Page(self.driver)
        moqi_check_management_page.login()
        result = moqi_check_management_page.cancel_change()
        if result:
            self.assertTrue(result, logger.info("取消修改墨奇检视没有问题."))
        else:
            self.assertTrue(result, logger.error("取消修改墨奇检视存在问题!"))

    def test02_switch_moqi_check(self):
        """
        测试切换墨奇检视开关和数量
        """
        moqi_check_management_page = Moqi_Check_Management_Page(self.driver)
        result = moqi_check_management_page.switch_moqi_check_management()
        if result:
            self.assertTrue(result, logger.info("切换墨奇检视开关和数量没有问题."))
        else:
            self.assertTrue(result, logger.error("切换墨奇检视开关和数量存在问题!"))

    def test03_save_change(self):
        """
        测试保存修改
        """
        moqi_check_management_page = Moqi_Check_Management_Page(self.driver)
        result = moqi_check_management_page.save_change()
        if result:
            self.assertTrue(result, logger.info("保存修改没有问题."))
        else:
            self.assertTrue(result, logger.error("保存修改存在问题!"))


if __name__ == '__main__':
    unittest.main()
