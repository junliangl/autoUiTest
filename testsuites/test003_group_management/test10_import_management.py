# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.group_management.import_management import Import_Management_Page
from framework.logger import Logger
logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Import_Management(unittest.TestCase):
    """
    测试入库设置
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

    def test01_check_import_settings(self):
        """
        测试查看入库设置
        """
        import_page = Import_Management_Page(self.driver)
        import_page.login()
        result = import_page.check_import_settings()
        if result:
            self.assertTrue(result, logger.debug("入库设置没有问题."))
        else:
            self.assertTrue(result, logger.error("入库设置存在问题!"))

    def test02_check_create_import_settings_button(self):
        """
        测试检查新建入库设置的buttons
        """
        import_page = Import_Management_Page(self.driver)
        result = import_page.check_create_import_settings_button()
        if result:
            self.assertTrue(result, logger.debug("新建入库设置buttons没有问题."))
        else:
            self.assertTrue(result, logger.error("新建入库设置buttons存在问题!"))

    def test03_switch_import_settings_button(self):
        """
        测试切换新建入库设置的buttons
        """
        import_page = Import_Management_Page(self.driver)
        result = import_page.switch_import_settings_button()
        if result:
            self.assertTrue(result, logger.debug("切换新建入库设置buttons没有问题."))
        else:
            self.assertTrue(result, logger.error("切换新建入库设置buttons存在问题!"))

    def test04_create_import_settings(self):
        """
        测试新建入库设置
        """
        import_page = Import_Management_Page(self.driver)
        result = import_page.create_import_settings()
        if result:
            self.assertTrue(result, logger.debug("新建入库设置没有问题."))
        else:
            self.assertTrue(result, logger.error("新建入库设置存在问题!"))

    def test05_delete_import_settings(self):
        """
        测试删除入库设置
        """
        import_page = Import_Management_Page(self.driver)
        result = import_page.delete_import_settings()
        if result:
            self.assertTrue(result, logger.debug("删除入库设置没有问题."))
        else:
            self.assertTrue(result, logger.error("删除入库设置存在问题!"))


if __name__ == '__main__':
    unittest.main()

