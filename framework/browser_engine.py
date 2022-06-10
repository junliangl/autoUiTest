# -*- coding:utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from framework.logger import Logger
from framework.browser_info import Browser_Info

logger = Logger(logger="浏览器初始化配置").get_log()
get_browser_info = Browser_Info()


class BrowserEngine:
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    geckodriver_driver_path = os.path.join(os.path.join(dir, 'tools'), 'geckodriver.exe')
    chrome_driver_path = os.path.join(os.path.join(dir, 'tools'), 'chromedriver.exe')
    ie_driver_path = os.path.join(os.path.join(dir, 'tools'), 'IEDriverServer.exe')

    def __init__(self, driver):
        self.driver = driver

        # 从 browser_message 里面拿到数据

    def open_browser(self, driver):
        # 获取配置文件属性
        logger.info(f"You had select {get_browser_info.get_driver()} browser.")
        logger.info(f"The test server url is: {get_browser_info.get_url()}")

        if get_browser_info.get_driver() == "Firefox":
            s = Service(self.geckodriver_driver_path)  # 给Firefox()指定驱动路径
            driver = webdriver.Firefox(service=s)
            logger.info("Starting firefox browser.")
        elif get_browser_info.get_driver() == "Chrome":
            s = Service(self.chrome_driver_path)  # 给Chrome()指定驱动路径
            driver = webdriver.Chrome(service=s)
            logger.info("Starting Chrome browser.")
        elif get_browser_info.get_driver() == "IE":
            s = Service(self.geckodriver_driver_path)
            driver = webdriver.Ie(service=s)
            logger.info("Starting IE browser.")
        driver.get(get_browser_info.get_url())
        logger.info(f"Open url: {get_browser_info.get_url()}.")
        driver.maximize_window()
        logger.info("Maximize the current window.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
