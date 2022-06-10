# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.group_management.mobile_police_management import Mobile_Police_Management_Page
from framework.logger import Logger
logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Mobile_Police_Management(unittest.TestCase):
    """
    测试移动警务管理
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

    def test01_check_mobile_police_user(self):
        """
        测试查看移动警务管理信息
        """
        mobile_police_management_page = Mobile_Police_Management_Page(self.driver)
        mobile_police_management_page.login()
        result = mobile_police_management_page.check_mobile_police_user()
        if result:
            self.assertTrue(result, logger.info("查看移动警务管理没有问题."))
        else:
            self.assertTrue(result, logger.error("查看移动警务管理存在问题!"))

    def test02_delete_mobile_police_user(self):
        """
        删除移动警务管理
        """
        mobile_police_management_page = Mobile_Police_Management_Page(self.driver)
        result = mobile_police_management_page.delete_mobile_police_user()
        if result:
            self.assertTrue(result, logger.info("删除移动警务人员没有问题."))
        else:
            self.assertTrue(result, logger.error("删除移动警务人员存在问题!"))

    def test03_create_mobile_police_user(self):
        """
        测试导入 csv 移动警务人员
        """
        mobile_police_management_page = Mobile_Police_Management_Page(self.driver)
        result = mobile_police_management_page.import_mobile_police_file()
        if result:
            self.assertTrue(result, logger.info("导入移动警务管理没有问题."))
        else:
            self.assertTrue(result, logger.error("导入移动警务管理存在问题!"))

    def test04_add_mobile_police_user(self):
        """
        测试增加移动警务人员
        """
        mobile_police_management_page = Mobile_Police_Management_Page(self.driver)
        result = mobile_police_management_page.add_mobile_police_user()
        if result:
            self.assertTrue(result, logger.info("增加移动警务管理没有问题."))
        else:
            self.assertTrue(result, logger.error("增加移动警务管理存在问题!"))


if __name__ == '__main__':
    unittest.main()
