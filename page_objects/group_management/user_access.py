import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'user_access.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    user_access_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)


class User_Access_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_user_access_element = (method_json["method"][0], menu_json["cd1_setting"]["user_access"][0])
    staging_user_access_element = (method_json["method"][0], menu_json["staging_setting"]["user_access"][0])
    child_group1_element = (method_json["method"][0], user_access_json["child_group"]["child_group1"][0])
    child_group2_element = (method_json["method"][0], user_access_json["child_group"]["child_group2"][0])
    role_group1_element = (method_json["method"][0], user_access_json["role_group"]["role1"][0])
    role_group2_element = (method_json["method"][0], user_access_json["role_group"]["role2"][0])
    basic_info = (method_json["method"][0], user_access_json["basic_information"]["basic_info"][0])
    edit_basic_info = (method_json["method"][0], user_access_json["basic_information"]["edit_basic_info"][0])
    edit_basic_info_forbidden = (method_json["method"][0], user_access_json["basic_information"]["edit_basic_forbidden"][0])
    child_name_input = (method_json["method"][0], user_access_json["basic_information"]["child_name_input"][0])
    child_user_group_code = (method_json["method"][0], user_access_json["basic_information"]["child_user_group_code"][0])
    group_region_code = (method_json["method"][0], user_access_json["basic_information"]["group_region_code"][0])
    choose_department = (method_json["method"][0], user_access_json["basic_information"]["department"][0])
    choose_province = (method_json["method"][0], user_access_json["basic_information"]["province"][0])
    choose_city = (method_json["method"][0], user_access_json["basic_information"]["city"][0])
    choose_district = (method_json["method"][0], user_access_json["basic_information"]["district"][0])
    confirm_button = (method_json["method"][0], user_access_json["confirm_button"][0])
    cancel_button = (method_json["method"][0], user_access_json["cancel_button"][0])
    user_management = (method_json["method"][0], user_access_json["user_management"]["user_management"][0])
    next_page = (method_json["method"][0], user_access_json["user_management"]["next_page"][0])
    last_page = (method_json["method"][0], user_access_json["user_management"]["last_page"][0])
    invite_to_group = (method_json["method"][0], user_access_json["action"]["invite_to_group"][0])
    delete_group = (method_json["method"][0], user_access_json["action"]["delete_child_group"][0])
    cannot_delete_group = (method_json["method"][0], user_access_json["action"]["cannot_delete_group"][0])
    delete_role = (method_json["method"][0], user_access_json["action"]["delete_role_group"][0])
    cannot_delete_role = (method_json["method"][0], user_access_json["action"]["cannot_delete_role"][0])
    add_child_group = (method_json["method"][0], user_access_json["action"]["add_child_group"][0])
    add_role_group = (method_json["method"][0], user_access_json["action"]["add_role_group"][0])
    choose_users = (method_json["method"][0], user_access_json["invite_users"]["choose_users"][0])
    first_user = (method_json["method"][0], user_access_json["invite_users"]["first_user"][0])
    delete_password = (method_json["method"][0], user_access_json["delete_role"]["input_password"][0])
    add_child_group_reminder = (method_json["method"][0], reminder_json["add_child_group"][0])
    add_role_group_reminder = (method_json["method"][0], reminder_json["add_role_group"][0])
    edit_basic_info_reminder = (method_json["method"][0], reminder_json["edit_basic_info"][0])
    invite_to_group_reminder = (method_json["method"][0], reminder_json["invite_to_group"][0])
    delete_group_reminder = (method_json["method"][0], reminder_json["delete_group"][0])
    delete_role_reminder = (method_json["method"][0], reminder_json["delete_role"][0])
    reminder = (method_json["method"][0], reminder_json["reminder"][0])
    group_number_element = (method_json["method"][0], user_access_json["child_group"]["group_number"][0])
    role_number_element = (method_json["method"][0], user_access_json["role_group"]["role_number"][0])

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

    def click_setting_button(self):
        self.click(*self.setting_button_element)

    def click_group_button(self):
        self.click(*self.group_element)

    def click_user_access(self):
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_user_access_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_user_access_element)

    # 找到当前总共有多少个用户组
    def get_group_number(self):
        self.forced_wait(*self.group_number_element)
        element = self.driver.find_element(*self.group_number_element)
        number = len(element.find_elements(method_json["method"][0], 'nz-tree-node'))
        if number < 1:
            logger.error("这个域列表没有显示!")
            self.get_windows_img()
            raise KeyError('域列表存在异常!')
        else:
            return number

    # 返回用户组的 tree 列表
    def get_group_level(self):
        level = []
        group_number = self.get_group_number()
        if group_number > 1:
            logger.info(f"当前域总共有 {group_number - 1} 个子用户组.")
        for number in range(group_number):
            group_list_element = (method_json["method"][0], f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[1]/div[2]/nz-tree/div[2]/div/div/nz-tree-node[{number + 1}]/nz-tree-indent")
            self.forced_wait(*group_list_element)
            element = self.driver.find_element(*group_list_element)
            # 看“span”属性的个数，如果为0，那么为当前域;如果为1就是子用户组
            level.append(len(element.find_elements(method_json["method"][0], 'span')))
        return level

    def get_role_number(self):
        self.forced_wait(*self.role_number_element)
        element = self.driver.find_element(*self.role_number_element)
        number = len(element.find_elements(method_json["method"][0], 'nz-list-item'))
        if number < 1:
            logger.error("当前用户组没有默认角色组.")
            self.get_windows_img()
            raise KeyError('当前用户组存在异常!')
        else:
            logger.info(f"当前用户组总共有 {number} 个角色组.")
            return number

    def get_role_info(self):
        role_number = self.get_role_number()
        for number in range(role_number):
            element = (method_json["method"][0], f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[2]/div[2]/nz-list/nz-spin/div/div/nz-list-item[{number + 1}]/span")
            self.forced_wait(*element)
            if number == 0:
                logger.info(f"当前用户组第一个默认角色组为：{self.get_element(*element)}.")
            else:
                logger.info(f"当前用户组第 {number + 1} 个角色组为：{self.get_element(*element)}. ")

    # 遍历查看每一个域的信息，看是否ui合格
    def get_group_info(self):
        temp = 0
        level = self.get_group_level()
        if level[0] != 0:
            logger.error("这个用户组列表存在异常!")
            self.get_windows_img()
            return False
        else:
            if len(level) == 1:
                logger.info("当前用户组没有子用户组,且用户组没有问题.")
                self.get_role_info()
                return True
            else:
                for number in range(len(level)):
                    element = (method_json["method"][0], f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[1]/div[2]/nz-tree/div[2]/div/div/nz-tree-node[{number + 1}]/nz-tree-node-title")
                    self.forced_wait(*element)
                    logger.info(f"正在查看 {self.get_element(*element)} 用户组.")
                    # 判断 tree 数组 level 叶节点的值是不是1
                    if number == 0:
                        self.get_role_info()
                    else:
                        if level[number] != 1:
                            logger.error(f"用户组：{self.get_element(*element)} 存在问题!")
                            self.get_windows_img()
                            temp = temp + 1
                            self.click(*element)
                            self.get_role_info()
                        else:
                            logger.info(f"用户组：{self.get_element(*element)} 没有问题.")
                            self.click(*element)
                            self.get_role_info()
        if temp == 0:
            return True
        else:
            return False

    # 得到当前用户组的基本信息修改权限
    def get_group_edit_basic_auth(self):
        group_number = self.get_group_number()
        if group_number == 1:
            self.click(*self.child_group1_element)
            self.click(*self.basic_info)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.edit_basic_info_forbidden))
                logger.info(f"{self.get_element(*self.child_group1_element)} 用户组无修改基础信息权限.")
                return True, group_number
            except Exception:
                logger.error(f"{self.get_element(*self.child_group1_element)} 用户组越权修改权限或按钮未找到.")
                self.get_windows_img()
                return False, group_number
        else:
            self.click(*self.child_group2_element)
            self.click(*self.basic_info)
            # 等待 4 秒防止点击不出弹窗
            self.sleep(4)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.edit_basic_info))
                logger.info(f"{self.get_element(*self.child_group2_element)} 用户组有修改基础信息权限.")
                return True, group_number
            except Exception:
                logger.error(f"{self.get_element(*self.child_group2_element)} 用户组没有修改基础信息权限或按钮未找到.")
                self.get_windows_img()
                return False, group_number

    # 编辑用户基本信息
    def edit_basic_information(self, group_name):
        result = self.get_group_edit_basic_auth()
        if result[0] == True and result[1] == 1:
            return True
        elif result[0] == False and result[1] == 1:
            return False
        else:
            self.click(*self.edit_basic_info)
            self.input(group_name, *self.child_name_input)
            self.click(*self.group_region_code)
            self.actionchains_click(*self.choose_department)
            self.actionchains_click(*self.choose_province)
            self.actionchains_click(*self.choose_city)
            self.actionchains_click(*self.choose_district)
            self.click(*self.confirm_button)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.edit_basic_info_reminder))
                logger.info(f"{reminder}.")
                self.get_windows_img()
                return True
            except Exception:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                    self.click(*self.cancel_button)
                    logger.error(f"{reminder}!")
                    logger.error("修改基础信息失败!")
                    self.get_windows_img()
                except Exception:
                    logger.error(f"未有提示信息 -- {reminder}!")
                    logger.error("修改基础信息失败!")
                    self.get_windows_img()
            return False

    # 权限修改操作
    def modification_permission(self):
        pass

    # 为了得到 users 的数量，找到 body 中 tr 节点数
    def get_page_users_number(self):
        users = (method_json["method"][0], "/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[3]/div[2]/nz-table[2]/nz-spin/div/div/nz-table-inner-default/div/table/tbody")
        self.forced_wait(*users)
        body_element = self.driver.find_element(*users)
        return len(body_element.find_elements(method_json["method"][0], 'tr'))

    def get_user_info(self):
        self.click(*self.child_group1_element)
        self.sleep(2)
        self.click(*self.role_group1_element)
        self.sleep(2)
        self.click(*self.user_management)
        self.sleep(4)
        info_number = 0
        # 做一个循环对当前用户组信息的遍历
        for col1 in range(4):
            account_quota = (method_json["method"][0], f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[3]/div[2]/nz-table[1]/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr[1]/th[{col1 + 1}]")
            account_quota_info = (method_json["method"][0], f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[3]/div[2]/nz-table[1]/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr[2]/td[{col1+ 1}]")
            self.forced_wait(*account_quota)
            logger.info(f"{self.get_element(*account_quota)} : {self.get_element(*account_quota_info)}")
        while True:
            users_number = self.get_page_users_number()
            for number in range(users_number):
                logger.info(f"第 {number + 1 + info_number} 个用户信息如下:")
                for col2 in range(4):
                    user_info = (method_json["method"][0], f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[3]/div[2]/nz-table[2]/nz-spin/div/div/nz-table-inner-default/div/table/thead/tr[1]/th[{col2 + 1}]")
                    users = (method_json["method"][0], f"/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-content/app-custom-group/app-custom-group-manage/section[2]/div/div[3]/div[2]/nz-table[2]/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[{number + 1}]/td[{col2 + 1}]")
                    logger.info(f"{self.get_element(*user_info)}:{self.get_element(*users)}.")
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.last_page))
                break
            except Exception:
                self.click(*self.next_page)
                info_number = info_number + users_number

    def invite_group(self):
        while True:
            self.click(*self.child_group1_element)
            self.sleep(2)
            self.execute_script_click(*self.role_group1_element)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.invite_to_group))
                logger.info(f"出现 {self.get_element(*self.invite_to_group)} 按钮.")
            except Exception:
                logger.error("未出现 邀请用户入组 按钮,权限有问题!")
                self.get_windows_img()
                break
            self.execute_script_click(*self.invite_to_group)
            self.click(*self.choose_users)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.first_user))
            except Exception:
                logger.info("该系统没有可邀请的账号")
                return True
            self.sleep(2)
            self.click(*self.first_user)
            username = self.get_element(*self.first_user)
            self.click(*self.choose_users)
            self.click(*self.confirm_button)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.invite_to_group_reminder))
                logger.info(f"邀请用户：{username} 入组成功.")
                self.get_windows_img()
                return True
            except Exception:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                    self.click(*self.cancel_button)
                    logger.error(f"{reminder}")
                    logger.error("邀请用户入组失败!")
                    self.get_windows_img()
                except Exception:
                    logger.error(f"未有提示信息 -- {reminder}!")
                    logger.error("邀请用户入组失败!")
                    self.get_windows_img()
            break
        return False

    def delete_roles(self, password):
        self.click(*self.child_group1_element)
        self.sleep(5)
        while True:
            self.click(*self.role_group1_element)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cannot_delete_role))
                logger.info("没有删除自己所在的用户组权限.")
            except Exception:
                logger.error("权限出错,或者未出现删除角色组按钮,或者未找到!")
                self.get_windows_img()
                break
            # noinspection PyBroadException
            try:
                # 判断是否有多的角色组
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.role_group2_element))
                logger.info(f"该用户组有可以删除的 {self.get_element(*self.role_group2_element)} 角色组.")
            except Exception:
                logger.warning("该用户组没有可以删除的角色组!")
                self.get_windows_img()
                return True
            self.click(*self.role_group2_element)
            role_name = self.get_element(*self.role_group2_element)
            # noinspection PyBroadException
            try:
                # 判断点击第二个角色组后是否出现 “删除角色组” 按钮
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_role))
                logger.info(f"出现 {self.get_element(*self.delete_role)} 按钮.")
            except Exception:
                logger.error("未出现删除角色组按钮或者未找到!")
                self.get_windows_img()
                break
            self.click(*self.delete_role)
            self.input(password, *self.delete_password)
            self.click(*self.confirm_button)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                # 点击删除后看是否提示删除成功
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_role_reminder))
                logger.info(f"删除 {role_name} 角色组成功.")
                self.get_windows_img()
                return True
            except Exception:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                    self.click(*self.cancel_button)
                    logger.error(f"{reminder}")
                    logger.error(f"删除 {role_name} 角色组失败!")
                    self.get_windows_img()
                except Exception:
                    logger.error(f"{reminder}")
                    logger.error(f"删除 {role_name} 角色组失败!")
                    self.get_windows_img()
            break
        return False

    def delete_groups(self, password):
        while True:
            self.click(*self.child_group1_element)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cannot_delete_group))
                logger.info("没有删除自己所在的用户组权限.")
            except Exception:
                logger.error("权限出错,或者未出现删除子用户组按钮,或者未找到!")
                self.get_windows_img()
                break
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.child_group2_element))
                logger.info(f"该用户有可以删除的 {self.get_element(*self.child_group2_element)} 子用户组.")
            except Exception:
                logger.warning("该用户组没有可以删除的子用户组")
                self.get_windows_img()
                return True
            self.click(*self.child_group2_element)
            group_name = self.get_element(*self.child_group2_element)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_group))
                logger.info(f"出现 {self.get_element(*self.delete_group)} 按钮.")
            except Exception:
                logger.error("未出现删除子用户组按钮或者未找到!")
                self.get_windows_img()
                break
            self.click(*self.delete_group)
            self.input(password, *self.delete_password)
            self.click(*self.confirm_button)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.delete_group_reminder))
                logger.info(f"删除 {group_name} 子用户组成功.")
                self.get_windows_img()
                return True
            except Exception:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                    self.click(*self.cancel_button)
                    logger.error(f"{reminder}")
                    logger.error(f"删除 {group_name} 子用户组失败!")
                    self.get_windows_img()
                except Exception:
                    logger.error(f"{reminder}")
                    logger.error(f"删除 {group_name} 子用户组失败!")
                    self.get_windows_img()
            break
        return False

    def add_group(self, group_name, code):
        while True:
            self.click(*self.child_group1_element)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.add_child_group))
                logger.info("该用户组可以增加子用户组.")
            except Exception:
                logger.error("该用户组不能增加子用户组,权限有问题!")
                self.get_windows_img()
                break
            self.execute_script_click(*self.add_child_group)
            self.input(group_name, *self.child_name_input)
            self.input(code, *self.child_user_group_code)
            self.click(*self.group_region_code)
            self.actionchains_click(*self.choose_department)
            self.actionchains_click(*self.choose_province)
            self.actionchains_click(*self.choose_city)
            self.actionchains_click(*self.choose_district)
            self.click(*self.confirm_button)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.add_child_group_reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.add_child_group_reminder))
                logger.info(f"子用户组添加成功.")
                self.get_windows_img()
                return True
            except Exception:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                    self.click(*self.cancel_button)
                    logger.error(f"{reminder}!")
                    logger.error("子用户组添加失败!")
                    self.get_windows_img()
                except Exception:
                    logger.error(f"{reminder}!")
                    logger.error("子用户组添加失败!")
                    self.get_windows_img()
            break
        return False

    def add_role(self, role_name):
        while True:
            self.click(*self.child_group1_element)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.add_role_group))
                logger.info("该用户组可以增加角色组.")
            except Exception:
                logger.error("该用户组不能增加角色组,权限有问题!")
                self.get_windows_img()
                break
            self.execute_script_click(*self.add_role_group)
            self.input(role_name, *self.child_name_input)
            self.click(*self.confirm_button)
            self.forced_wait(*self.reminder)
            reminder = self.get_element(*self.add_role_group_reminder)
            # noinspection PyBroadException
            try:
                WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.add_role_group_reminder))
                logger.info(f"角色组添加成功.")
                self.get_windows_img()
                return True
            except Exception:
                # noinspection PyBroadException
                try:
                    WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.cancel_button))
                    self.click(*self.cancel_button)
                    logger.error(f"{reminder}!")
                    logger.error("角色组添加失败!")
                    self.get_windows_img()
                except Exception:
                    logger.error(f"{reminder}!")
                    logger.error("角色组添加失败!")
                    self.get_windows_img()
            break
        return False
