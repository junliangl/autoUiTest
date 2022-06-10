# coding=utf-8
import os
import sys
project = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project)
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.import_file.import_file_page import Import_File_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Import_Page(unittest.TestCase):
    """
    测试导入功能
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

    def test01_enter_import_page(self):
        """
        测试进入导入页
        """
        import_page = Import_File_Page(self.driver)
        import_page.login()
        result = import_page.enter_import_file_page()
        if result:
            self.assertTrue(result, logger.debug('进入导入页没有问题.'))
        else:
            self.assertTrue(result, logger.error('进入导入页存在问题!'))

    def test02_check_buttons(self):
        """
        测试查看默认buttons
        """
        import_page = Import_File_Page(self.driver)
        result = import_page.check_default_buttons()
        if result:
            self.assertTrue(result, logger.debug('查看buttons问题.'))
        else:
            self.assertTrue(result, logger.error('buttons存在问题!'))

    def test03_switch_buttons(self):
        """
        测试切换按钮
        """
        import_page = Import_File_Page(self.driver)
        result = import_page.switch_buttons()
        if result:
            self.assertTrue(result, logger.debug('切换按钮没有问题.'))
        else:
            self.assertTrue(result, logger.error('切换按钮存在问题!'))


if __name__ == '__main__':
    unittest.main()
