import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from framework.logger import Logger
from page_objects.common_login.login import Login

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'import'), 'import_page.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    import_page_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

result = None

class Import_Page(BasePage):
    import_button = (method_json[0], import_page_json["import"][0])
    upload = (method_json["method"][0], import_page_json["upload"]["button"][0])
    case_db = (method_json["method"][0], import_page_json["upload"]["case_database"][0])
    person_db = (method_json["method"][0], import_page_json["upload"]["person_database"][0])
    target_db = (method_json["method"][0], import_page_json["upload"]["target_database"][0])
    import_fpt = (method_json["method"][0], import_page_json["upload"]["import_fpt"][0])
    import_bmp = (method_json["method"][0], import_page_json["upload"]["import_bmp"][0])
    not_override = (method_json["method"][0], import_page_json["upload"]["not_override"][0])
    override = (method_json["method"][0], import_page_json["upload"]["override"][0])
    attribute_value =  (method_json["method"][0], import_page_json["upload"]["attribute_value"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def into_import_detail_page(self):
        global result
        self.click(self.import_button)
        self.click(*self.upload)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.target_db))
            logger.info("进入导入界面成功.")
            result = True
            return result
        except Exception as e:
            logger.error('进入导入界面失败!')
            logger.error(e)
            self.get_windows_img()
            result = False
            return result

    def choose_conditions(self):
        if result:
            if self.attribute_value in self.find_element_attribute('class', *self.case_db):
                logger.info("上传库默认选中案件库.")
            elif self.attribute_value in self.find_element_attribute('class', *self.person_db):
                logger.error("上传库默认选中人员库!")
                self.get_windows_img()
            else:
                logger.error("上传库未被默认选中!")
                self.get_windows_img()
            # if self.attribute_value in self.find_element_attribute('class', )
        else:
            pass