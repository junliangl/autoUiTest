import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
element_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'change_password.json')
login_file = os.path.join(os.path.join(project_path, 'config'), 'login.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(element_file, encoding='utf-8') as file1:
    change_password_json = json.load(file1)

with open(login_file, encoding='utf-8') as file2:
    login_json = json.load(file2)

with open(menu_file, encoding='utf-8') as file3:
    menu_json = json.load(file3)

with open(method_file, encoding='utf-8') as file4:
    method_json = json.load(file4)


class Change_Password_Page(BasePage):
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    change_password_element = (method_json["method"][0], menu_json["user"]["change_password"][0])
    initial_password_element = (method_json["method"][0], change_password_json["initial_password"][0])
    new_password_element = (method_json["method"][0], change_password_json["new_password"][0])
    confirm_password_element = (method_json["method"][0], change_password_json["confirm_password"][0])
    confirm_button_element = (method_json["method"][0], change_password_json["confirm_button"][0])
    cancel_button_element = (method_json["method"][0], change_password_json["cancel_button"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def get_cancel_result(self):
        self.click(*self.username_element)
        self.click(*self.change_password_element)
        self.click(*self.cancel_button_element)
        # noinspection PyBroadException
        try:
            # 判断是否能找到 username 元素，找到就视为取消修改密码成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False

    def get_change_result(self, original_password, new_password, confirm_password):
        self.click(*self.username_element)
        self.click(*self.change_password_element)
        self.input(original_password, *self.initial_password_element)
        self.input(new_password, *self.new_password_element)
        self.input(confirm_password, *self.confirm_password_element)
        self.click(*self.confirm_button_element)
        # noinspection PyBroadException
        try:
            # 判断是否能找到确认按钮，找不到就视为修改密码成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.confirm_button_element))
            return False
        except Exception:
            return True

