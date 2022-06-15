import os
import json
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'inspect_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    inspect_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)

check_create_inspect_result = False
button_result = []
inspect_name = ''
group_name = ''


class Inspect_Management_Page(BasePage):
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_inspect_management = (method_json["method"][0], menu_json["cd1_setting"]["inspect_management"][0])
    staging_inspect_management = (method_json["method"][0], menu_json["staging_setting"]["inspect_management"][0])
    inspect_none_data = (method_json["method"][0], inspect_management_json["none_data"][0])
    create_inspect = (method_json["method"][0], inspect_management_json["create_inspect"][0])
    input_name = (method_json["method"][0], inspect_management_json["input_name"][0])
    private = (method_json["method"][0], inspect_management_json["permission"]["private"][0])
    public = (method_json["method"][0], inspect_management_json["permission"]["public"][0])
    choose_group = (method_json["method"][0], inspect_management_json["permission"]["choose_group"][0])
    first_group = (method_json["method"][0], inspect_management_json["permission"]["first_group"][0])
    first_group_name = (method_json["method"][0], inspect_management_json["permission"]["group_name"][0])
    inspect_name = (method_json["method"][0], inspect_management_json["inspect_name"][0])
    group_type = (method_json["method"][0], inspect_management_json["group_type"][0])
    creator = (method_json["method"][0], inspect_management_json["creator"][0])
    inspector_number = (method_json["method"][0], inspect_management_json["inspector_number"][0])
    action = (method_json["method"][0], inspect_management_json["action"][0])
    edit = (method_json["method"][0], inspect_management_json["edit"]["button"][0])
    create_inspector_button = (method_json["method"][0], inspect_management_json["edit"]["create_inspector"][0])
    inspector_none_data = (method_json["method"][0], inspect_management_json["edit"]["none_data"][0])
    inspector_name = (method_json["method"][0], inspect_management_json["edit"]["name"][0])
    inspector_account = (method_json["method"][0], inspect_management_json["edit"]["account"][0])
    inspector_area = (method_json["method"][0], inspect_management_json["edit"]["area"][0])
    inspector_group = (method_json["method"][0], inspect_management_json["edit"]["group"][0])
    inspector_action = (method_json["method"][0], inspect_management_json["edit"]["action"][0])
    inspector_delete = (method_json["method"][0], inspect_management_json["edit"]["delete_inspector"][0])
    input_inspector = (method_json["method"][0], inspect_management_json["edit"]["input_inspector"][0])
    delete_input = (method_json["method"][0], inspect_management_json["edit"]["delete_input"][0])
    delete_create = (method_json["method"][0], inspect_management_json["edit"]["delete_create"][0])
    delete = (method_json["method"][0], inspect_management_json["delete"][0])
    confirm = (method_json["method"][0], inspect_management_json["confirm"][0])
    cancel = (method_json["method"][0], inspect_management_json["cancel"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    create_inspect_reminder = (method_json["method"][0], reminder_json["create_inspect"][0])
    create_inspector_reminder = (method_json["method"][0], reminder_json["create_inspector"][0])
    delete_inspect_reminder = (method_json["method"][0], reminder_json["delete_inspect"][0])
    delete_inspector_reminder = (method_json["method"][0], reminder_json["delete_inspector"][0])
    attribute_value = inspect_management_json["permission"]["attribute_value"][0]

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

    def check_inspect_info(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_inspect_management)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_inspect_management)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.inspect_none_data))
            logger.info("该域没有设置检视组.")
            return True
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                logger.info("该域有设置检视组.")
                return True
            except Exception:
                logger.error("前端界面展示有问题")
                self.get_windows_img()
                return False

    def delete_inspect(self):
        times = 0
        while True:
            # noinspection PyBroadException
            try:
                before = time.time()
                self.sleep(1)
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                logger.warning(f"即将删除 inspect_name:{self.get_element(*self.inspect_name)} "
                               f"group_type:{self.get_element(*self.group_type)} "
                               f"creator:{self.get_element(*self.creator)} "
                               f"inspect_number:{self.get_element(*self.inspector_number)} "
                               f"action：{self.get_element(*self.action)} 检视组")
                self.execute_script_click(*self.delete)
                times = times + 1
                self.click(*self.confirm)
                self.forced_wait(*self.reminder)
                reminder = self.get_element(*self.reminder)
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_inspect_reminder))
                    logger.info(self.get_element(*self.delete_inspect_reminder))
                    self.get_windows_img()
                except Exception:
                    # noinspection PyBroadException
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel))
                        self.click(*self.cancel)
                        logger.error(f"{reminder}")
                        logger.error("删除检视组有问题!")
                        self.get_windows_img()
                        return False
                    except Exception:
                        logger.error(f"{reminder}")
                        logger.error(f"删除检视组有问题!")
                        self.get_windows_img()
                        return False
                after = time.time()
                if after - before > 12 or times > 5:
                    break
            except Exception:
                break
        if times == 0:
            logger.info("该域没有检视组!")
        return True

    def check_create_inspect(self):
        global check_create_inspect_result
        global button_result
        global inspect_name
        global group_name
        self.click(*self.create_inspect)
        inspect_name = self.get_random_name()
        self.input(inspect_name, *self.input_name)
        if self.attribute_value in self.find_element_attribute('class', *self.private):
            if self.attribute_value in self.find_element_attribute('class', *self.public):
                logger.error("检视组权限两个按钮都被选中!")
                self.get_windows_img()
                button_result = [1, 1]
                return check_create_inspect_result
            else:
                logger.info("检视组权限两个按钮没有问题.")
        else:
            if self.attribute_value in self.find_element_attribute('class', *self.public):
                logger.error(f"检视组权限默认选中的 {self.get_element(*self.private)} 按钮未被选中!")
                self.get_windows_img()
                button_result = [0, 1]
                return check_create_inspect_result
            else:
                logger.error(f"检视组权限两个按钮都未被选中!")
                self.get_windows_img()
                button_result = [0, 0]
                return check_create_inspect_result
        self.click(*self.public)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.choose_group))
            logger.info("切换按钮后显示选择域下拉列表.")
        except Exception as e:
            logger.error("切换按钮后未显示选择域下拉列表!")
            logger.error(e)
            self.get_windows_img()
            button_result = [1, 0]
            return check_create_inspect_result
        self.click(*self.choose_group)
        group_name = self.get_element(*self.first_group)
        self.click(*self.first_group)
        if self.attribute_value in self.find_element_attribute('class', *self.private):
            if self.attribute_value in self.find_element_attribute('class', *self.public):
                logger.error("检视组权限两个按钮都被选中!")
                self.get_windows_img()
                button_result = [1, 1]
                return check_create_inspect_result
            else:
                logger.error(f"检视组权限 {self.get_element(*self.public)} 未被选中"
                             f",且 {self.get_element(*self.private)} 未取消选中.")
                self.get_windows_img()
                button_result = [1, 0]
                return check_create_inspect_result
        else:
            if self.attribute_value in self.find_element_attribute('class', *self.public):
                logger.info(f"选择 {self.get_element(*self.public)} 按钮没有问题.")
                check_create_inspect_result = True
                button_result = [0, 1]
                return check_create_inspect_result
            else:
                logger.error(f"检视组权限两个按钮都未被选中!")
                self.get_windows_img()
                button_result = [0, 0]
                return check_create_inspect_result

    def cancel_create_inspect(self):
        if check_create_inspect_result:
            self.click(*self.cancel)
            self.sleep(1)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located(self.cancel))
                logger.error('点击取消失败!')
                self.get_windows_img()
                self.refresh_browser()
                return False
            except Exception:
                logger.info("点击取消成功!")
            self.click(*self.create_inspect)
            self.forced_wait(*self.input_name)
            new_inspect_name = self.find_element_attribute('value', *self.input_name)
            new_button_result = []
            if self.attribute_value in self.find_element_attribute('class', *self.private):
                new_button_result.append(1)
            else:
                new_button_result.append(0)
            if self.attribute_value in self.find_element_attribute('class', *self.public):
                new_button_result.append(1)
            else:
                new_button_result.append(0)
            self.forced_wait(*self.first_group_name)
            new_group_name = self.get_element(*self.first_group_name)
            if new_inspect_name == inspect_name and new_button_result == button_result and new_group_name == group_name:
                logger.info("取消后未影响原来的设置.")
                return True
            else:
                logger.error("取消后影响了原来的设置")
                self.get_windows_img()
                return False
        else:
            logger.error("检测出检视组按钮有问题.本功能默认失败!")
            return False

    def create_private_inspect(self):
        self.refresh_browser()
        self.click(*self.create_inspect)
        self.input(self.get_random_name(), *self.input_name)
        self.click(*self.confirm)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.create_inspect))
            logger.info(self.get_element(*self.reminder))
            self.get_windows_img()
            return True
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel))
                self.click(*self.cancel)
                logger.error(f"{reminder}")
                logger.error("创建检视组有问题!")
                self.get_windows_img()
                return False
            except Exception:
                logger.error(f"{reminder}")
                logger.error(f"创建检视组有问题!")
                self.get_windows_img()
                return False

    def create_public_inspect(self):
        self.refresh_browser()
        self.click(*self.create_inspect)
        self.input(self.get_random_name(), *self.input_name)
        self.click(*self.public)
        self.click(*self.choose_group)
        self.click(*self.first_group)
        self.click(*self.confirm)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.create_inspect))
            logger.info(self.get_element(*self.reminder))
            self.get_windows_img()
            return True
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel))
                self.click(*self.cancel)
                logger.error(f"{reminder}")
                logger.error("创建检视组有问题!")
                self.get_windows_img()
                return False
            except Exception:
                logger.error(f"{reminder}")
                logger.error(f"创建检视组有问题!")
                self.get_windows_img()
                return False

    def check_inspector_info(self):
        self.refresh_browser()
        self.execute_script_click(*self.edit)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.inspector_none_data))
            logger.info("该检视组没有设置检视专家.")
            return True
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.inspector_delete))
                logger.info("该域有设置检视组.")
                return True
            except Exception:
                logger.error("前端界面展示有问题")
                self.get_windows_img()
                return False

    def delete_inspector(self):
        times = 0
        while True:
            # noinspection PyBroadException
            try:
                before = time.time()
                self.sleep(1)
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.inspector_delete))
                logger.warning(f"即将删除 inspector_name:{self.get_element(*self.inspector_name)} "
                               f"inspector_account:{self.get_element(*self.inspector_account)} "
                               f"inspector_area:{self.get_element(*self.inspector_area)} "
                               f"inspector_group:{self.get_element(*self.inspector_group)} "
                               f"action：{self.get_element(*self.inspector_action)} 检视专家")
                self.execute_script_click(*self.inspector_delete)
                times = times + 1
                self.click(*self.confirm)
                self.forced_wait(*self.reminder)
                reminder = self.get_element(*self.reminder)
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_inspector_reminder))
                    logger.info(self.get_element(*self.delete_inspector_reminder))
                    self.get_windows_img()
                except Exception:
                    # noinspection PyBroadException
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel))
                        self.click(*self.cancel)
                        logger.error(f"{reminder}")
                        logger.error("删除检视专家有问题!")
                        self.get_windows_img()
                        return False
                    except Exception:
                        logger.error(f"{reminder}")
                        logger.error(f"删除检视专家有问题!")
                        self.get_windows_img()
                        return False
                after = time.time()
                if after - before > 12 or times > 5:
                    break
            except Exception:
                break
        if times == 0:
            logger.info("该域没有检视专家!")
        return True

    def create_inspector(self):
        self.click(*self.create_inspector_button)
        self.input(self.get_element(*self.username_element), *self.input_inspector)
        self.sleep(3)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.first_group))
            logger.info("找到自己作为候选人员.")
        except Exception as e:
            logger.error("未找到自己的账号!")
            logger.error(e)
            self.get_windows_img()
            return False
        inspector = self.get_element(*self.first_group)
        self.click(*self.first_group)
        try:
            WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located(self.delete_input))
            WebDriverWait(self.driver, 3, 1).until(EC.presence_of_element_located(self.delete_create))
            logger.info(f"检视专家:{inspector} 已被添加到候选列表.")
        except Exception as e:
            logger.error(f"检视专家：{inspector} 未被添加到候选列表!")
            logger.error(e)
            self.get_windows_img()
            return False
        self.click(*self.delete_create)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 2, 1).until(EC.presence_of_element_located(self.delete_input))
            logger.error(f'检视专家:{inspector} 输入框未被清除!')
            self.get_windows_img()
            return False
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 2, 1).until(EC.presence_of_element_located(self.delete_create))
                logger.error(f"检视专家:{inspector} 候选列表未被删除!")
                self.get_windows_img()
                return False
            except Exception:
                logger.info(f"检视专家:{inspector} 已被删除候选.")
        self.input(self.get_element(*self.username_element), *self.input_inspector)
        self.sleep(3)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.first_group))
            logger.info("找到自己作为候选人员.")
        except Exception as e:
            logger.error("未找到自己的账号!")
            logger.error(e)
            self.get_windows_img()
            return False
        self.click(*self.first_group)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_input))
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_create))
            logger.info(f"检视专家:{inspector} 已被添加到候选列表.")
        except Exception as e:
            logger.error(f"检视专家：{inspector} 未被添加到候选列表!")
            logger.error(e)
            self.get_windows_img()
            return False
        self.click(*self.confirm)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.create_inspector_reminder))
            logger.info(self.get_element(*self.create_inspector_reminder))
            self.get_windows_img()
            return True
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel))
                self.click(*self.cancel)
                logger.error(f"{reminder}")
                logger.error("增加检视专家有问题!")
                self.get_windows_img()
                return False
            except Exception:
                logger.error(f"{reminder}")
                logger.error(f"增加检视专家有问题!")
                self.get_windows_img()
                return False
