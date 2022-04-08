# coding=utf-8
import unittest
from selenium.webdriver.common.by import By
from framework.browser_engine import BrowserEngine
from framework.browser_info import Message
from page_objects.register import Register_Page
from framework.logger import Logger

logger = Logger(logger='注册测试结果').get_log()
get_message = Message()
register_init_button_element = (By.XPATH,
                                '/html/body/app-root/app-login/div/form/nz-form-item[4]/nz-form-control/div/div/div/a[contains(text(),"注册新账号")]')

class Test_Register(unittest.TestCase):
    """
    测试注册模块
    """

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, *register_init_button_element)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        pass

    def test_register(self):
        """
        测试注册用例
        """
        register_page = Register_Page(self.driver)
        register_page.get_wait_log()
        register_page.click_init_register_button()
        register_page.input_register_message_account('testauto123')  # 测试账号
        register_page.input_register_message_password('aA123456')
        register_page.input_register_message_confirm_password('aA1234567')
        register_page.input_register_message_username('junliangl')
        register_page.choose_register_gender()
        register_page.input_register_message_phone('12345678911')
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

        register_page.input_register_message_company('墨奇科技')
        register_page.get_windows_img()
        register_page.click_register_button()

        # 断言元素注册按钮是否存在，存在就视为注册失败
        if register_page.get_result() is True:
            self.assertFalse(register_page.get_result(), logger.critical('注册失败'))
        else:
            self.assertTrue(register_page.get_result(), logger.info('注册成功'))


if __name__ == '__main__':
    unittest.main()
