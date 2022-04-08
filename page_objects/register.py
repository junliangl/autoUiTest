from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class Register_Page(BasePage):
    register_init_button_element = (
        By.XPATH, '/html/body/app-root/app-login/div/form/nz-form-item[4]/nz-form-control/div/div/div/a[contains(text(),"注册新账号")]')
    register_account_element = (By.XPATH, '//*[@id="username"]')
    register_password1_element = (By.XPATH, '//*[@id="password"]')
    register_password2_element = (By.XPATH, '//*[@id="confirmPassword"]')
    register_username_element = (By.XPATH, '//*[@id="actualName"]')
    register_genderMan_element = (By.XPATH, '//*[@id="gender"]/label[1]/span[1]')
    register_genderWomen_element = (By.XPATH, '//*[@id="gender"]/label[2]/span[1]')
    register_phone_number_element = (By.XPATH, '//*[@id="telephone"]')
    register_area1_element = (By.XPATH, '/html/body/app-root/app-register/div/form/nz-form-item[7]/nz-form-control')
    register_area2_element = (By.XPATH, '/html/body/div[2]/div/div/div/ul[1]/li')
    register_area3_element = (By.XPATH, '/html/body/div[2]/div/div/div/ul[2]/li[23]')
    register_area4_element = (By.XPATH, '/html/body/div[2]/div/div/div/ul[3]/li[1]')
    register_area5_element = (By.XPATH, '/html/body/div[2]/div/div/div/ul[4]/li[5]')
    register_company_element = (By.XPATH, '//*[@id="workUnit"]')
    register_enter_button_element = (
        By.XPATH, '/html/body/app-root/app-register/div/form/nz-form-item[9]/nz-form-control/div/div/div/button')

    def input_register_message_account(self, text):
        self.input(text, *self.register_account_element)

    def input_register_message_password(self, text):
        self.input(text, *self.register_password1_element)

    def input_register_message_confirm_password(self, text):
        self.input(text, *self.register_password2_element)

    def input_register_message_username(self, text):
        self.input(text, *self.register_username_element)

    def choose_register_gender(self):
        self.click(*self.register_genderMan_element)

    def input_register_message_phone(self, text):
        self.input(text, *self.register_phone_number_element)

    def choose_area1(self):
        self.click(*self.register_area1_element)

    # chromedriver 的点击方式
    def choose_chrome_area2(self):
        self.actionchains_click(*self.register_area2_element)

    def choose_chrome_area3(self):
        self.actionchains_click(*self.register_area3_element)

    def choose_chrome_area4(self):
        self.actionchains_click(*self.register_area4_element)

    def choose_chrome_area5(self):
        self.actionchains_click(*self.register_area5_element)

    # geckodriver 的点击方式
    def choose_firefox_area2(self):
        self.click(*self.register_area2_element)

    def choose_firefox_area3(self):
        self.click(*self.register_area3_element)

    def choose_firefox_area4(self):
        self.click(*self.register_area4_element)

    def choose_firefox_area5(self):
        self.click(*self.register_area5_element)

    def input_register_message_company(self, text):
        self.input(text, *self.register_company_element)

    def click_init_register_button(self):
        self.click(*self.register_init_button_element)

    def click_register_button(self):
        self.click(*self.register_enter_button_element)

    def get_wait_log(self):
        self.get_wait_element(*self.register_init_button_element)

    def get_result(self):
        result = True
        # noinspection PyBroadException
        try:
            self.driver.find_element(*self.register_enter_button_element)  # 判断是否能找到注册按钮，找不到就视为注册成功
        except Exception:
            result = False
        return result

    def time_sleep(self):
        self.sleep(1.5)
