# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.group_management.inspect_management import Inspect_Management_Page
from framework.logger import Logger
logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Inspect_Management(unittest.TestCase):
    """
    测试检视组管理
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

    def test01_check_inspect_info(self):
        """
        测试查看检视组管理信息
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        inspect_management_page.login()
        result = inspect_management_page.check_inspect_info()
        if result:
            self.assertTrue(result, logger.info("查看检视组管理没有问题."))
        else:
            self.assertTrue(result, logger.error("查看检视组管理存在问题!"))

    def test02_delete_inspect(self):
        """
        测试删除检视组
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.delete_inspect()
        if result:
            self.assertTrue(result, logger.info("删除检视组没有问题."))
        else:
            self.assertTrue(result, logger.error("删除检视组存在问题!"))

    def test03_check_create_inspect(self):
        """
        测试创建检视组流程是否有问题
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.check_create_inspect()
        if result:
            self.assertTrue(result, logger.info("创建检视组流程没有问题."))
        else:
            self.assertTrue(result, logger.error("创建检视组流程存在问题!"))

    def test04_cancel_create_inspect(self):
        """
        测试取消创建检视组
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.cancel_create_inspect()
        if result:
            self.assertTrue(result, logger.info("取消创建检视组流程没有问题."))
        else:
            self.assertTrue(result, logger.error("取消创建检视组流程存在问题!"))

    def test05_create_private_inspect(self):
        """
        测试创建私有检视组
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.create_private_inspect()
        if result:
            self.assertTrue(result, logger.info("创建私有检视组没有问题."))
        else:
            self.assertTrue(result, logger.error("创建私有检视组存在问题!"))

    def test05_create_public_inspect(self):
        """
        测试创建公有检视组
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.create_public_inspect()
        if result:
            self.assertTrue(result, logger.info("创建公有检视组没有问题."))
        else:
            self.assertTrue(result, logger.error("创建公有检视组存在问题!"))

    def test06_check_inspector_info(self):
        """
        测试查看检视专家信息
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.check_inspector_info()
        if result:
            self.assertTrue(result, logger.info("查看检视专家信息没有问题."))
        else:
            self.assertTrue(result, logger.error("查看检视专家信息存在问题!"))

    def test07_delete_inspector(self):
        """
        测试删除检视专家
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.delete_inspector()
        if result:
            self.assertTrue(result, logger.info("删除检视专家没有问题."))
        else:
            self.assertTrue(result, logger.error("删除检视专家存在问题!"))

    def test08_create_inspector(self):
        """
        测试增加检视专家
        """
        inspect_management_page = Inspect_Management_Page(self.driver)
        result = inspect_management_page.create_inspector()
        if result:
            self.assertTrue(result, logger.info("增加检视专家没有问题."))
        else:
            self.assertTrue(result, logger.error("增加检视专家存在问题!"))


if __name__ == '__main__':
    unittest.main()
