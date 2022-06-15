import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'moqi_check_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    moqi_check_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)


class Moqi_Check_Management_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_moqi_check_element = (method_json["method"][0], menu_json["cd1_setting"]["moqi_check_management"][0])
    staging_moqi_check_element = (method_json["method"][0], menu_json["staging_setting"]["moqi_check_management"][0])
    check_activated_number = (method_json["method"][0], moqi_check_management_json["check_activated"]["number"][0])
    true = (method_json["method"][0], moqi_check_management_json["check_activated"]["true"][0])
    true_click = (method_json["method"][0], moqi_check_management_json["check_activated"]["true_click"][0])
    false = (method_json["method"][0], moqi_check_management_json["check_activated"]["false"][0])
    false_click = (method_json["method"][0], moqi_check_management_json["check_activated"]["false_click"][0])
    disabled = (method_json["method"][0], moqi_check_management_json["amount"]["disabled"][0])
    amount_buttons = (method_json["method"][0], moqi_check_management_json["amount"]["buttons"][0])
    amount_number = (method_json["method"][0], moqi_check_management_json["amount"]["number"][0])
    attribute_value = moqi_check_management_json["amount"]["attribute_value"][0]
    cancel_button = (method_json["method"][0], moqi_check_management_json["cancel"][0])
    save_button = (method_json["method"][0], moqi_check_management_json["save"][0])
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

    def check_button(self):
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_moqi_check_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_moqi_check_element)
        self.forced_wait(*self.save_button)
        element1 = self.driver.find_element(*self.check_activated_number)
        element2 = self.driver.find_element(*self.amount_number)
        check_activated_number = len(element1.find_elements(method_json["method"][0], 'label'))
        amount_number = len(element2.find_elements(method_json["method"][0], 'label'))
        if check_activated_number == 2 and amount_number == 4:
            logger.info("该页面button没有问题.")
            return True
        elif check_activated_number == 2 and amount_number != 4:
            logger.error("app墨奇检视量button有问题!")
            self.get_windows_img()
        elif check_activated_number != 2 and amount_number == 4:
            logger.error("墨奇检视开关button有问题!")
            self.get_windows_img()
        else:
            logger.error("墨奇检视开关和app墨奇检视量button都有问题!")
            self.get_windows_img()
        return False

    def cancel_change(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_moqi_check_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_moqi_check_element)
        self.forced_wait(*self.cancel_button)
        self.click(*self.cancel_button)
        # noinspection PyBroadException
        try:
            if self.get_url() == 'http://10.1.1.80:7001/':
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cd1_moqi_check_element))
            elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.staging_moqi_check_element))
            logger.info("取消修改成功.")
            return True
        except Exception:
            logger.error("取消修改失败!")
            self.get_windows_img()

    def save_change(self):
        self.forced_wait(*self.save_button)
        self.click(*self.save_button)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.change_reminder))
            logger.info(self.get_element(*self.change_reminder))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("修改信息失败!")
            logger.error(reminder)
            logger.error(e)
            self.get_windows_img()
            return False

    def switch_moqi_check_management(self):
        result = self.check_button()
        if result:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.true_click))
                # noinspection PyBroadException
                try:
                    # 并且app默认检视量设置 button 处于开启状态
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled))
                    logger.error("当前墨奇检视开关为打开状态,但不可以设置app墨奇检视量!")
                    self.get_windows_img()
                    return False
                except Exception:
                    logger.info("当前墨奇检视开关为打开状态,且可以设置app墨奇检视量.")
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.false))
                    logger.info("开关状态没有问题.")
                except Exception as e:
                    logger.error("同时选中了打开和关闭!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                self.traverse_click(*self.amount_buttons, attribute='class', value=self.attribute_value)
                self.click(*self.false)
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled))
                    logger.info("当前墨奇检视开关为关闭状态,且不可以设置app墨奇检视量.")
                except Exception as e:
                    logger.error("当前墨奇检视开关为关闭状态,但可以设置app墨奇检视量!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.false_click))
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.true))
                        logger.info("开关切换成关闭状态成功.")
                    except Exception as e:
                        logger.error("开关切换成关闭状态失败!")
                        logger.error(e)
                        self.get_windows_img()
                        return False
                except Exception as e:
                    logger.error("开关切换成关闭状态失败!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                self.click(*self.true)
                # noinspection PyBroadException
                try:
                    # 并且app默认检视量设置 button 处于开启状态
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled))
                    logger.error("当前墨奇检视开关为打开状态,但不可以设置app墨奇检视量!")
                    self.get_windows_img()
                    return False
                except Exception:
                    logger.info("当前墨奇检视开关为打开状态,且可以设置app墨奇检视量.")
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.true_click))
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.false))
                        logger.info("开关重新切换成打开状态成功.")
                    except Exception as e:
                        logger.error("开关重新切换成打开状态失败!")
                        logger.error(e)
                        self.get_windows_img()
                        return False
                except Exception as e:
                    logger.error("开关重新切换成打开状态失败!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                self.traverse_click(*self.amount_buttons, attribute='class', value=self.attribute_value)
            except Exception:
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled))
                    logger.info("当前墨奇检视开关为关闭状态,且不可以设置app墨奇检视量.")
                except Exception as e:
                    logger.error("当前墨奇检视开关为关闭状态,但可以设置app墨奇检视量!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.true))
                    logger.info("开关状态没有问题.")
                except Exception as e:
                    logger.error("同时选中了打开和关闭!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                self.click(*self.true)
                # noinspection PyBroadException
                try:
                    # 并且app默认检视量设置 button 处于开启状态
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled))
                    logger.error("当前墨奇检视开关为打开状态,但不可以设置app墨奇检视量!")
                    self.get_windows_img()
                    return False
                except Exception:
                    logger.info("当前墨奇检视开关为打开状态,且可以设置app墨奇检视量.")
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.true_click))
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.false))
                        logger.info("开关切换成打开状态成功.")
                    except Exception as e:
                        logger.error("开关切换成打开状态失败!")
                        logger.error(e)
                        self.get_windows_img()
                        return False
                except Exception as e:
                    logger.error("开关切换成打开状态失败!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                self.traverse_click(*self.amount_buttons, attribute='class', value=self.attribute_value)
                self.click(*self.false)
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled))
                    logger.info("当前墨奇检视开关为关闭状态,且不可以设置app墨奇检视量.")
                except Exception as e:
                    logger.error("当前墨奇检视开关为关闭状态,但可以设置app墨奇检视量!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.false_click))
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.true))
                        logger.info("开关重新切换成关闭状态成功.")
                    except Exception as e:
                        logger.error("开关重新切换成关闭状态失败!")
                        logger.error(e)
                        self.get_windows_img()
                        return False
                except Exception as e:
                    logger.error("开关重新切换成关闭状态失败!")
                    logger.error(e)
                    self.get_windows_img()
                    return False
            return True
        else:
            return False