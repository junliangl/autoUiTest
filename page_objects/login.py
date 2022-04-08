from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page(BasePage):
    input_username_element = (
        By.XPATH, '/html/body/app-root/app-login/div/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input')
    input_password_element = (
        By.XPATH, '/html/body/app-root/app-login/div/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input')
    login_button_element = (
        By.XPATH, '/html/body/app-root/app-login/div/form/nz-form-item[3]/nz-form-control/div/div/button')
    username_element = (By.XPATH, '/html/body/app-root/app-shell/div/nz-layout/nz-layout/nz-header/div/div[2]/div[2]')

    def input_login_message_account(self, text):
        self.input(text, *self.input_username_element)

    def input_login_message_password(self, text):
        self.input(text, *self.input_password_element)

    def time_sleep(self):
        self.sleep(1)

    def click_login_button(self):
        self.click(*self.login_button_element)
        self.time_sleep()

    # 判断是否能找到某一元素，找不到就视为注册成功
    def get_result(self):
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.username_element))
            return True
        except Exception:
            return False

    def get_wait_log(self):
        self.get_wait_element(*self.login_button_element)
