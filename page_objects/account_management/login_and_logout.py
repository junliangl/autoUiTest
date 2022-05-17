import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login


project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'init'), 'login_and_logout.json')
login_file = os.path.join(os.path.join(project_path, 'config'), 'login.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    login_and_logout_json = json.load(file1)

with open(login_file, encoding='utf-8') as file2:
    login_json = json.load(file2)

with open(menu_file, encoding='utf-8') as file3:
    menu_json = json.load(file3)

with open(method_file, encoding='utf-8') as file4:
    method_json = json.load(file4)


class Login_And_Logout_Page(BasePage):
    login_button_element = (method_json["method"][0], login_json["login_button"][0])
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    logout_button_element = (method_json["method"][0], menu_json["user"]["log_out"][0])
    cancel_button_element = (method_json["method"][0], login_and_logout_json["cancel_button"][0])
    confirm_button_element = (method_json["method"][0], login_and_logout_json["confirm_button"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def get_login_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到人员名字，找不到就视为登录成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False

    def get_cancel_result(self):
        self.click(*self.username_element)
        self.click(*self.logout_button_element)
        self.click(*self.cancel_button_element)
        # noinspection PyBroadException
        try:
            # 判断是否回到之前的页面，回到就视为取消注销成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False

    def get_logout_result(self):
        self.click(*self.username_element)
        self.click(*self.logout_button_element)
        self.click(*self.confirm_button_element)
        # noinspection PyBroadException
        try:
            # 判断是否能找到登录按钮，找到就视为注销成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.login_button_element))
            return True
        except Exception:
            return False
