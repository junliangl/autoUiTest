import os
import json
from framework.base_page import BasePage
from selenium.webdriver.common import action_chains

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(project_path, 'config'), 'login.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
account_file = os.path.join(os.path.join(project_path, 'data'), 'account.json')

with open(json_file, encoding='utf-8') as file1:
    login_json = json.load(file1)

with open(method_file, encoding='utf-8') as file2:
    method_json = json.load(file2)

with open(account_file, encoding='utf-8') as file3:
    account_json = json.load(file3)


class Login(BasePage):
    input_username_element = (method_json["method"][0], login_json["account"][0])
    input_password_element = (method_json["method"][0], login_json["password"][0])
    login_button_element = (method_json["method"][0], login_json["login_button"][0])
    superadmin_account = account_json["superadmin"]["account"]
    superadmin_password = account_json["superadmin"]["password"]
    change_password = account_json["change"]["password"]

    def login(self, test):
        if test == 'superadmin':
            self.input(self.superadmin_account, *self.input_username_element)
            self.input(self.superadmin_password, *self.input_password_element)
        elif test == 'change_password':
            # 静态账号调试使用
            # self.input('test006', *self.input_username_element)
            self.input(self.get_account(), *self.input_username_element)
            self.input(self.change_password, *self.input_password_element)
        else:
            # 静态账号调试使用
            # self.input('test006', *self.input_username_element)
            self.input(self.get_account(), *self.input_username_element)
            self.input('aA123456', *self.input_password_element)
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        self.click(*self.login_button_element)
        self.sleep(1)
