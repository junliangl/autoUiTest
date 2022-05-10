import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
element_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'change_password.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
data_file = os.path.join(os.path.join(project_path, 'data'), 'change_password_data.json')
with open(element_file, encoding='utf-8') as file1:
    change_password_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(data_file, encoding='utf-8') as file4:
    password_json = json.load(file4)

password = password_json["test1"]["password"]


class Change_Password_Page(BasePage):
    input_username_element = (method_json["method"][0], change_password_json["account"][0])
    input_password_element = (method_json["method"][0], change_password_json["password"][0])
    login_button_element = (method_json["method"][0], change_password_json["login_button"][0])
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    change_password_element = (method_json["method"][0], menu_json["user"]["change_password"][0])
    initial_password_element = (method_json["method"][0], change_password_json["initial_password"][0])
    new_password_element = (method_json["method"][0], change_password_json["new_password"][0])
    confirm_password_element = (method_json["method"][0], change_password_json["confirm_password"][0])
    confirm_button_element = (method_json["method"][0], change_password_json["confirm_button"][0])
    cancel_button_element = (method_json["method"][0], change_password_json["cancel_button"][0])

    def input_login_message_account(self, text):
        self.input(text, *self.input_username_element)

    def input_login_message_password(self):
        self.input(password, *self.input_password_element)

    def input_initial_password(self, text):
        self.input(text, *self.initial_password_element)

    def input_new_password(self, text):
        self.input(text, *self.new_password_element)

    def input_confirm_password(self, text):
        self.input(text, *self.confirm_password_element)

    def time_sleep(self):
        self.sleep(0.5)

    def click_login_button(self):
        self.click(*self.login_button_element)
        self.time_sleep()

    def click_username_button(self):
        self.click(*self.username_element)
        self.time_sleep()

    def click_change_password_button(self):
        self.click(*self.change_password_element)
        self.time_sleep()

    def click_confirm_button(self):
        self.click(*self.confirm_button_element)
        self.time_sleep()

    def click_cancel_button(self):
        self.click(*self.cancel_button_element)
        self.time_sleep()

    def get_change_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到确认按钮，找不到就视为修改密码成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.confirm_button_element))
            return False
        except Exception:
            return True

    def get_cancel_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到 username 元素，找到就视为取消修改密码成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False

