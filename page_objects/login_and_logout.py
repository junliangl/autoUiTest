import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = os.path.join(os.path.join(project_path, 'config'), 'login_and_logout.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    login_json = json.load(file1)

with open(method_file, encoding='utf-8') as file2:
    method_json = json.load(file2)


class Login_And_Logout_Page(BasePage):
    input_username_element = (method_json["method"][0], login_json["account"][0])
    input_password_element = (method_json["method"][0], login_json["password"][0])
    login_button_element = (method_json["method"][0], login_json["login_button"][0])
    username_element = (method_json["method"][0], login_json["username"][0])
    logout_button_element = (method_json["method"][0], login_json["logout_button"][0])
    cancel_button_element = (method_json["method"][0], login_json["cancel_button"][0])
    confirm_button_element = (method_json["method"][0], login_json["confirm_button"][0])

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

    def click_logout_button(self):
        self.click(*self.logout_button_element)
        self.time_sleep()

    def click_cancel_button(self):
        self.click(*self.cancel_button_element)
        self.time_sleep()

    def click_confirm_button(self):
        self.click(*self.confirm_button_element)
        self.time_sleep()

    def get_login_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到人员名字，找不到就视为登录成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False

    def get_cancel_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否回到之前的页面，回到就视为取消注销成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False

    def get_logout_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到登录按钮，找到就视为注销成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.login_button_element))
            return True
        except Exception:
            return False
