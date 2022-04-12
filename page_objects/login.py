import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = os.path.join(os.path.join(project_path, 'config'), 'login.json')

with open(json_file, encoding='utf-8') as file:
    login_json = json.load(file)


class Login_Page(BasePage):
    input_username_element = (login_json["method"][0], login_json["account"][0])
    input_password_element = (login_json["method"][0], login_json["password"][0])
    login_button_element = (login_json["method"][0], login_json["login_button"][0])
    username_element = (login_json["method"][0], login_json["username"][0])

    def input_login_message_account(self, text):
        self.input(text, *self.input_username_element)

    def input_login_message_password(self, text):
        self.input(text, *self.input_password_element)

    def time_sleep(self):
        self.sleep(1)

    def click_login_button(self):
        self.click(*self.login_button_element)
        self.time_sleep()

    # 判断是否能找到某一元素，找不到就视为注册成功
    def get_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到人员名字，找不到就视为登录成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False


