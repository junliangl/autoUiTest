import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'init'), 'register.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

# 拿到 json 文件解析成 dict
with open(json_file, encoding='utf-8') as file1:
    register_json = json.load(file1)

with open(method_file, encoding='utf-8') as file2:
    method_json = json.load(file2)


class Register_Page(BasePage):
    # method_json 存放定位方法的列表  后面对应存放着对应的方法的元素列表
    register_init_button_element = (method_json["method"][0], register_json["init_button"][0])
    register_account_element = (method_json["method"][0], register_json["account"][0])
    register_password1_element = (method_json["method"][0], register_json["password"]["new_password"][0])
    register_password2_element = (method_json["method"][0], register_json["password"]["confirm_password"][0])
    register_username_element = (method_json["method"][0], register_json["username"][0])
    register_male_element = (method_json["method"][0], register_json["gender"]["male"][0])
    register_female_element = (method_json["method"][0], register_json["gender"]["female"][0])
    register_phone_number_element = (method_json["method"][0], register_json["phone_number"][0])
    register_area1_element = (method_json["method"][0], register_json["area"]["area1"][0])
    register_area2_element = (method_json["method"][0], register_json["area"]["area2"][0])
    register_area3_element = (method_json["method"][0], register_json["area"]["area3"][0])
    register_area4_element = (method_json["method"][0], register_json["area"]["area4"][0])
    register_area5_element = (method_json["method"][0], register_json["area"]["area5"][0])
    register_company_element = (method_json["method"][0], register_json["company"][0])
    register_enter_button_element = (method_json["method"][0], register_json["enter_button"][0])

    def input_register_message_account(self, text):
        self.input(text, *self.register_account_element)

    def input_register_message_password(self, text):
        self.input(text, *self.register_password1_element)

    def input_register_message_confirm_password(self, text):
        self.input(text, *self.register_password2_element)

    def input_register_message_username(self, text):
        self.input(text, *self.register_username_element)

    def choose_register_gender(self, gender):
        if gender == "男":
            self.click(*self.register_male_element)
        elif gender == "女":
            self.click(*self.register_female_element)

    def input_register_message_phone(self, text):
        self.input(text, *self.register_phone_number_element)

    def choose_area1(self):
        self.click(*self.register_area1_element)

    # chromedriver 的点击方式
    def choose_chrome_area2(self):
        self.actionchains_click(*self.register_area2_element)

    def choose_chrome_area3(self):
        self.actionchains_click(*self.register_area3_element)

    def choose_chrome_area4(self):
        self.actionchains_click(*self.register_area4_element)

    def choose_chrome_area5(self):
        self.actionchains_click(*self.register_area5_element)

    # geckodriver 的点击方式
    def choose_firefox_area2(self):
        self.click(*self.register_area2_element)

    def choose_firefox_area3(self):
        self.click(*self.register_area3_element)

    def choose_firefox_area4(self):
        self.click(*self.register_area4_element)

    def choose_firefox_area5(self):
        self.click(*self.register_area5_element)

    def input_register_message_company(self, text):
        self.input(text, *self.register_company_element)

    def click_init_register_button(self):
        self.click(*self.register_init_button_element)

    def click_register_button(self):
        self.click(*self.register_enter_button_element)

    def get_wait_log(self):
        self.get_wait_element(*self.register_init_button_element)

    def get_result(self):
        # noinspection PyBroadException
        try:
            # 判断是否能找到注册按钮，找不到就视为注册成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.register_enter_button_element))
            return True
        except Exception:
            return False

    def time_sleep(self):
        self.sleep(1.5)
