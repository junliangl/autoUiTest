import os
import json
from framework.base_page import BasePage

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'available_quota.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    available_quota_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)


class Available_Quota_Page(BasePage):
    input_username_element = (method_json["method"][0], available_quota_json["account"][0])
    input_password_element = (method_json["method"][0], available_quota_json["password"][0])
    login_button_element = (method_json["method"][0], available_quota_json["login_button"][0])
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    available_quota_element = (method_json["method"][0], menu_json["user"]["available_quota"][0])
    quota_info_element = (method_json["method"][0], available_quota_json["quota_info"][0])
    quota_list_element = (method_json["method"][0], available_quota_json["quota_list"][0])

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

