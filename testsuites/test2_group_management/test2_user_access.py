# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from page_objects.group_management.user_access import User_Access_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_User_Access(unittest.TestCase):
    """
    测试查看用户权限管理
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

    def test1_check_group(self):
        """
        测试查看当前子用户组
        """
        user_access_page = User_Access_Page(self.driver)
        user_access_page.login()
        user_access_page.click_setting_button()
        user_access_page.click_group_button()
        user_access_page.click_user_access()
        user_access_page.sleep(7)
        result = user_access_page.get_group_info()
        if result:
            self.assertTrue(result, logger.info('所有用户组无误.'))
        else:
            self.assertTrue(result, logger.error('用户组存在问题!'))

    def test2_edit_basic(self):
        """
        测试编辑子用户组的基本信息
        """
        user_access_page = User_Access_Page(self.driver)
        result = user_access_page.edit_basic_information('test_' + user_access_page.get_random_name())
        if result:
            self.assertTrue(result, logger.info('修改用户组基础信息没有问题.'))
        else:
            self.assertTrue(result, logger.error('修改用户组的基础信息存在问题!'))

    def test3_users_management(self):
        """
        测试查看用户
        """
        user_access_page = User_Access_Page(self.driver)
        user_access_page.get_user_info()

    def test4_invite_to_group(self):
        """
        测试邀请入组
        """
        user_access_page = User_Access_Page(self.driver)
        result = user_access_page.invite_group()
        if result:
            self.assertTrue(result, logger.info('邀请用户入组没有问题.'))
        else:
            self.assertTrue(result, logger.error('邀请用户入组存在问题!'))

    def test5_delete_roles(self):
        """
        测试删除角色组
        """
        user_access_page = User_Access_Page(self.driver)
        result = user_access_page.delete_roles('Aa123456')
        if result:
            self.assertTrue(result, logger.info('删除角色组没有问题.'))
        else:
            self.assertTrue(result, logger.error('删除角色组存在问题!'))

    def test6_delete_groups(self):
        """
        测试删除子用户组
        """
        user_access_page = User_Access_Page(self.driver)
        result = user_access_page.delete_groups('aA123456')
        user_access_page.sleep(3)
        if result:
            self.assertTrue(result, logger.info('删除子用户组没有问题.'))
        else:
            self.assertTrue(result, logger.error('删除子用户组存在问题!'))

    def test7_add_group(self):
        """
        测试添加子用户组
        """
        user_access_page = User_Access_Page(self.driver)
        random_name = user_access_page.get_random_name()
        random_number = user_access_page.get_random_number()
        result = user_access_page.add_group(random_name, random_number)
        user_access_page.sleep(3)
        if result:
            self.assertTrue(result, logger.info("添加子用户组没有问题."))
        else:
            self.assertTrue(result, logger.error("添加子用户组存在问题!"))

    def test8_add_role(self):
        """
        测试添加角色组
        """
        user_access_page = User_Access_Page(self.driver)
        random_name = user_access_page.get_random_name()
        result = user_access_page.add_role(random_name)
        user_access_page.sleep(3)
        if result:
            self.assertTrue(result, logger.info("添加角色组没有问题."))
        else:
            self.assertTrue(result, logger.error("添加角色组存在问题!"))


if __name__ == '__main__':
    unittest.main()
