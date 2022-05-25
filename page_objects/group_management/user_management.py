import os
import json
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'user_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')

with open(json_file, encoding='utf-8') as file1:
    user_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)


class User_Management_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_user_access_element = (method_json["method"][0], menu_json["cd1_setting"]["user_management"][0])
    staging_user_access_element = (method_json["method"][0], menu_json["staging_setting"]["user_management"][0])
    account_quota_available = (method_json["method"][0], user_management_json["account_quota_available"][0])
    account_quota_used = (method_json["method"][0], user_management_json["account_quota_used"][0])
    account_quota_total = (method_json["method"][0], user_management_json["account_quota_total"][0])
    package_expire_time = (method_json["method"][0], user_management_json["package_expire_time"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def get_user_management_info(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_user_access_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_user_access_element)
        self.forced_wait(*self.package_expire_time)
        account_quota_available = int(self.get_element(*self.account_quota_available).replace(',', ''))
        account_quota_used = int(self.get_element(*self.account_quota_used).replace(',', ''))
        account_quota_total = int(self.get_element(*self.account_quota_total).replace(',', ''))
        pack_expire_time = self.get_element(*self.package_expire_time)
        logger.info(f"账号总量是: {account_quota_total}.")
        logger.info(f"可用账号量: {account_quota_available}.")
        logger.info(f"已用账号量: {account_quota_used}")
        logger.info(f"账号包过期时间：{pack_expire_time}")
        if account_quota_total == account_quota_used + account_quota_available:
            logger.info("账号信息没有问题.")
            return True
        else:
            logger.error("账号信息存在问题!")
            return False


