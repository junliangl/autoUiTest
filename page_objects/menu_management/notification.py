import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.base_page import BasePage
from page_objects.common_login.login import Login

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'notification.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
login_file = os.path.join(os.path.join(project_path, 'config'), 'login.json')

with open(json_file, encoding='utf-8') as file1:
    notification_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(login_file, encoding='utf-8') as file4:
    login_json = json.load(file4)

result = None


class Notification_Page(BasePage):
    login_button = (method_json["method"][0], login_json["login_button"][0])
    username = (method_json["method"][0], menu_json["user"]["button"][0])
    logout_button = (method_json["method"][0], menu_json["user"]["log_out"][0])
    notification_button = (method_json["method"][0], menu_json["notification"][0])
    pop_ups_reminder = (method_json["method"][0], notification_json["pop_ups_reminder"][0])
    sound_reminder = (method_json["method"][0], notification_json["sound_reminder"][0])
    confirm = (method_json["method"][0], notification_json["confirm_button"][0])
    click_attribute_value = notification_json["attribute_value"]["click"][0]
    disabled_attribute_value = notification_json["attribute_value"]["disabled"][0]

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def check_default_reminder_button(self):
        global result
        self.click(*self.notification_button)
        # 判断弹窗提醒按钮是否为打开状态
        result1 = self.click_attribute_value in self.find_element_attribute('class', *self.pop_ups_reminder)
        # 判断弹窗提醒按钮是否可以点击
        result2 = self.disabled_attribute_value in self.find_element_attribute('class', *self.pop_ups_reminder)
        # 判断声音提醒按钮是否为打开状态
        result3 = self.click_attribute_value in self.find_element_attribute('class', *self.sound_reminder)
        # 判断声音提醒按钮是否可以点击
        result4 = self.disabled_attribute_value in self.find_element_attribute('class', *self.sound_reminder)
        if result1:
            pop_ups_state = '打开'
        else:
            pop_ups_state = '关闭'
        if result2:
            pop_ups_button = '无法'
        else:
            pop_ups_button = '可以'
        if result3:
            sound_state = '打开'
        else:
            sound_state = '关闭'
        if result4:
            sound_button = '无法'
        else:
            sound_button = '可以'
        if not result1 and not result2 and result3 and result4:
            logger.info(f"弹窗提醒为{pop_ups_state}状态(默认关闭),{pop_ups_button}点击(默认可以点击);"
                        f"声音提醒为{sound_state}状态(默认打开),{sound_button}点击(默认无法点击)!")
            result = True
            return result
        else:
            logger.error(f"弹窗提醒为{pop_ups_state}状态(默认关闭),{pop_ups_button}点击(默认可以点击);"
                         f"声音提醒为{sound_state}状态(默认打开),{sound_button}点击(默认无法点击)!")
            self.get_windows_img()
            result = False
            return result

    def change_setting(self):
        if result:
            self.click(*self.pop_ups_reminder)
            if self.click_attribute_value in self.find_element_attribute('class', *self.pop_ups_reminder):
                if self.disabled_attribute_value not in self.find_element_attribute('class', *self.sound_reminder):
                    logger.info("点击弹窗提醒按钮成功,声音提醒按钮可以点击.")
                else:
                    logger.error("点击弹窗提醒按钮成功,声音提醒按钮无法点击.")
                    self.get_windows_img()
                    return False
            else:
                if self.disabled_attribute_value not in self.find_element_attribute('class', *self.sound_reminder):
                    logger.error("点击弹窗提醒按钮失败,声音提醒按钮可以点击.")
                    self.get_windows_img()
                    return False
                else:
                    logger.error("点击弹窗提醒按钮失败,声音提醒按钮不可以点击.")
                    self.get_windows_img()
                    return False
            self.click(*self.sound_reminder)
            if self.click_attribute_value in self.find_element_attribute('class', *self.sound_reminder):
                logger.error("点击声音提醒按钮失败!")
                self.get_windows_img()
                return False
            else:
                logger.info("点击声音提醒按钮成功.")
            self.click(*self.pop_ups_reminder)
            if self.click_attribute_value not in self.find_element_attribute('class', *self.pop_ups_reminder):
                if self.disabled_attribute_value in self.find_element_attribute('class', *self.sound_reminder):
                    logger.info("点击弹窗提醒按钮成功,声音提醒按钮不可以点击.")
                else:
                    logger.error("点击弹窗提醒按钮成功,声音提醒按钮可以点击!")
                    self.get_windows_img()
                    return False
            else:
                if self.disabled_attribute_value in self.find_element_attribute('class', *self.sound_reminder):
                    logger.error("点击弹窗提醒按钮失败,声音提醒按钮不可以点击.")
                    self.get_windows_img()
                    return False
                else:
                    logger.error("点击弹窗提醒按钮失败,声音提醒按钮可以点击!")
                    self.get_windows_img()
                    return False
            self.refresh_browser()
            self.click(*self.notification_button)
            if self.click_attribute_value not in self.find_element_attribute('class', *self.pop_ups_reminder):
                if self.disabled_attribute_value in self.find_element_attribute('class', *self.sound_reminder):
                    logger.info('刷新后不影响设置.')
                else:
                    logger.error("刷新后影响设置!")
                    self.get_windows_img()
                    return False
            else:
                logger.error("刷新后影响设置!")
                self.get_windows_img()
                return False
            # 注销
            self.click(*self.username)
            self.click(*self.logout_button)
            self.click(*self.confirm)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.login_button))
                logger.info("注销成功.")
            except Exception:
                logger.error("注销失败!")
                self.get_windows_img()
                return False
            # 再次登录
            self.login()
            self.click(*self.notification_button)
            if self.click_attribute_value not in self.find_element_attribute('class', *self.pop_ups_reminder):
                if self.disabled_attribute_value in self.find_element_attribute('class', *self.sound_reminder):
                    logger.info('注销再次登录后不影响设置.')
                else:
                    logger.error("注销再次登录后影响设置!")
                    self.get_windows_img()
                    return False
            else:
                logger.error("注销再次登录影响设置!")
                self.get_windows_img()
                return False
            # 再次注销
            self.click(*self.username)
            self.click(*self.logout_button)
            self.click(*self.confirm)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.login_button))
                logger.info("注销成功.")
            except Exception:
                logger.error("注销失败!")
                self.get_windows_img()
                return False
            # 测试强制刷新清除本地缓存的设置
            self.force_refresh()
            self.login()
            # 调用上面定义的方法测试下消息提醒button是否是默认值
            last_result = self.check_default_reminder_button()
            if last_result:
                logger.info("强制刷新不影响设置.")
                return True
            else:
                logger.error("强制刷新影响设置!")
                self.get_windows_img()
                return False
        else:
            logger.warning("上一个测试未通过,不进行本次测试(默认失败)!")
            return False
