import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'message.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    message_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)


class Message_Page(BasePage):
    input_username_element = (method_json["method"][0], message_json["account"][0])
    input_password_element = (method_json["method"][0], message_json["password"][0])
    login_button_element = (method_json["method"][0], message_json["login_button"][0])
    message_button_element = (method_json["method"][0], menu_json["message"]["button"][0])
    message_div_element = (method_json["method"][0], menu_json["message"]["message_div"][0])
    system_message_element = (method_json["method"][0], menu_json["message"]["system_message_1"][0])
    detail_button_element = (method_json["method"][0], menu_json["message"]["detail"][0])
    next_page_element = (method_json["method"][0], message_json["next_page"][0])
    last_page_element = (method_json["method"][0], message_json["last_page"][0])
    data_and_time_element = (method_json["method"][0], message_json["data_and_time"][0])
    message_element = (method_json["method"][0], message_json["message"][0])
    action_token_element = (method_json["method"][0], message_json["action_token"][0])
    time_of_action_element = (method_json["method"][0], message_json["time_of_action"][0])
    action_element = (method_json["method"][0], message_json["action"][0])

    def input_login_message_account(self, text):
        self.input(text, *self.input_username_element)

    def input_login_message_password(self, text):
        self.input(text, *self.input_password_element)

    def time_sleep(self):
        self.sleep(0.5)

    def click_login_button(self):
        self.click(*self.login_button_element)

    def click_message_button(self):
        self.click(*self.message_button_element)

    def click_detail_button(self):
        self.click(*self.detail_button_element)

    def click_next_page(self):
        self.click(*self.next_page_element)

    def get_message_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到消息 div ，找到就视为打开消息成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.message_div_element))
            return True
        except Exception:
            return False

    def get_system_message_number(self):
        self.forced_wait(*self.system_message_element)
        return self.get_element(*self.system_message_element)

    def get_message_header(self):
        WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.action_element))
        header = [self.get_element(*self.data_and_time_element), self.get_element(*self.message_element),
                  self.get_element(*self.action_token_element), self.get_element(*self.time_of_action_element),
                  self.get_element(*self.action_element)]
        return header

    # 得到每一页的信息
    def get_message_info(self):
        info = []
        while True:
            for i in range(10):
                # 遍历每行的每个消息信息
                for j in range(5):
                    message_info_element = ('xpath', f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-message/div[2]/nz-tabset/div/div/div[1]/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[{i + 1}]/td[{j + 1}]")
                    # noinspection PyBroadException
                    try:
                        WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(message_info_element))
                        info.append(self.get_element(*message_info_element))
                    except Exception:
                        return info, len(info)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 2, 0.5).until(EC.presence_of_element_located(self.last_page_element))
                break
            except Exception:
                self.click(*self.next_page_element)
        return info, len(info)
