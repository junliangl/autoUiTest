# -*- coding:utf-8 -*-
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome import service
from framework.logger import Logger
from framework.browser_info import Browser_Info
logger = Logger(logger="浏览器初始化配置").get_log()
get_browser_info = Browser_Info()


class BrowserEngine:
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    windows_geckodriver_driver_path = os.path.join(os.path.join(dir, 'tools'), 'geckodriver.exe')
    windows_chrome_driver_path = os.path.join(os.path.join(dir, 'tools'), 'chromedriver.exe')
    windows_ie_driver_path = os.path.join(os.path.join(dir, 'tools'), 'IEDriverServer.exe')
    linux_chrome_driver_path = os.path.join(os.path.join(dir, 'tools'), 'chromedriver')

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
                driver = webdriver.Chrome(executable_path=self.linux_chrome_driver_path, options=options)# 给Chrome()指定驱动路径
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
