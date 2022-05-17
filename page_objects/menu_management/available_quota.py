import os
import json
from framework.base_page import BasePage
from page_objects.common_login.login import Login

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
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    available_quota_element = (method_json["method"][0], menu_json["user"]["available_quota"][0])
    quota_info_element = (method_json["method"][0], available_quota_json["quota_info"][0])
    quota_list_element = (method_json["method"][0], available_quota_json["quota_list"][0])

    def login(self):
        login = Login(self.driver)
        login.login('uninvited')

    def click_quota_info(self):
        self.click(*self.quota_info_element)

    # 判断算力信息能否找到自己的域，找不到就说明没有加入域
    def get_result(self):
        self.click(*self.username_element)
        self.click(*self.available_quota_element)
        # noinspection PyBroadException
        self.forced_wait(*self.quota_list_element)
        if self.get_element(*self.quota_list_element) == "暂无数据":
            return True
        else:
            return False

