import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from framework.logger import Logger
from page_objects.common_login.login import Login

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'import_file'), 'import_page.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    import_page_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

result = None


class Import_File_Page(BasePage):
    import_button = (method_json["method"][0], import_page_json["import"][0])
    upload = (method_json["method"][0], import_page_json["upload"]["button"][0])
    case_db = (method_json["method"][0], import_page_json["upload"]["case_database"][0])
    person_db = (method_json["method"][0], import_page_json["upload"]["person_database"][0])
    target_db = (method_json["method"][0], import_page_json["upload"]["target_database"][0])
    import_fpt = (method_json["method"][0], import_page_json["upload"]["import_fpt"][0])
    import_bmp = (method_json["method"][0], import_page_json["upload"]["import_bmp"][0])
    not_override = (method_json["method"][0], import_page_json["upload"]["not_override"][0])
    override = (method_json["method"][0], import_page_json["upload"]["override"][0])
    auto_match = (method_json["method"][0], import_page_json["upload"]["auto_match"][0])
    not_auto_match = (method_json["method"][0], import_page_json["upload"]["not_auto_match"][0])
    change_auto_match = (method_json["method"][0], import_page_json["upload"]["change_auto_match"][0])
    import_file = (method_json["method"][0], import_page_json["upload"]["upload"][0])
    disabled_import_file = (method_json["method"][0], import_page_json["upload"]["disabled_upload"][0])
    attribute_value = import_page_json["upload"]["attribute_value"][0]

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def enter_import_file_page(self):
        global result
        self.sleep(1)
        self.click(*self.import_button)
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

    def check_default_buttons(self):
        global result
        if result:
            if self.attribute_value in self.find_element_attribute('class', *self.case_db):
                logger.info("上传库默认选中案件库.")
                try:
                    # 显示等待直到找到包含'案件库'的文本
                    WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.target_db, '案件库'))
                    logger.info("目标库没有问题.")
                except Exception as e:
                    logger.error(f"目标库为:{self.get_element(*self.target_db)},存在问题!")
                    logger.error(e)
                    self.get_windows_img()
                    result = False
                    return result
            elif self.attribute_value in self.find_element_attribute('class', *self.person_db):
                logger.error("上传库默认选中人员库!")
                self.get_windows_img()
                result = False
                return result
            else:
                logger.error("上传库未被默认选中!")
                self.get_windows_img()
                result = False
                return result
            if self.attribute_value in self.find_element_attribute('class', *self.import_fpt):
                logger.info("上传文件默认为 FPT 格式.")
            elif self.attribute_value in self.find_element_attribute('class', *self.import_bmp):
                logger.error("上传文件默认为 BMP 格式!")
                self.get_windows_img()
                result = False
                return result
            else:
                logger.error("上传文件未被选中!")
                self.get_windows_img()
                result = False
                return result
            if self.attribute_value in self.find_element_attribute('class', *self.not_override):
                logger.info("覆盖类型默认选中不覆盖.")
            elif self.attribute_value in self.find_element_attribute('class', *self.override):
                logger.error("覆盖类型默认选中覆盖!")
                self.get_windows_img()
                result = False
                return result
            else:
                logger.error("覆盖类型未被选中!")
                self.get_windows_img()
                result = False
                return result
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled_import_file))
                logger.info("开始导入 button 当前无法点击.")
                return True
            except Exception as e:
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.import_file))
                    logger.error("开始导入 button 当前可以点击!")
                    logger.error(e)
                    self.get_windows_img()
                    result = False
                    return result
                except Exception as e:
                    logger.error("开始导入 button 存在问题!")
                    logger.error(e)
                    self.get_windows_img()
                    result = False
                    return result
        else:
            logger.error("上一个测试用例测试失败,当前测试用例当做失败处理!")
            return False

    def switch_buttons(self):
        global result
        if result:
            self.click(*self.person_db)
            if self.attribute_value not in self.find_element_attribute('class', *self.case_db):
                if self.attribute_value in self.find_element_attribute('class', *self.person_db):
                    logger.info('切换目标库成功.')
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.target_db, '人员库'))
                        logger.info("目标库没有问题.")
                    except Exception as e:
                        logger.error(f"目标库为:{self.get_element(*self.target_db)},存在问题!")
                        logger.error(e)
                        self.get_windows_img()
                        result = False
                        return result
            else:
                logger.error('按钮切换失败!')
                self.get_windows_img()
                result = False
                return result
            self.click(*self.import_bmp)
            if self.attribute_value not in self.find_element_attribute('class', *self.import_fpt):
                if self.attribute_value in self.find_element_attribute('class', *self.import_bmp):
                    logger.info('切换导入文件类型成功.')
            else:
                logger.error('按钮导入文件类型失败!')
                self.get_windows_img()
                result = False
                return result
            self.click(*self.override)
            if self.attribute_value not in self.find_element_attribute('class', *self.import_fpt):
                if self.attribute_value in self.find_element_attribute('class', *self.import_bmp):
                    logger.info('切换覆盖类型成功.')
            else:
                logger.error('切换覆盖类型失败!')
                self.get_windows_img()
                result = False
                return result
        else:
            logger.error("上一个测试用例测试失败,当前测试用例当做失败处理!")
            return False
