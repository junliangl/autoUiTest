# coding=utf-8
# 当前文件的绝对路径

import os
import sys
now_path = os.path.dirname(os.path.abspath(__file__))
# 找到根目录
root_path = os.path.dirname(now_path)
# 添加进根目录
sys.path.append(root_path)
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from page_objects.message import Message_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains

logger = Logger(logger='测试结果').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(os.path.join(project_path, 'data'), 'message_data.json')


@ddt
class Test_Message(unittest.TestCase):
    """
    测试登录模块
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

    @file_data(data_path)
    def test_message(self, account, password):
        """
        测试查看消息用例
        """
        message_page = Message_Page(self.driver)
        message_page.input_login_message_account(account)
        message_page.input_login_message_password(password)
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
        message_page.click_login_button()
        message_page.click_message_button()
        if message_page.get_message_result() is True:
            self.assertTrue(message_page.get_message_result(), logger.info('消息框成功打开，查看消息成功'))
            # 获取未读消息的数量
            number = message_page.get_system_message_number()[6:len(message_page.get_system_message_number()) - 1]
            if number != '0':
                logger.warning(f"还有未查看的消息,消息数为：{number}")
                # 遍历每一页直到最后一页
            # else:
            #     logger.info("当前待查看消息为：0")
            # message_page.click_detail_button()
            # for i in range(message_page.get_message_number() - 1):
            #     # 总共有有多少行
            #     raw_number = message_page.get_message_info()[1]
            #     for j in range(raw_number):
            #         logger.info(f"{message_page.get_message_header()[j % 5]} ：{message_page.get_message_info()[0][j]}")
            #     # 遍历完一页就点击下一页
            #     message_page.click_next_page()
            logger.info("查看消息完成")
        else:
            self.assertTrue(message_page.get_message_result(), logger.info('查看消息失败'))


if __name__ == '__main__':
    unittest.main()
