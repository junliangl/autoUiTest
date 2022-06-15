import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'matching_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    matching_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)


class Matching_Management_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_matching_element = (method_json["method"][0], menu_json["cd1_setting"]["matching_management"][0])
    staging_matching_element = (method_json["method"][0], menu_json["staging_setting"]["matching_management"][0])
    person_original_checkbox1 = (method_json["method"][0], matching_management_json["person_database"]["original_checkbox1"][0])
    person_first_click_checkbox = (method_json["method"][0], matching_management_json["person_database"]["first_click_checkbox"][0])
    person_first_checkbox = (method_json["method"][0], matching_management_json["person_database"]["first_checkbox"][0])
    case_original_checkbox1 = (method_json["method"][0], matching_management_json["case_database"]["original_checkbox1"][0])
    case_first_click_checkbox = (method_json["method"][0], matching_management_json["case_database"]["first_click_checkbox"][0])
    case_first_checkbox = (method_json["method"][0], matching_management_json["case_database"]["first_checkbox"][0])
    case_original_checkbox2 = (method_json["method"][0], matching_management_json["case_database"]["original_checkbox2"][0])
    case_second_checkbox = (method_json["method"][0], matching_management_json["case_database"]["second_checkbox"][0])
    case_second_click_checkbox = (method_json["method"][0], matching_management_json["case_database"]["second_click_checkbox"][0])
    save_button = (method_json["method"][0], matching_management_json["save"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    change_reminder = (method_json["method"][0], reminder_json["change"][0])

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

    def change_matching_management(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_matching_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_matching_element)
        self.forced_wait(*self.save_button)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.person_original_checkbox1))
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.person_first_click_checkbox))
                logger.info("该人员库处于勾选状态.")
                self.click(*self.person_first_click_checkbox)
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.person_first_checkbox))
                    logger.info("该人员库取消勾选成功.")
                except Exception as e:
                    logger.error("该人员库取消勾选失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                self.click(*self.person_first_checkbox)
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.person_first_click_checkbox))
                    logger.info("该人员库再次勾选成功.")
                except Exception as e:
                    logger.error("该人员库再次勾选失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
            except Exception:
                logger.info("该人员库处于取消勾选状态.")
                self.click(*self.person_first_checkbox)
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.person_first_click_checkbox))
                    logger.info("该人员库勾选成功.")
                except Exception as e:
                    logger.error("该人员库勾选失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                self.click(*self.person_first_click_checkbox)
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.person_first_checkbox))
                    logger.info("该人员库取消勾选成功.")
                except Exception as e:
                    logger.error("该人员库取消勾选失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
        except Exception as e:
            logger.error("未找到第一个app比对人员库.")
            logger.error(e)
            self.get_windows_img()
            return False
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_original_checkbox1))
        except Exception as e:
            logger.error("未找到第一个app比对案件库.")
            logger.error(e)
            self.get_windows_img()
            return False
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_original_checkbox2))
        except Exception:
            logger.info("未找到第二个app比对案件库.")
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_first_click_checkbox))
                logger.info("该比对案件库设置没有问题.")
            except Exception as e:
                logger.error("该比对案件库设置有问题.")
                logger.error(e)
                self.get_windows_img()
                return False
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_first_click_checkbox))
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_second_checkbox))
                logger.info("app比对案件库没有问题.")
            except Exception as e:
                logger.error("app比对案件库存在问题.")
                logger.error(e)
                self.get_windows_img()
                return False
            self.click(*self.case_second_checkbox)
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_second_click_checkbox))
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_first_checkbox))
                    logger.info("切换比对案件库成功.")
                except Exception as e:
                    logger.error("切换比对案件库失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
            except Exception as e:
                logger.error("切换比对案件库失败.")
                logger.error(e)
                self.get_windows_img()
                return False
            self.click(*self.case_first_checkbox)
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_first_click_checkbox))
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_second_checkbox))
                    logger.info("再次切换比对案件库成功.")
                except Exception as e:
                    logger.error("再次切换比对案件库失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
            except Exception as e:
                logger.error("再次切换比对案件库失败.")
                logger.error(e)
                self.get_windows_img()
                return False
        except Exception:
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_second_click_checkbox))
                logger.info("app比对案件库没有问题.")
            except Exception as e:
                logger.error("app比对案件库存在问题.")
                logger.error(e)
                self.get_windows_img()
                return False
            self.click(*self.case_first_checkbox)
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_first_click_checkbox))
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_second_checkbox))
                    logger.info("切换比对案件库成功.")
                except Exception as e:
                    logger.error("切换比对案件库失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
            except Exception as e:
                logger.error("切换比对案件库失败.")
                logger.error(e)
                self.get_windows_img()
                return False
            self.click(*self.case_second_checkbox)
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_second_click_checkbox))
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.case_first_checkbox))
                    logger.info("再次切换比对案件库成功.")
                except Exception as e:
                    logger.error("再次切换比对案件库失败.")
                    logger.error(e)
                    self.get_windows_img()
                    return False
            except Exception as e:
                logger.error("再次切换比对案件库失败.")
                logger.error(e)
                self.get_windows_img()
                return False
        self.click(*self.save_button)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.change_reminder))
            logger.info(f"{self.get_element(*self.change_reminder)}")
            return True
        except Exception:
            logger.error("修改app比对库存在问题.")
            logger.error(reminder)
            self.get_windows_img()
            return False
