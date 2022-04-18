import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger(logger='爬取消息').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = os.path.join(os.path.join(project_path, 'config'), 'message.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    message_json = json.load(file1)

with open(method_file, encoding='utf-8') as file2:
    method_json = json.load(file2)


class Message_Page(BasePage):
    input_username_element = (method_json["method"][0], message_json["account"][0])
    input_password_element = (method_json["method"][0], message_json["password"][0])
    login_button_element = (method_json["method"][0], message_json["login_button"][0])
    message_button_element = (method_json["method"][0], message_json["message_button"][0])
    message_div_element = (method_json["method"][0], message_json["message_div"][0])
    system_message_element = (method_json["method"][0], message_json["system_message"][0])
    detail_button_element = (method_json["method"][0], message_json["detail"][0])
    last_number_element = (method_json["method"][0], message_json["last_number"][0])
    next_page_element = (method_json["method"][0], message_json["next_page"][0])
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

    def get_message_number(self):
        self.forced_wait(*self.last_number_element)
        return int(self.get_element(*self.last_number_element))

    def get_message_header(self):
        header = [self.get_element(*self.data_and_time_element), self.get_element(*self.message_element),
                  self.get_element(*self.action_token_element), self.get_element(*self.time_of_action_element),
                  self.get_element(*self.action_element)]
        return header

    # 暂时未完成
    def get_message_info(self):
        info = []
        temp = 0
        # 遍历每页的每行消息信息
        for i in range(10):
            # 遍历每行的每个消息信息
            for j in range(5):
                # noinspection PyBroadException
                try:
                    message_info_element = ('xpath',
                                            f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-message/div[2]/nz-tabset/div/div/div/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[{i + 1}]/td[{j + 1}]")
                    WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located(message_info_element))
                    info.append(self.get_element(*message_info_element))
                    temp = temp + 1
                except Exception:
                    logger.warning("该页消息爬取完成")
                    return info, temp
                return info, temp
