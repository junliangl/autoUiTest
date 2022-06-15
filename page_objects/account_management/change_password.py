import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.base_page import BasePage
from page_objects.common_login.login import Login

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
element_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'change_password.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(element_file, encoding='utf-8') as file1:
    change_password_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)

result = None


class Change_Password_Page(BasePage):
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    change_password_element = (method_json["method"][0], menu_json["user"]["change_password"][0])
    initial_password_element = (method_json["method"][0], change_password_json["initial_password"][0])
    new_password_element = (method_json["method"][0], change_password_json["new_password"][0])
    confirm_password_element = (method_json["method"][0], change_password_json["confirm_password"][0])
    confirm_button_element = (method_json["method"][0], change_password_json["confirm_button"][0])
    cancel_button_element = (method_json["method"][0], change_password_json["cancel_button"][0])
    change_success = (method_json["method"][0], change_password_json["change_success"][0])
    change_success_button = (method_json["method"][0], change_password_json["change_success_button"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    same_password_reminder = (method_json["method"][0], reminder_json["change_same_password"][0])

    def login(self):
        # 以下为调试使用
        login = Login(self.driver)
        login.login('')

        # if self.get_account():
        #     login = Login(self.driver)
        #     # 参数为'superadmin'就登录superadmin账号，其他则登录注册成功的账号
        #     login.login('')
        # else:
        #     raise Exception('登录账号为空!')

    def get_cancel_result(self):
        self.click(*self.username_element)
        self.click(*self.change_password_element)
        self.click(*self.cancel_button_element)
        # noinspection PyBroadException
        try:
            # 判断是否能找到 username 元素，找到就视为取消修改密码成功
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.username_element))
            logger.info("取消修改密码成功.")
            return True
        except Exception:
            logger.error("取消修改密码失败!")
            self.get_windows_img()
            return False

    def change_same_password(self):
        global result
        self.refresh_browser()
        self.click(*self.username_element)
        self.click(*self.change_password_element)
        # 修改成相同的密码防止忘记.
        self.input('aA123456', *self.initial_password_element)
        self.input('aA123456', *self.new_password_element)
        self.input('aA123456', *self.confirm_password_element)
        self.click(*self.confirm_button_element)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            # 判断是否弹出修改密码成功弹窗
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.same_password_reminder))
            logger.info(self.get_element(*self.same_password_reminder))
            result = True
            return True
        except Exception:
            logger.error("提示有问题!")
            logger.error(reminder)
            self.get_windows_img()
            result = False
            return False

    def change_right_password(self):
        global result
        if result:
            self.input('Aa123456', *self.new_password_element)
            self.input('Aa123456', *self.confirm_password_element)
            self.click(*self.confirm_button_element)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.change_success))
                logger.info("修改密码成功.")
                self.click(*self.change_success_button)
                return True
            except Exception:
                logger.error("修改密码失败!")
                self.get_windows_img()
                result = False
                return False
        else:
            logger.error("上一个测试用例执行失败,该测试用例视为失败!")
            result = False
            return False

    def restore_initial_password(self):
        if result:
            self.refresh_browser()
            login = Login(self.driver)
            login.login('change_password')
            self.click(*self.username_element)
            self.click(*self.change_password_element)
            # 修改成相同的密码防止忘记.
            self.input('Aa123456', *self.initial_password_element)
            self.input('aA123456', *self.new_password_element)
            self.input('aA123456', *self.confirm_password_element)
            self.click(*self.confirm_button_element)
            self.sleep(1)
            logger.info("恢复密码 'aA123456' 成功.")
        else:
            logger.info("上一个测试用例失败,不恢复密码!")
