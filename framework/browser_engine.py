# -*- coding:utf-8 -*-
import os
import json
import platform
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.browser_info import Browser_Info

logger = Logger(logger="浏览器初始化配置").get_log()
get_browser_info = Browser_Info()

login_type = None
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file = os.path.join(os.path.join(project_path, 'config'), 'login.json')

with open(json_file, encoding='utf-8') as file1:
    login_type_json = json.load(file1)


class BrowserEngine:
    login_type_element = ('xpath', login_type_json["account"][0])  # 非天津私有化类型
    windows_geckodriver_driver_path = os.path.join(os.path.join(project_path, 'tools'), 'geckodriver.exe')
    windows_chrome_driver_path = os.path.join(os.path.join(project_path, 'tools'), 'chromedriver.exe')
    windows_ie_driver_path = os.path.join(os.path.join(project_path, 'tools'), 'IEDriverServer.exe')
    linux_chrome_driver_path = os.path.join(os.path.join(project_path, 'tools'), 'chromedriver')

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        # 获取配置文件属性
        logger.info(f"You had select {get_browser_info.get_driver()} browser.")
        logger.info(f"The test server url is: {get_browser_info.get_url()}")

        if platform.system() == 'Linux':
            if get_browser_info.get_driver() == "Chrome":
                options = webdriver.chrome.options.Options()
                options.add_argument('--headless')  # 使用无头模式执行
                options.add_argument('--disable-gpu')
                options.add_argument('--disable-extensions')
                options.add_argument('--no-sandbox')
                driver = webdriver.Chrome(executable_path=self.linux_chrome_driver_path,
                                          options=options)  # 给Chrome()指定驱动路径
                logger.info("Starting Chrome browser.")
            elif get_browser_info.get_driver() == "Firefox":
                options = webdriver.firefox.options.Options()
                options.add_argument('--headless')  # 使用无头模式执行
                options.add_argument('--disable-gpu')
                options.add_argument('disable-extensions')
                options.add_argument('--no-sandbox')
                driver = webdriver.Firefox(executable_path=self.windows_geckodriver_driver_path)
                logger.info("Starting firefox browser.")
            elif get_browser_info.get_driver() == "IE":
                options = webdriver.firefox.options.Options()
                options.add_argument('--headless')  # 使用无头模式执行
                options.add_argument('--disable-gpu')
                options.add_argument('disable-extensions')
                options.add_argument('--no-sandbox')
                driver = webdriver.Ie(executable_path=self.windows_ie_driver_path)
                logger.info("Starting IE browser.")
        elif platform.system() == 'Windows':
            if get_browser_info.get_driver() == "Chrome":
                options = webdriver.chrome.options.Options()
                options.add_argument('--headless')  # 使用无头模式执行
                options.add_argument('--disable-gpu')
                options.add_argument('--disable-extensions')
                options.add_argument('--no-sandbox')
                driver = webdriver.Chrome(executable_path=self.windows_chrome_driver_path, options=options)
                logger.info("Starting Chrome browser.")
            elif get_browser_info.get_driver() == "Firefox":
                options = webdriver.firefox.options.Options()
                options.add_argument('--headless')  # 使用无头模式执行
                options.add_argument('--disable-gpu')
                options.add_argument('disable-extensions')
                options.add_argument('--no-sandbox')
                driver = webdriver.Firefox(executable_path=self.windows_geckodriver_driver_path)
                logger.info("Starting firefox browser.")
            elif get_browser_info.get_driver() == "IE":
                options = webdriver.firefox.options.Options()
                options.add_argument('--headless')  # 使用无头模式执行
                options.add_argument('--disable-gpu')
                options.add_argument('disable-extensions')
                options.add_argument('--no-sandbox')
                driver = webdriver.Ie(executable_path=self.windows_geckodriver_driver_path)
                logger.info("Starting IE browser.")
        driver.get(get_browser_info.get_url())
        logger.info(f"Open url: {get_browser_info.get_url()}.")
        driver.maximize_window()
        logger.info("Maximize the current window.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()

    def look_login_type(self):
        global login_type
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.login_type_element))
            login_type = True
        except Exception:
            login_type = False

    @staticmethod
    def get_login_type():
        return login_type
