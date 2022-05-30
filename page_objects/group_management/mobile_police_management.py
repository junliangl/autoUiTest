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
file = 'mobile_police_management.json'
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), file)
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    mobile_police_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)


class Mobile_Police_Management_Page(BasePage):
    username_element = (method_json["method"][0], menu_json["user"]["button"][0])
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_mobile_police_management = (method_json["method"][0], menu_json["cd1_setting"]["mobile_police_management"][0])
    staging_mobile_police_management = (method_json["method"][0], menu_json["staging_setting"]["mobile_police_management"][0])
    none_data = (method_json["method"][0], mobile_police_management_json["none_data"][0])
    id = (method_json["method"][0], mobile_police_management_json["first_user"]["id"][0])
    username = (method_json["method"][0], mobile_police_management_json["first_user"]["username"][0])
    name = (method_json["method"][0], mobile_police_management_json["first_user"]["name"][0])
    date = (method_json["method"][0], mobile_police_management_json["first_user"]["date"][0])
    delete = (method_json["method"][0], mobile_police_management_json["first_user"]["delete"][0])
    bulk_import = (method_json["method"][0], mobile_police_management_json["bulk_import"]["button"][0])
    import_csv_file = (method_json["method"][0], mobile_police_management_json["bulk_import"]["import"][0])
    delete_file = (method_json["method"][0], mobile_police_management_json["bulk_import"]["delete_file"][0])
    cancel_task = (method_json["method"][0], mobile_police_management_json["bulk_import"]["cancel_task"]["button"][0])
    next_step = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["button"][0])
    disabled_next_step = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["disabled"][0])
    add_user_number = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["add_user_number"][0])
    success_number = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["success"][0])
    fail_number = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["fail"][0])
    export_detail = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["export"][0])
    submit = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["submit"][0])
    disabled_submit = (method_json["method"][0], mobile_police_management_json["bulk_import"]["next_step"]["disabled_submit"][0])
    add_user = (method_json["method"][0], mobile_police_management_json["add_user"]["button"][0])
    police_id = (method_json["method"][0], mobile_police_management_json["add_user"]["police_id"][0])
    police_username = (method_json["method"][0], mobile_police_management_json["add_user"]["username"][0])
    police_first_username = (method_json["method"][0], mobile_police_management_json["add_user"]["first_username"][0])
    confirm1_button = (method_json["method"][0], mobile_police_management_json["add_user"]["confirm_button"][0])
    cancel1_button = (method_json["method"][0], mobile_police_management_json["add_user"]["cancel_button"][0])
    confirm2_button = (method_json["method"][0], mobile_police_management_json["bulk_import"]["cancel_task"]["confirm_button"][0])
    cancel2_button = (method_json["method"][0], mobile_police_management_json["bulk_import"]["cancel_task"]["cancel_button"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    success_reminder = (method_json["method"][0], reminder_json["add_mobile_police_success"][0])
    fail_reminder = (method_json["method"][0], reminder_json["import_mobile_user_fail"][0])
    delete_reminder = (method_json["method"][0], reminder_json["delete"][0])
    export_reminder = (method_json["method"][0], reminder_json["export"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def check_mobile_police_user(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_mobile_police_management)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_mobile_police_management)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.none_data))
            logger.info("该域没有移动警务管理人员.")
            return True
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                logger.info("该域有移动管理人员.")
                return True
            except Exception:
                logger.error("前端界面展示有问题")
                self.get_windows_img()
                return False

    def add_mobile_police_user(self):
        self.click(*self.add_user)
        self.input(self.get_random_number(), *self.police_id)
        self.click(*self.police_username)
        self.click(*self.police_first_username)
        self.click(*self.confirm1_button)
        self.forced_wait(*self.reminder)
        reminder = self.get_element(*self.reminder)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.success_reminder))
            logger.info(f"{self.get_element(*self.success_reminder)}")
            self.get_windows_img()
            return True
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel1_button))
                self.click(*self.cancel1_button)
                logger.error(f"{reminder}")
                logger.error("添加警务人员有问题!")
                self.get_windows_img()
                return False
            except Exception:
                logger.error(f"{reminder}")
                logger.error(f"添加警务人员有问题!")
                self.get_windows_img()
                return False

    def import_mobile_police_file(self):
        username = self.get_element(*self.username_element)
        column = ['移动警务ID', '用户名']
        raw = [[self.get_random_number(), username]]
        csv_path = self.create_csv(column, raw)
        self.click(*self.bulk_import)
        self.click(*self.import_csv_file)
        self.sleep(2)
        self.import_file(csv_path)
        self.click(*self.delete_file)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled_next_step))
            logger.info("删除当前上传文件成功.")
        except Exception as e:
            logger.error("删除当前上传文件失败.")
            logger.error(e)
            self.get_windows_img()
            return False
        self.click(*self.import_csv_file)
        if csv_path:
            self.import_file(csv_path)
            # 如果创建文件成功导入后就删除
            try:
                os.remove(csv_path)
            except Exception as e:
                logger.error("删除文件失败")
                logger.error(e)
        else:
            logger.error("csv文件路径为None.")
            return False
        self.click(*self.next_step)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.fail_reminder))
            self.get_windows_img()
            logger.error(self.get_element(*self.fail_reminder))
            return False
        except Exception:
            logger.info("上传成功.")
        self.forced_wait(*self.fail_number)
        success_number = self.get_element(*self.success_number)
        fail_number = self.get_element(*self.fail_number)
        logger.info(self.get_element(*self.add_user_number))
        logger.info(self.get_element(*self.success_number))
        logger.info(self.get_element(*self.fail_number))
        if success_number[-1] == '0' and success_number[-2] == '：':
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled_submit))
                logger.info("由于正确文件数量为0,上传不了.")
                self.click(*self.export_detail)
                reminder = self.get_element(*self.reminder)
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.export_reminder))
                    logger.info(f"{self.get_element(*self.export_reminder)}")
                    self.get_windows_img()
                except Exception:
                    logger.error(f"{reminder}")
                    logger.error(f"导出名单有问题!")
                    self.get_windows_img()
                    return False
            except Exception as e:
                logger.error("正确文件数量为0,还可以继续上传,上传存在问题.")
                logger.error(e)
                self.get_windows_img()
                return False
        elif fail_number[-1] == '0' and fail_number[-2] == '：':
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled_submit))
                logger.error("现在全部正常导入,但是不能正常提交")
                self.get_windows_img()
            except Exception:
                logger.info("现在全部正常导入,可以正常提交.")
                self.click(*self.submit)
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                    logger.info("导入成功.")
                    return True
                except Exception:
                    logger.error("导入失败.")
                    self.get_windows_img()
                    return False
        else:
            self.click(*self.export_detail)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.export_reminder))
                logger.info(f"{self.get_element(*self.export_reminder)}")
                self.get_windows_img()
            except Exception:
                logger.error(f"{reminder}")
                logger.error(f"导出名单有问题!")
                self.get_windows_img()
                return False
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled_submit))
                logger.error("现在全部正常导入,但是不能正常提交")
                self.get_windows_img()
                return False
            except Exception:
                logger.info("现在全部正常导入,可以正常提交.")
                self.click(*self.submit)
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                    logger.info("导入成功.")
                    return True
                except Exception:
                    logger.error("导入失败.")
                    self.get_windows_img()
                    return False

    def delete_mobile_police_user(self):
        times = 0
        while True:
            # noinspection PyBroadException
            try:
                before = time.time()  # 当前时间
                self.sleep(1)
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                logger.warning(f"即将删除 id:{self.get_element(*self.id)} username:{self.get_element(*self.username)} "
                               f"name:{self.get_element(*self.name)} date:{self.get_element(*self.date)} 检视人员")
                self.execute_script_click(*self.delete)
                times = times + 1
                self.click(*self.confirm2_button)
                self.forced_wait(*self.reminder)
                reminder = self.get_element(*self.reminder)
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_reminder))
                    logger.info(f"{self.get_element(*self.delete_reminder)}")
                    self.get_windows_img()
                except Exception:
                    # noinspection PyBroadException
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel2_button))
                        self.click(*self.cancel2_button)
                        logger.error(f"{reminder}")
                        logger.error("删除警务人员有问题!")
                        self.get_windows_img()
                        return False
                    except Exception:
                        logger.error(f"{reminder}")
                        logger.error(f"删除警务人员有问题!")
                        self.get_windows_img()
                        return False
                after = time.time()  # 完成删除事件后时间
                # 限定时间和次数避免死循环
                if after - before > 12 or times > 5:
                    break
            except Exception:
                break
        return True
