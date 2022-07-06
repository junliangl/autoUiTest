import os
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.base_page import BasePage
from page_objects.common_login.login import Login


logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'superadmin.json')
login_file = os.path.join(os.path.join(project_path, 'config'), 'login.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    superadmin_json = json.load(file1)

with open(login_file, encoding='utf-8') as file2:
    login_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)

group_name = None


class Superadmin_Page(BasePage):
    system_management = (method_json["method"][0], superadmin_json["system_management"][0])
    group_management = (method_json["method"][0], superadmin_json["group_management"][0])
    search_input = (method_json["method"][0], superadmin_json["search_input"][0])
    search = (method_json["method"][0], superadmin_json["search"][0])
    group_name_text = (method_json["method"][0], superadmin_json["group_name_text"][0])
    group = (method_json["method"][0], superadmin_json["group"]["button"][0])
    group_detail = (method_json["method"][0], superadmin_json["group"]["detail"][0])
    role = (method_json["method"][0], superadmin_json["group"]["role"][0])
    invite_user = (method_json["method"][0], superadmin_json["group"]["invite_user"][0])
    input_account = (method_json["method"][0], superadmin_json["group"]["input_account"][0])
    first_user = (method_json["method"][0], superadmin_json["group"]["first_user"][0])
    confirm_button = (method_json["method"][0], superadmin_json["group"]["confirm_button"][0])
    create_group = (method_json["method"][0], superadmin_json["create_new_group"][0])
    group_name = (method_json["method"][0], superadmin_json["group_name"][0])
    group_id = (method_json["method"][0], superadmin_json["group_id"][0])
    group_area_button = (method_json["method"][0], superadmin_json["group_area"]["button"][0])
    ministry = (method_json["method"][0], superadmin_json["group_area"]["ministry"][0])
    province = (method_json["method"][0], superadmin_json["group_area"]["province"][0])
    city = (method_json["method"][0], superadmin_json["group_area"]["city"][0])
    district = (method_json["method"][0], superadmin_json["group_area"]["district"][0])
    group_account_number = (method_json["method"][0], superadmin_json["group_account_number"][0])
    group_app_number = (method_json["method"][0], superadmin_json["group_app_number"][0])
    group_expiration_time = (method_json["method"][0], superadmin_json["group_expiration_time"][0])
    available_quota = (method_json["method"][0], superadmin_json["available_quota"][0])
    quota_expiration_time = (method_json["method"][0], superadmin_json["quota_expiration_time"][0])
    finger_palm = (method_json["method"][0], superadmin_json["finger_palm"][0])
    mobile_police = (method_json["method"][0], superadmin_json["mobile_police"][0])
    moqi_match = (method_json["method"][0], superadmin_json["moqi_match"][0])
    invite_match = (method_json["method"][0], superadmin_json["invite_match"][0])
    save_group = (method_json["method"][0], superadmin_json["save_group"][0])
    db_management = (method_json["method"][0], superadmin_json["db_management"][0])
    create_db = (method_json["method"][0], superadmin_json["create_db"][0])
    db_name = (method_json["method"][0], superadmin_json["db_name"][0])
    db_id = (method_json["method"][0], superadmin_json["db_id"][0])
    private_db = (method_json["method"][0], superadmin_json["private_db"][0])
    input_group = (method_json["method"][0], superadmin_json["input_group"][0])
    choose_group = (method_json["method"][0], superadmin_json["choose_group"][0])
    case_db = (method_json["method"][0], superadmin_json["case_db"][0])
    max_finger_palm = (method_json["method"][0], superadmin_json["max_finger"][0])
    max_finger = (method_json["method"][0], superadmin_json["max_finger"][0])
    max_palm = (method_json["method"][0], superadmin_json["max_palm"][0])
    save_db = (method_json["method"][0], superadmin_json["save_db"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    create_group_reminder = (method_json["method"][0], reminder_json["create_group"][0])
    create_db_reminder = (method_json["method"][0], reminder_json["create_db"][0])
    invite_to_group_reminder = (method_json["method"][0], reminder_json["invite_to_group"][0])

    def login(self):
        # 以下为调试使用
        # login = Login(self.driver)
        # login.login('superadmin')
        if self.get_account():
            login = Login(self.driver)
            # 参数为'superadmin'就登录superadmin账号，其他则登录注册成功的账号
            login.login('superadmin')
        else:
            raise Exception('登录账号为空!')

    def create_new_group(self):
        global group_name
        self.click(*self.system_management)
        self.click(*self.group_management)
        self.click(*self.create_group)
        group_name = self.get_random_name()
        group_id = self.get_random_number()
        self.input(group_name, *self.group_name)
        self.input(group_id, *self.group_id)
        self.click(*self.group_area_button)
        self.actionchains_click(*self.ministry)
        self.actionchains_click(*self.province)
        self.actionchains_click(*self.city)
        self.actionchains_click(*self.district)
        self.input('50', *self.group_account_number)
        self.input('50', *self.group_app_number)
        self.input('2025-01-01', *self.group_expiration_time)
        self.input('100000', *self.available_quota)
        self.input('2025-01-01', *self.quota_expiration_time)
        self.actionchains_click(*self.finger_palm)
        self.execute_script_click(*self.mobile_police)
        self.execute_script_click(*self.moqi_match)
        self.execute_script_click(*self.invite_match)
        self.click(*self.save_group)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.create_group_reminder))
            logger.info(self.get_element(*self.create_group_reminder))
            self.get_windows_img()
            return True
        except Exception:
            logger.error("新建域失败.")
            logger.error(reminder)
            self.get_windows_img()
            return False

    def create_private_db(self):
        # 创建私有人员库
        self.click(*self.system_management)
        self.click(*self.db_management)
        self.click(*self.create_db)
        date_time = time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))
        self.input(f'test_{date_time}', *self.db_name)
        self.input(self.get_random_number()+self.get_random_number(), *self.db_id)
        self.click(*self.private_db)
        self.input(group_name, *self.input_group)
        self.sleep(1)
        self.click(*self.choose_group)
        self.input('1000', *self.max_finger_palm)
        self.click(*self.save_db)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.create_db_reminder))
            logger.info(self.get_element(*self.create_db_reminder))
        except Exception:
            logger.error("新建私有人员库失败.")
            logger.error(reminder)
            self.get_windows_img()
            return False

        # 创建私有案件库
        self.click(*self.system_management)
        self.click(*self.db_management)
        self.click(*self.create_db)
        date_time = time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))
        self.input(f'test_{date_time}', *self.db_name)
        self.input(self.get_random_number(), *self.db_id)
        self.click(*self.private_db)
        self.input(group_name, *self.input_group)
        self.sleep(1)
        self.click(*self.choose_group)
        self.click(*self.case_db)
        self.input('1000', *self.max_finger)
        self.input('1000', *self.max_palm)
        self.click(*self.save_db)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.create_db_reminder))
            logger.info(self.get_element(*self.create_db_reminder))
            return True
        except Exception:
            logger.error("新建私有案件失败.")
            logger.error(reminder)
            self.get_windows_img()
            return False

    def invite_to_group(self):
        self.refresh_browser()
        self.click(*self.system_management)
        self.click(*self.group_management)
        self.input(group_name, *self.search_input)
        self.sleep(1)
        self.click(*self.search)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.group_name_text, group_name))
            logger.info("搜索出先刚创建的域.")
        except Exception as e:
            logger.error("搜索未出现刚创建的域!")
            logger.error(e)
            self.get_windows_img()
            return False
        self.execute_script_click(*self.group)
        self.execute_script_click(*self.group_detail)
        self.click(*self.role)
        self.click(*self.invite_user)
        self.input(self.get_account(), *self.input_account)
        self.sleep(1)
        self.click(*self.first_user)
        self.click(*self.input_account)
        self.click(*self.confirm_button)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.invite_to_group_reminder))
            logger.info(self.get_element(*self.invite_to_group_reminder))
            return True
        except Exception:
            logger.error(f"邀请人员 {self.get_account()} 失败.")
            logger.error(reminder)
            self.get_windows_img()
            return False
