import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Logger
from common.browser_info import Browser_Info
from common.browser_engine import BrowserEngine
from common.base_page import BasePage


logger = Logger(logger='测试流程').get_log()
browser_info = Browser_Info()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'init'), 'register.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

# 拿到 json 文件解析成 dict
with open(json_file, encoding='utf-8') as file1:
    register_json = json.load(file1)

with open(method_file, encoding='utf-8') as file2:
    method_json = json.load(file2)

with open(reminder_file, encoding='utf-8') as file3:
    reminder_json = json.load(file3)

password = 'aA123456'


class Register_Page(BasePage):
    # method_json 存放定位方法的列表  后面对应存放着对应的方法的元素列表
    init_button_element = (method_json["method"][0], register_json["init_button"][0])
    tianjin_init_button = (method_json["method"][0], register_json["tianjin_init"][0])
    account_element = (method_json["method"][0], register_json["account"][0])
    password1_element = (method_json["method"][0], register_json["password"]["new_password"][0])
    password2_element = (method_json["method"][0], register_json["password"]["confirm_password"][0])
    username_element = (method_json["method"][0], register_json["username"][0])
    male_element = (method_json["method"][0], register_json["gender"]["male"][0])
    female_element = (method_json["method"][0], register_json["gender"]["female"][0])
    phone_number_element = (method_json["method"][0], register_json["phone_number"][0])
    area1_element = (method_json["method"][0], register_json["area"]["area1"][0])
    tianjin_area1_element = (method_json["method"][0], register_json["area"]["tianjin_area1"][0])
    area2_element = (method_json["method"][0], register_json["area"]["area2"][0])
    area3_element = (method_json["method"][0], register_json["area"]["area3"][0])
    area4_element = (method_json["method"][0], register_json["area"]["area4"][0])
    area5_element = (method_json["method"][0], register_json["area"]["area5"][0])
    company_element = (method_json["method"][0], register_json["company"][0])
    enter_button_element = (method_json["method"][0], register_json["enter_button"][0])
    tianjin_enter_button = (method_json["method"][0], register_json["tianjin_enter"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    register_reminder = (method_json["method"][0], reminder_json["register"][0])

    def register_account(self):
        get_login_type = BrowserEngine(self.driver)
        if get_login_type.get_login_type():
            try:
                WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(self.init_button_element))
            except Exception as e:
                logger.error("打开网页太慢!")
                logger.error(e)
                return False
            self.click(*self.init_button_element)
            self.input(self.get_random_account(), *self.account_element)
            # 设定好默认密码,当然也可以通过以下设置随机密码
            self.input(password, *self.password1_element)
            # 确认密码
            self.input(password, *self.password2_element)
            self.input(self.get_random_name(), *self.username_element)
            self.click(*self.female_element)
            self.input(self.get_random_name() + self.get_random_number(), *self.phone_number_element)
            self.click(*self.area1_element)
            if browser_info.get_driver() == 'Chrome':
                self.actionchains_click(*self.area2_element)
                self.actionchains_click(*self.area3_element)
                self.actionchains_click(*self.area4_element)
                self.actionchains_click(*self.area5_element)
            else:
                self.click(*self.area2_element)
                self.click(*self.area3_element)
                self.click(*self.area4_element)
                self.click(*self.area5_element)
            self.input(self.get_random_name(), *self.company_element)
            self.click(*self.enter_button_element)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.register_reminder))
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.init_button_element))
                logger.info(self.get_element(*self.register_reminder))
                self.get_windows_img()
                return True
            except Exception:
                logger.error("注册失败!")
                logger.error(reminder)
                self.get_windows_img()
                return False
        else:
            try:
                WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(self.tianjin_init_button))
            except Exception as e:
                logger.error("打开网页太慢!")
                logger.error(e)
                return False
            self.click(*self.tianjin_init_button)
            self.input(self.get_random_account(), *self.account_element)
            # 设定好默认密码,当然也可以通过以下设置随机密码
            self.input(password, *self.password1_element)
            # 确认密码
            self.input(password, *self.password2_element)
            self.input(self.get_random_name(), *self.username_element)
            self.click(*self.female_element)
            self.input(self.get_random_name() + self.get_random_number(), *self.phone_number_element)
            self.click(*self.tianjin_area1_element)
            if browser_info.get_driver() == 'Chrome':
                self.actionchains_click(*self.area2_element)
                self.actionchains_click(*self.area3_element)
                self.actionchains_click(*self.area4_element)
                self.actionchains_click(*self.area5_element)
            else:
                self.click(*self.area2_element)
                self.click(*self.area3_element)
                self.click(*self.area4_element)
                self.click(*self.area5_element)
            self.input(self.get_random_name(), *self.company_element)
            self.click(*self.tianjin_enter_button)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.register_reminder))
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.tianjin_init_button))
                logger.info(self.get_element(*self.register_reminder))
                self.get_windows_img()
                return True
            except Exception:
                logger.error("注册失败!")
                logger.error(reminder)
                self.get_windows_img()
                return False

