import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Logger
from common.browser_info import Browser_Info
from common.base_page import BasePage
from page_objects.common_login.login import Login


logger = Logger(logger='测试流程').get_log()
browser_info = Browser_Info()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'init'), 'accept_invite.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

# 拿到 json 文件解析成 dict
with open(json_file, encoding='utf-8') as file1:
    accept_invite_json = json.load(file1)

with open(method_file, encoding='utf-8') as file2:
    method_json = json.load(file2)

with open(reminder_file, encoding='utf-8') as file3:
    reminder_json = json.load(file3)


class Accept_Invite_Page(BasePage):
    accept = (method_json["method"][0], accept_invite_json["accept"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    accept_reminder = (method_json["method"][0], reminder_json["accept_invite"][0])

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

    def accept_invite(self):
        self.click(*self.accept)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.accept_reminder))
            logger.info(self.get_element(*self.accept_reminder))
            logger.info("接受邀请入组成功.")
            return True
        except Exception:
            logger.error("接受邀请入组失败!")
            logger.error(reminder)
            self.get_windows_img()
            return False
        