import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from framework.logger import Logger
from page_objects.common_login.login import Login

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file1 = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'import_file'), 'import_page.json')
json_file2 = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'import_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file1, encoding='utf-8') as file1:
    import_page_json = json.load(file1)

with open(json_file2, encoding='utf-8') as file2:
    import_management_json = json.load(file2)

with open(menu_file, encoding='utf-8') as file3:
    menu_json = json.load(file3)

with open(method_file, encoding='utf-8') as file4:
    method_json = json.load(file4)

result = None
exist = None
setting = None

class Import_File_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_import_management = (method_json["method"][0], menu_json["cd1_setting"]["import_management"][0])
    staging_import_management = (method_json["method"][0], menu_json["staging_setting"]["import_management"][0])
    target_import_db = (method_json["method"][0], import_management_json["target_import_db"][0])
    delete = (method_json["method"][0], import_management_json["action"]["delete"][0])
    none_data = (method_json["method"][0], import_management_json["none_data"][0])
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
    disabled_change_auto_match = (method_json["method"][0], import_page_json["upload"]["disabled_change_auto_match"][0])
    import_file = (method_json["method"][0], import_page_json["upload"]["upload"][0])
    disabled_import_file = (method_json["method"][0], import_page_json["upload"]["disabled_upload"][0])
    attribute_value = import_page_json["upload"]["attribute_value"][0]

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

    def check_import_setting_exist(self):
        global setting
        global exist
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_import_management)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_import_management)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
            logger.info("该域有库设置.")
            setting = self.get_element(*self.target_import_db)
            exist = True
            return True
        except Exception:
            logger.error("该域没有入库设置!")
            self.get_windows_img()
            exist = False
            return False

    def enter_import_file_page(self):
        global result
        self.refresh_browser()
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
                logger.error('切换导入文件类型按钮失败!')
                self.get_windows_img()
                result = False
                return result
            self.click(*self.override)
            if self.attribute_value not in self.find_element_attribute('class', *self.not_override):
                if self.attribute_value in self.find_element_attribute('class', *self.override):
                    logger.info('切换覆盖类型成功.')
            else:
                logger.error('切换覆盖类型失败!')
                self.get_windows_img()
                result = False
                return result
            # 如果存在入库设置
            if exist:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.not_auto_match))
                    # 如果上面查看到的自动入库设置目标库和当前统一就继续执行
                    if setting == self.get_element(*self.target_db):
                        if self.attribute_value in self.find_element_attribute('class', *self.not_auto_match):
                            logger.info("自动类型默认选中不自动比对.")
                        elif self.attribute_value in self.find_element_attribute('class', *self.auto_match):
                            logger.error("自动比对类型默认选中自动比对!")
                            self.get_windows_img()
                            result = False
                            return result
                        else:
                            logger.error("自动比对类型未被选中!")
                            self.get_windows_img()
                            result = False
                            return result
                    else:
                        logger.error("自动入库设置目标库不一致却显示自动入库设置button!")
                        self.get_windows_img()
                        result = False
                        return result
                except Exception:
                    if setting == self.get_element(*self.target_db):
                        logger.error("该目标库有入库设置却不显示自动入库设置button!")
                        self.get_windows_img()
                        result = False
                        return result
                    else:
                        logger.error("显示了非法目标库!")
                        logger.error(self.get_element(*self.target_db))
                        self.get_windows_img()
                        result = False
                        return result
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.disabled_change_auto_match))
                    logger.info("修改自动比对设置无法被点击.")
                    try:
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.change_auto_match))
                        logger.error("修改自动比对设置可以被点击!")
                    except Exception as e:
                        logger.error(e)
                        self.get_windows_img()
                        result = False
                        return False
                except Exception as e:
                    logger.error(e)
                    self.get_windows_img()
                    result = False
                    return False
                self.click(*self.auto_match)
                if self.attribute_value not in self.find_element_attribute('class', *self.not_auto_match):
                    if self.attribute_value in self.find_element_attribute('class', *self.auto_match):
                        try:
                            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.change_auto_match))
                            logger.info('切换自动入库设置button成功.')
                        except Exception as e:
                            logger.error('切换按钮自动入库设置button失败!')
                            logger.error(e)
                            self.get_windows_img()
                            return False
                else:
                    logger.error('切换按钮自动入库设置button失败!')
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




    # def import_data_file(self):
    #     if result:
    #         self.refresh_browser()
    #         self.click(*self.person_db)
    #         self.click(*self.import_bmp)
    #         self.click(*self.override)
    #         self.click(*self.import_file)
    #         self.click(*self.)
    #     else:
    #         logger.error("上一个测试用例测试失败,当前测试用例当做失败处理!")
    #         return False