import os
import json
from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'check_group.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    group_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)


class Check_Group_Page(BasePage):
    input_username_element = (method_json["method"][0], group_management_json["account"][0])
    input_password_element = (method_json["method"][0], group_management_json["password"][0])
    login_button_element = (method_json["method"][0], group_management_json["login_button"][0])
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group = (method_json["method"][0], menu_json["setting"]["group"][0])
    group_father_element = (method_json["method"][0], group_management_json["group_father"][0])
    user_access_element = (method_json["method"][0], menu_json["setting"]["user_access"][0])
    group_name = (method_json["method"][0], group_management_json["child_group"]["group_name"][0])

    def input_login_message_account(self, text):
        self.input(text, *self.input_username_element)

    def input_login_message_password(self, text):
        self.input(text, *self.input_password_element)

    def time_sleep(self):
        self.sleep(0.5)

    def click_login_button(self):
        self.click(*self.login_button_element)

    def click_setting_button(self):
        self.click(*self.setting_button_element)

    def click_user_access(self):
        self.click(*self.user_access_element)

    def get_group_number(self):
        self.click_setting_button()
        self.forced_wait(*self.group)
        element = self.driver.find_element(*self.group_father_element)
        return len(element.find_elements(method_json["method"][0], 'li'))

    def get_all_groups(self):
        group = []
        group_number = self.get_group_number()
        for number in range(group_number):
            group_element = (method_json["method"][0], f"/html/body/div[2]/div/div/div/ul/li[last()-{number}]")
            group.append(self.get_element(*group_element))
        return group, group_number

    def get_click_groups_result(self):
        group = self.get_all_groups()
        logger.info(f"当前用户总共有 {group[1]} 个域")
        temp = 0
        for number in range(group[1]):
            group_element = (method_json["method"][0], f"/html/body/div[2]/div/div/div/ul/li[last()-{number}]")
            self.click(*group_element)
            self.sleep(2)
            self.click_user_access()
            self.forced_wait(*self.group_name)
            if self.get_element(*self.group_name) == group[0][number]:
                logger.info(f"这是第 {number + 1} 个域,进入 {group[0][number]} 成功.")
                temp = temp + 1
            else:
                logger.error(f"这是第 {number + 1} 个域,进入 {group[0][number]} 失败!")
            self.click_setting_button()
        # 判定进入当前域管理数量和总域数量是否相同
        if temp == group[1]:
            return True
        else:
            return False