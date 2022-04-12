import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = os.path.join(os.path.join(project_path, 'config'), 'available_quota.json')

with open(json_file, encoding='utf-8') as file:
    available_quota_json = json.load(file)


class Available_quota_Page(BasePage):
    input_username_element = (available_quota_json["method"][0], available_quota_json["account"][0])
    input_password_element = (available_quota_json["method"][0], available_quota_json["password"][0])
    login_button_element = (available_quota_json["method"][0], available_quota_json["login_button"][0])
    username_element = (available_quota_json["method"][0], available_quota_json["username"][0])
    available_quota_element = (available_quota_json["method"][0], available_quota_json["available_quato"][0])
    quota_info_element = (available_quota_json["method"][0], available_quota_json["quota_info"][0])
    quota_list_element = (available_quota_json["method"][0], available_quota_json["quota_list"][0])

    def input_login_message_account(self, text):
        self.input(text, *self.input_username_element)

    def input_login_message_password(self, text):
        self.input(text, *self.input_password_element)

    def time_sleep(self):
        self.sleep(0.5)

    def click_login_button(self):
        self.click(*self.login_button_element)
        self.time_sleep()

    def click_username_button(self):
        self.click(*self.username_element)
        self.time_sleep()

    def click_quota_button(self):
        self.click(*self.available_quota_element)
        self.time_sleep()

    def click_quota_info(self):
        self.click(*self.quota_info_element)
        self.time_sleep()

    # 判断算力信息能否找到自己的域，找不到就说明没有加入域
    def get_result(self):
        # noinspection PyBroadException
        if self.get_element(*self.quota_list_element) == "暂无数据":
            return True
        else:
            return False

