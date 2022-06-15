import os
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'import_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    import_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)

result = None


class Import_Management_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_import_management = (method_json["method"][0], menu_json["cd1_setting"]["import_management"][0])
    staging_import_management = (method_json["method"][0], menu_json["staging_setting"]["import_management"][0])
    none_data = (method_json["method"][0], import_management_json["none_data"][0])
    create = (method_json["method"][0], import_management_json["create"]["button"][0])
    person_db = (method_json["method"][0], import_management_json["create"]["person_db"][0])
    case_db = (method_json["method"][0], import_management_json["create"]["case_db"][0])
    import_db = (method_json["method"][0], import_management_json["create"]["target_import_db"][0])
    data_type1 = (method_json["method"][0], import_management_json["create"]["data_type"][0])
    TL_LL_match_db = (method_json["method"][0], import_management_json["create"]["TL_LL_match_db"][0])
    TL_LL_text = (method_json["method"][0], import_management_json["create"]["TL_LL_text"][0])
    LT_TT_match_db = (method_json["method"][0], import_management_json["create"]["LT_TT_match_db"][0])
    LT_TT_text = (method_json["method"][0], import_management_json["create"]["LT_TT_text"][0])
    match_priority1 = (method_json["method"][0], import_management_json["create"]["match_priority"][0])
    group_change_true = (method_json["method"][0], import_management_json["create"]["group_change_true"][0])
    group_change_false = (method_json["method"][0], import_management_json["create"]["group_change_false"][0])
    import_change_true = (method_json["method"][0], import_management_json["create"]["import_change_true"][0])
    import_change_false = (method_json["method"][0], import_management_json["create"]["import_change_false"][0])
    type_first = (method_json["method"][0], import_management_json["create"]["type_first"][0])
    type_last = (method_json["method"][0], import_management_json["create"]["type_last"][0])
    confirm = (method_json["method"][0], import_management_json["create"]["confirm"][0])
    cancel = (method_json["method"][0], import_management_json["create"]["cancel"][0])
    target_import_db = (method_json["method"][0], import_management_json["target_import_db"][0])
    target_match_db = (method_json["method"][0], import_management_json["target_match_db"][0])
    match_type = (method_json["method"][0], import_management_json["match_type"][0])
    data_type2 = (method_json["method"][0], import_management_json["data_type"][0])
    match_priority2 = (method_json["method"][0], import_management_json["match_priority"][0])
    group_change = (method_json["method"][0], import_management_json["group_change"][0])
    import_change = (method_json["method"][0], import_management_json["import_change"][0])
    last_editor = (method_json["method"][0], import_management_json["last_editor"][0])
    last_edit_time = (method_json["method"][0], import_management_json["last_edit_time"][0])
    delete = (method_json["method"][0], import_management_json["action"]["delete"][0])
    confirm2 = (method_json["method"][0], import_management_json["action"]["confirm"][0])
    cancel2 = (method_json["method"][0], import_management_json["action"]["cancel"][0])
    attribute_value = import_management_json["attribute_value"][0]
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    create_reminder = (method_json["method"][0], reminder_json["create"][0])
    delete_reminder = (method_json["method"][0], reminder_json["delete"][0])

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

    def check_import_settings(self):
        global result
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_import_management)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_import_management)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.none_data))
            logger.info("该域没有入库设置.")
            result = True
            return result
        except Exception:
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                logger.info("该域有入库设置.")
                result = False
                return result
            except Exception:
                logger.error("前端界面展示有问题!")
                self.get_windows_img()
                result = False
                return result

    def check_create_import_settings_button(self):
        global result
        if result:
            self.click(*self.create)
            if self.attribute_value in self.find_element_attribute('class', *self.person_db):
                if self.attribute_value not in self.find_element_attribute('class', *self.case_db):
                    logger.info("默认入库目标库为人员库.")
                else:
                    logger.error("默认入库目标库都被选中!")
                    self.get_windows_img()
                    result = False
                    return False
            else:
                if self.attribute_value in self.find_element_attribute('class', *self.case_db):
                    logger.error("默认入库目标库为案件库!")
                    self.get_windows_img()
                    result = False
                    return False
                else:
                    logger.error("默认入库目标库都未被选中!")
                    self.get_windows_img()
                    result = False
                    return False
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.TL_LL_text, '倒查'))
                WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.LT_TT_text, '查重'))
                logger.info("比对目标库比对方式没有问题.")
            except Exception as e:
                logger.error("比对目标库比对方式存在问题!")
                logger.error(e)
                self.get_windows_img()
                result = False
                return False
            if self.attribute_value in self.find_element_attribute('class', *self.group_change_true):
                if self.attribute_value not in self.find_element_attribute('class', *self.group_change_false):
                    logger.info("默认子用户组可以修改.")
                else:
                    logger.error("默认子用户组修改权限都被选中!")
                    self.get_windows_img()
                    result = False
                    return False
            else:
                if self.attribute_value in self.find_element_attribute('class', *self.group_change_false):
                    logger.error("默认子用户组不可以修改!")
                    self.get_windows_img()
                    result = False
                    return False
                else:
                    logger.error("默认子用户组修改权限都未被选中!")
                    self.get_windows_img()
                    result = False
                    return False
            if self.attribute_value in self.find_element_attribute('class', *self.import_change_true):
                if self.attribute_value not in self.find_element_attribute('class', *self.import_change_false):
                    logger.info("默认导入时可临时修改.")
                    return True
                else:
                    logger.error("默认导入时修改权限都被选中!")
                    self.get_windows_img()
                    result = False
                    return False
            else:
                if self.attribute_value in self.find_element_attribute('class', *self.import_change_false):
                    logger.error("默认导入时不可以修改!")
                    self.get_windows_img()
                    result = False
                    return False
                else:
                    logger.error("默认导入时修改权限都未被选中!")
                    self.get_windows_img()
                    result = False
                    return False
        else:
            logger.error("上一个测试用例测试失败,当前测试用例当做失败处理!")
            return False

    def switch_import_settings_button(self):
        global result
        if result:
            # 切换成案件库
            self.click(*self.case_db)
            if self.attribute_value in self.find_element_attribute('class', *self.case_db):
                if self.attribute_value not in self.find_element_attribute('class', *self.person_db):
                    logger.info("入库类别设置按钮切换成功.")
                else:
                    logger.error("人员库按钮未取消选中状态!")
                    self.get_windows_img()
                    result = False
                    return False
            else:
                if self.attribute_value not in self.find_element_attribute('class', *self.person_db):
                    logger.error("案件库按钮未成为选中状态!")
                    self.get_windows_img()
                    result = False
                    return False
                else:
                    logger.error("按钮未变化,切换按钮失败!")
                    self.get_windows_img()
                    result = False
                    return False
            if '案件库' in self.get_element(*self.import_db):
                logger.info("系统入库目标库显示成功.")
            else:
                logger.error("系统入库目标库显示失败!")
                logger.error(f"系统入库目标库为:{self.get_element(*self.import_db)}")
                self.get_windows_img()
                result = False
                return False
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.TL_LL_text, '串查'))
                WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.LT_TT_text, '正查'))
                logger.info("切换后入库目标库后比对目标库比对方式没有问题.")
            except Exception as e:
                logger.error("切换后入库目标库后比对目标库比对方式存在问题!")
                logger.error(e)
                self.get_windows_img()
                result = False
                return False
            # 再次切换回人员库看是否出现按钮还原
            self.click(*self.person_db)
            if self.attribute_value in self.find_element_attribute('class', *self.person_db):
                if self.attribute_value not in self.find_element_attribute('class', *self.case_db):
                    logger.info("入库类别设置按钮切换回来成功.")
                else:
                    logger.error("案件库按钮未取消选中状态!")
                    self.get_windows_img()
                    result = False
                    return False
            else:
                if self.attribute_value not in self.find_element_attribute('class', *self.case_db):
                    logger.error("人员库按钮未成为选中状态!")
                    self.get_windows_img()
                    result = False
                    return False
                else:
                    logger.error("按钮未变化,切换按钮失败!")
                    self.get_windows_img()
                    result = False
                    return False
            if '人员库' in self.get_element(*self.import_db):
                logger.info("系统入库目标库显示成功.")
            else:
                logger.error("系统入库目标库显示失败!")
                logger.error(f"系统入库目标库为:{self.get_element(*self.import_db)}")
                self.get_windows_img()
                result = False
                return False
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.TL_LL_text, '倒查'))
                WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.LT_TT_text, '查重'))
                logger.info("切换回来后入库目标库后比对目标库比对方式没有问题.")
            except Exception as e:
                logger.error("切换回来后入库目标库后比对目标库比对方式存在问题!")
                logger.error(e)
                self.get_windows_img()
                result = False
                return False
            # 切换子用户可修改权限为否
            self.click(*self.group_change_false)
            if self.attribute_value in self.find_element_attribute('class', *self.group_change_false):
                if self.attribute_value not in self.find_element_attribute('class', *self.group_change_true):
                    logger.info("子用户组可修改权限切换成功.")
                else:
                    logger.error("'是'按钮未取消选中状态")
                    self.get_windows_img()
                    result = False
                    return False
            else:
                if self.attribute_value not in self.find_element_attribute('class', *self.person_db):
                    logger.error("'否'按钮未变为选中状态!")
                    self.get_windows_img()
                    result = False
                    return False
                else:
                    logger.error("按钮未变化,切换按钮失败!")
                    self.get_windows_img()
                    result = False
                    return False
            # 切换导入时临时修改权限为否
            self.click(*self.import_change_false)
            if self.attribute_value in self.find_element_attribute('class', *self.import_change_false):
                if self.attribute_value not in self.find_element_attribute('class', *self.import_change_true):
                    logger.info("导入时可临时修改权限切换成功.")
                    return True
                else:
                    logger.error("'是'按钮未取消选中状态")
                    self.get_windows_img()
                    result = False
                    return False
            else:
                if self.attribute_value not in self.find_element_attribute('class', *self.import_change_true):
                    logger.error("'否'按钮未变为选中状态!")
                    self.get_windows_img()
                    result = False
                    return False
                else:
                    logger.error("按钮未变化,切换按钮失败!")
                    self.get_windows_img()
                    result = False
                    return False
        else:
            logger.error("上一个测试用例测试失败,当前测试用例当做失败处理!")
            return False

    def create_import_settings(self):
        global result
        if result:
            self.refresh_browser()
            self.click(*self.create)
            self.click(*self.import_db)
            # 选择下拉列表的选项(默认选择第一个)
            target_import_db = self.get_element(*self.type_first)
            self.click(*self.type_first)
            self.sleep(0.5)
            self.click(*self.data_type1)
            self.click(*self.type_last)
            self.sleep(0.5)
            self.click(*self.TL_LL_match_db)
            self.click(*self.type_first)
            # 点击空白处让下拉列表消失
            self.actionchains_click(*self.TL_LL_text)
            self.click(*self.LT_TT_match_db)
            self.click(*self.type_first)
            self.actionchains_click(*self.LT_TT_text)
            # 选择最低优先级算力消耗
            self.click(*self.match_priority1)
            self.click(*self.type_last)
            # 默认选择子用户可修改和导入时可临时修改
            self.click(*self.confirm)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.create_reminder))
                logger.info(f"{self.get_element(*self.create_reminder)}")
                self.get_windows_img()
            except Exception:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel))
                    self.click(*self.cancel)
                    logger.error(f"{reminder}")
                    logger.error("新建入库设置有问题!")
                    self.get_windows_img()
                    result = False
                    return False
                except Exception:
                    logger.error(f"{reminder}")
                    logger.error("新建入库设置有问题!")
                    self.get_windows_img()
                    result = False
                    return False
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.target_import_db))
                if target_import_db == self.get_element(*self.target_import_db):
                    logger.info("新建入库设置成功.")
                    self.get_windows_img()
                    return True
                else:
                    logger.error("新建入库设置和选择的不一致!")
                    logger.error(self.get_element(*self.target_import_db))
                    self.get_windows_img()
                    result = False
                    return False
            except Exception as e:
                logger.error("新建入库设置前端未显示!")
                logger.error(e)
                self.get_windows_img()
                result = False
                return False
        else:
            logger.error("上一个测试用例测试失败,当前测试用例当做失败处理!")
            return False

    def delete_import_settings(self):
        times = 0
        while True:
            # noinspection PyBroadException
            try:
                before = time.time()
                self.sleep(1)
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete))
                logger.warning(f"即将删除 入库目标库:{self.get_element(*self.target_import_db)}\n"
                               f"比对目标库:{self.get_element(*self.target_match_db)}\n"
                               f"比对类型:{self.get_element(*self.match_type)}\n"
                               f"入库数据类型:{self.get_element(*self.data_type2)}\n"
                               f"比对优先级：{self.get_element(*self.match_priority2)}\n"
                               f"子用户组修改配置权限：{self.get_element(*self.group_change)}\n"
                               f"导入页临时修改权限：{self.get_element(*self.group_change)}\n"
                               f"最后编辑者：{self.get_element(*self.last_editor)}\n"
                               f"最后编辑时间：{self.get_element(*self.last_edit_time)} 入库设置.")
                self.execute_script_click(*self.delete)
                times = times + 1
                self.click(*self.confirm2)
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
                        WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel2))
                        self.click(*self.cancel2)
                        logger.error(f"{reminder}")
                        logger.error("删除入库设置有问题!")
                        self.get_windows_img()
                        return False
                    except Exception:
                        logger.error(f"{reminder}")
                        logger.error("删除入库设置有问题!")
                        self.get_windows_img()
                        return False
                after = time.time()
                # 限定时间和次数避免死循环
                if after - before > 12 or times > 5:
                    break
            except Exception:
                break
        return True
