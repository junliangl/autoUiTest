import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'quota_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    quota_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)


class Quota_Management_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_quota_management_element = (method_json["method"][0], menu_json["cd1_setting"]["quota_management"][0])
    staging_quota_management_element = (method_json["method"][0], menu_json["staging_setting"]["quota_management"][0])
    quota_amount = (method_json["method"][0], quota_management_json["quota_amount"][0])
    used_allocatable_amount = (method_json["method"][0], quota_management_json["used_allocatable_amount"][0])
    allocatable_amount = (method_json["method"][0], quota_management_json["allocatable_amount"][0])
    available_amount = (method_json["method"][0], quota_management_json["available_amount"][0])
    used_amount = (method_json["method"][0], quota_management_json["used_amount"][0])
    frozen_amount = (method_json["method"][0], quota_management_json["frozen_amount"][0])
    available_quota = (method_json["method"][0], quota_management_json["available_quota"][0])
    allocatable_quota = (method_json["method"][0], quota_management_json["allocatable_quota"][0])
    valid_only = (method_json["method"][0], quota_management_json["valid_only"][0])
    banned = (method_json["method"][0], quota_management_json["banned"][0])
    record = (method_json["method"][0], quota_management_json["record"]["button"][0])
    all_record = (method_json["method"][0], quota_management_json["record"]["all"][0])
    allocation_only = (method_json["method"][0], quota_management_json["record"]["allocation_only"][0])
    using_detail = (method_json["method"][0], quota_management_json["using_detail"]["button"][0])
    allocation_record = (method_json["method"][0], quota_management_json["using_detail"]["allocation_record"][0])
    close_page = (method_json["method"][0], quota_management_json["record"]["close_page"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def get_available_quota_info(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_quota_management_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_quota_management_element)
        self.sleep(6)
        self.click(*self.available_quota)
        self.forced_wait(*self.frozen_amount)
        logger.info(self.get_element(*self.quota_amount))
        logger.info(self.get_element(*self.available_amount))
        logger.info(self.get_element(*self.used_amount))
        logger.info(self.get_element(*self.frozen_amount))

    def get_allocatable_quota_info(self):
        self.click(*self.allocatable_quota)
        self.sleep(2)
        self.forced_wait(*self.frozen_amount)
        logger.info(self.get_element(*self.quota_amount))
        logger.info(self.get_element(*self.used_allocatable_amount))
        logger.info(self.get_element(*self.allocatable_amount))
        logger.info(self.get_element(*self.available_amount))
        logger.info(self.get_element(*self.used_amount))
        logger.info(self.get_element(*self.frozen_amount))

    def check_valid_only(self):
        self.click(*self.available_quota)
        self.click(*self.valid_only)
        self.sleep(2)
        self.click(*self.allocatable_quota)
        self.click(*self.valid_only)

    def check_record(self):
        self.execute_script_click(*self.record)
        self.click(*self.all_record)
        self.click(*self.allocation_only)
        self.click(*self.close_page)
        self.sleep(2)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.close_page))
            logger.error("关闭查看记录界面失败!")
            self.get_windows_img()
            self.refresh_browser()
            return False
        except Exception:
            logger.info("关闭查看记录界面成功.")
            return True

    def check_using_detail(self):
        self.execute_script_click(*self.using_detail)
        self.click(*self.allocation_record)
        self.click(*self.close_page)
        self.sleep(2)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.close_page))
            logger.error("关闭查看分配记录界面失败!")
            self.get_windows_img()
            self.refresh_browser()
            return False
        except Exception:
            logger.info("关闭查看记录界面成功.")
            return True
