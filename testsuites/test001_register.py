# coding=utf-8
import os
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from framework.browser_info import Message
from page_objects.register import Register_Page
from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
get_message = Message()
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(os.path.join(project_path, 'data'), 'register_data.json')


@ddt
class Test_Register(unittest.TestCase):
    """
    测试注册模块
    """

    # @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.driver.close()

    # 拿到json里的数据进行数据驱动测试
    @file_data(data_path)
    def test_register(self, account, first_password, second_password, username, gender, phone_number, company):
        """
        测试注册用例
        """
        register_page = Register_Page(self.driver)
        register_page.get_wait_log()
        register_page.click_init_register_button()
        register_page.input_register_message_account(account)
        register_page.input_register_message_password(first_password)
        register_page.input_register_message_confirm_password(second_password)
        register_page.input_register_message_username(username)
        register_page.choose_register_gender(gender)
        register_page.input_register_message_phone(phone_number)
        register_page.choose_area1()  # 选择区域

        # 判断浏览器用不同方法点击
        if get_message.get_driver() == "Chrome":
            register_page.choose_chrome_area2()  # 选择公安部
            register_page.choose_chrome_area3()  # 选择四川省
            register_page.choose_chrome_area4()  # 选择成都市
            register_page.choose_chrome_area5()  # 选择武侯区

        elif get_message.get_driver() == "Firefox":
            register_page.choose_firefox_area2()  # 选择公安部
            register_page.choose_firefox_area3()  # 选择四川省
            register_page.choose_firefox_area4()  # 选择成都市
            register_page.choose_firefox_area5()  # 选择武侯区

        register_page.input_register_message_company(company)
        register_page.get_windows_img()
        register_page.click_register_button()

        # 断言元素注册按钮是否存在，存在就视为注册失败
        if register_page.get_result() is True:
            self.assertFalse(register_page.get_result(), logger.critical('注册失败'))
        else:
            self.assertTrue(register_page.get_result(), logger.info('注册成功'))


if __name__ == '__main__':
    unittest.main()
