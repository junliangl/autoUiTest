import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'auth_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    auth_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)


class Auth_Management_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_auth_management_element = (method_json["method"][0], menu_json["cd1_setting"]["auth_management"][0])
    staging_auth_management_element = (method_json["method"][0], menu_json["staging_setting"]["auth_management"][0])
    permission_granted = (method_json["method"][0], auth_management_json["header"]["permission_granted"][0])
    auth_count_available = (method_json["method"][0], auth_management_json["header"]["auth_count_available"][0])
    auth_amount_used = (method_json["method"][0], auth_management_json["header"]["auth_amount_used"][0])
    activated_amount = (method_json["method"][0], auth_management_json["header"]["activated_amount"][0])
    inactivated_amount = (method_json["method"][0], auth_management_json["header"]["inactivated_amount"][0])
    banned_amount = (method_json["method"][0], auth_management_json["header"]["banned_amount"][0])
    generate_auth_code = (method_json["method"][0], auth_management_json["generate_auth_code"]["button"][0])
    amount_input = (method_json["method"][0], auth_management_json["generate_auth_code"]["amount_input"][0])
    remark_input = (method_json["method"][0], auth_management_json["generate_auth_code"]["remark_input"][0])
    auth_body = (method_json["method"][0], auth_management_json["auth_info"]["auth_body"][0])
    remark = (method_json["method"][0], auth_management_json["auth_info"]["first_auth_admin"]["remark"][0])
    search_input = (method_json["method"][0], auth_management_json["search_input"]["input"][0])
    search = (method_json["method"][0], auth_management_json["search_input"]["search"][0])
    ban = (method_json["method"][0], auth_management_json["auth_info"]["action"]["ban"][0])
    recover = (method_json["method"][0], auth_management_json["auth_info"]["action"]["recover"][0])
    QRcode = (method_json["method"][0], auth_management_json["auth_info"]["action"]["QRcode"][0])
    close_page = (method_json["method"][0], auth_management_json["auth_info"]["action"]["close_page"][0])
    activated_status = (method_json["method"][0], auth_management_json["auth_info"]["activated_status"][0])
    cancel_button = (method_json["method"][0], auth_management_json["cancel_button"][0])
    confirm_button = (method_json["method"][0], auth_management_json["confirm_button"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    generate_auth_code_reminder = (method_json["method"][0], reminder_json["generate_auth_code"][0])
    ban_reminder = (method_json["method"][0], reminder_json["ban"][0])
    recover_reminder = (method_json["method"][0], reminder_json["recover"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def input_random_number(self):
        random_number = self.get_random_number()
        self.input(random_number, *self.amount_input)
        return random_number

    def input_random_name(self):
        self.input(self.get_random_name(), *self.remark_input)

    def get_used_info(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_auth_management_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_auth_management_element)
        self.sleep(6)
        logger.info("license授权使用情况如下：")
        logger.info(f"{self.get_element(*self.permission_granted)}.")
        logger.info(f"{self.get_element(*self.auth_count_available)}.")
        logger.info(f"{self.get_element(*self.auth_amount_used)}.")
        logger.info(f"{self.get_element(*self.activated_amount)}.")
        logger.info(f"{self.get_element(*self.inactivated_amount)}.")
        logger.info(f"{self.get_element(*self.banned_amount)}.")

    # 出去前面字符，获得数字
    def get_used_number(self):
        permission_granted_number = int(self.get_element(*self.permission_granted)[8:])
        auth_count_available_number = int(self.get_element(*self.auth_count_available)[6:])
        auth_amount_used_number = int(self.get_element(*self.auth_amount_used)[6:])
        activated_amount_number = int(self.get_element(*self.activated_amount)[4:])
        inactivated_amount_number = int(self.get_element(*self.inactivated_amount)[5:])
        banned_amount_number = int(self.get_element(*self.banned_amount)[4:])
        return [permission_granted_number, auth_count_available_number, auth_amount_used_number,
                activated_amount_number, inactivated_amount_number, banned_amount_number]

    def generate_authorization_code(self):
        first_number = self.get_used_number()
        self.click(*self.generate_auth_code)
        random_number = self.input_random_number()
        self.input_random_name()
        self.click(*self.confirm_button)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.generate_auth_code_reminder))
            logger.info(f"{self.get_element(*self.generate_auth_code_reminder)}")
            self.get_windows_img()
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                self.click(*self.cancel_button)
                logger.error(f"{reminder}")
                logger.error("生成授权码有问题!")
                self.get_windows_img()
                return False
            except Exception:
                logger.error(f"{reminder}")
                logger.error(f"生成授权码有问题!")
                self.get_windows_img()
                return False
        self.sleep(4)
        second_number = self.get_used_number()
        result1 = first_number[0] + random_number == second_number[0]
        result2 = first_number[1] - random_number == second_number[1]
        result3 = first_number[2] + random_number == second_number[2]
        result4 = first_number[3] == second_number[3]
        result5 = first_number[4] + random_number == second_number[4]
        result6 = first_number[5] == second_number[5]
        if result1 and result2 and result3 and result4 and result5 and result6:
            return True
        else:
            logger.error("前端数字显示有异常!")
            return False

    def ban_auth_code(self):
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.ban))
            logger.info("新添加的第一个授权码可以被禁用.")
        except Exception:
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.recover))
                logger.error("新添加的第一个授权码已经被禁用.")
                return False
            except Exception as e:
                logger.error(e)
                logger.error("新添加的授权码存在异常")
                return False
        if self.get_element(*self.activated_status) == '未激活':
            pass
        else:
            logger.info(self.get_element(*self.activated_status))
            return False
        first_ban_number = self.get_used_number()
        self.click(*self.ban)
        self.click(*self.confirm_button)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.ban_reminder))
            logger.info(f"{self.get_element(*self.ban_reminder)}")
            self.get_windows_img()
        except Exception:
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                self.click(*self.cancel_button)
                logger.error(f"{reminder}")
                logger.error("禁用授权码有问题!")
                self.get_windows_img()
                return False
            except Exception as e:
                logger.error(e)
                logger.error("禁用授权码有问题!")
                return False
        self.forced_wait(*self.activated_status)
        self.sleep(3)
        if self.get_element(*self.activated_status) == '已禁用':
            pass
        else:
            logger.error("前端字体未变化")
            return False
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.recover))
            logger.info("禁用成功!")
        except Exception as e:
            logger.error("禁用失败!")
            logger.error(e)
            return False
        second_ban_number = self.get_used_number()
        result1 = first_ban_number[0] == second_ban_number[0]
        result2 = first_ban_number[1] + 1 == second_ban_number[1]
        result3 = first_ban_number[2] == second_ban_number[2]
        result4 = first_ban_number[3] == second_ban_number[3]
        result5 = first_ban_number[4] - 1 == second_ban_number[4]
        result6 = first_ban_number[5] + 1 == second_ban_number[5]
        if result1 and result2 and result3 and result4 and result5 and result6:
            return True
        else:
            logger.error("前端数字显示有异常!")
            return False

    def recover_auth_code(self):
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.recover))
            logger.info("第一个被禁用的授权码可以被恢复.")
        except Exception:
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.ban))
                logger.error("第一个被禁用的授权码不可以被恢复.")
                return False
            except Exception as e:
                logger.error(e)
                logger.error("新禁用的的授权码存在异常")
                return False
        if self.get_element(*self.activated_status) == '已禁用':
            pass
        else:
            logger.info(self.get_element(*self.activated_status))
            return False
        first_recover_number = self.get_used_number()
        self.click(*self.recover)
        self.click(*self.confirm_button)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.recover_reminder))
            logger.info(f"{self.get_element(*self.recover_reminder)}")
            self.get_windows_img()
        except Exception:
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                self.click(*self.cancel_button)
                logger.error(f"{reminder}")
                logger.error("恢复授权码有问题!")
                self.get_windows_img()
                return False
            except Exception as e:
                logger.error(e)
                logger.error("恢复授权码有问题!")
                return False
        self.forced_wait(*self.activated_status)
        self.sleep(3)
        if self.get_element(*self.activated_status) == '未激活':
            pass
        else:
            logger.error("前端字体未变化")
            return False
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.ban))
            logger.info("恢复成功!")
        except Exception as e:
            logger.error("恢复失败!")
            logger.error(e)
            return False
        second_recover_number = self.get_used_number()
        result1 = first_recover_number[0] == second_recover_number[0]
        result2 = first_recover_number[1] - 1 == second_recover_number[1]
        result3 = first_recover_number[2] == second_recover_number[2]
        result4 = first_recover_number[3] == second_recover_number[3]
        result5 = first_recover_number[4] + 1 == second_recover_number[4]
        result6 = first_recover_number[5] - 1 == second_recover_number[5]
        if result1 and result2 and result3 and result4 and result5 and result6:
            return True
        else:
            logger.error("前端数字显示有异常!")
            return False

    # 查看授权码
    def check_qrcode(self):
        self.forced_wait(*self.QRcode)
        self.click(*self.QRcode)
        self.forced_wait(*self.close_page)
        self.get_windows_img()
        self.click(*self.close_page)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.close_page))
            logger.info("查看授权码成功")
            return True
        except Exception as e:
            logger.error("关闭授权码界面失败")
            self.refresh_browser()
            self.sleep(8)
            logger.error(e)
            return False

    def search_first_auth_code(self):
        self.forced_wait(*self.remark)
        remark = self.get_element(*self.remark)
        self.input(remark, *self.search_input)
        self.click(*self.search)
        self.sleep(5)
        self.forced_wait(*self.remark)
        body_element = self.driver.find_element(*self.auth_body)
        auth_number = len(body_element.find_elements(method_json["method"][0], 'tr'))
        if auth_number == 1:
            return True
        else:
            return False
