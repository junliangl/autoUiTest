import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.base_page import BasePage
from page_objects.common_login.login import Login

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'menu'), 'help.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    help_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)


class Help_Page(BasePage):
    help_button = (method_json["method"][0], menu_json["help"][0])
    phone_number = (method_json["method"][0], help_json["phone"][0])
    QR_code = (method_json["method"][0], help_json["QR_code"][0])
    we_chat = (method_json["method"][0], help_json["we_chat"][0])
    work_date = (method_json["method"][0], help_json["work_date"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def look_help(self):
        self.click(*self.help_button)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.phone_number))
            logger.info("打开帮助菜单成功.")
        except Exception as e:
            logger.error("打开帮助菜单失败!")
            logger.error(e)
            self.get_windows_img()
            return False
        self.sleep(1)
        logger.info(f"信息如下------ phone_number:{self.get_element(*self.phone_number)} "
                    f"we_chat:{self.get_element(*self.we_chat)} "
                    f"work_date:{self.get_element(*self.work_date)}")
        self.get_windows_img()
        return True
