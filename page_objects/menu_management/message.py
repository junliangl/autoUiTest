import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from framework.logger import Logger
from page_objects.common_login.login import Login

logger = Logger(logger='测试流程').get_log()
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
    message_button_element = (method_json["method"][0], menu_json["message"]["button"][0])
    message_number = (method_json["method"][0], menu_json["message"]["message_number"][0])
    message_div_element = (method_json["method"][0], menu_json["message"]["message_div"][0])
    detail_button_element = (method_json["method"][0], menu_json["message"]["detail"][0])
    next_page_element = (method_json["method"][0], message_json["next_page"][0])
    last_page_element = (method_json["method"][0], message_json["last_page"][0])
    data_and_time_element = (method_json["method"][0], message_json["data_and_time"][0])
    message_element = (method_json["method"][0], message_json["message"][0])
    action_token_element = (method_json["method"][0], message_json["action_token"][0])
    time_of_action_element = (method_json["method"][0], message_json["time_of_action"][0])
    action_element = (method_json["method"][0], message_json["action"][0])

    def login(self):
        # 以下为调试使用
        # login = Login(self.driver)
        # login.login('')

        if self.get_account():
            login = Login(self.driver)
            # 参数为'superadmin'就登录superadmin账号，其他则登录注册成功的账号
            login.login('')
        else:
            raise Exception('登录账号为空!')

    def get_uncheck_message_number(self):
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.message_number))
            message_number = self.get_element(*self.message_number)
            return int(message_number)
        except Exception:
            return 0

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

    def get_message_result(self):
        self.click(*self.message_button_element)
        # noinspection PyBroadException
        try:
            # 判断是否能找到消息 div ，找到就视为打开消息成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.message_div_element))
            self.sleep(2)
            # 获取未读消息的数量
            uncheck_number = self.get_uncheck_message_number()
            if uncheck_number != '0':
                logger.warning(f"还有未查看的消息,消息数为：{uncheck_number}")
                # 循环遍历所有消息
                # self.click(*self.detail_button_element)
                # info = self.get_message_info()
                # all_info = info[0]
                # number = info[1]
                # message_number = int(number / 5)
                # logger.info(f"总共有：{message_number} 条消息")
                # for text in range(message_number):
                #     logger.warning(f"下面是第{text + 1 }条消息:")
                #     for title in range(5):
                #         logger.info(f"{self.get_message_header()[title]} : {all_info[text * 5 + title]}")
                # # for text in range(number):
                # #     logger.info(f"{self.get_message_header()[text % 5]} : {all_info[text]}")
                # logger.info("查看消息完成")
            else:
                logger.info("当前待查看消息为：0")
            return True
        except Exception:
            return False

