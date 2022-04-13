# coding=utf-8
import time
import os.path
from selenium.webdriver import ActionChains
from framework.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a logger instance
logger = Logger(logger="测试流程").get_log()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        """
        打开浏览器
        """
        # noinspection PyBroadException
        try:
            self.driver.get()
            logger.info("打开浏览器成功.")
        except Exception:
            logger.error("打开浏览器失败.")

    def get_windows_img(self):
        """
        浏览器截图操作
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./screenshots下
        """
        try:
            file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshots')
            rq = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
            screen_name = os.path.join(file_path, rq + '.png')
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(f"已经成功截图并保存在 : {screen_name}")
        except NameError as e:
            logger.warning(f"截图失败： {e}.")

    def quit_browser(self):
        """
        浏览器退出操作
        """
        # noinspection PyBroadException
        try:
            self.driver.quit()
            logger.info("Click quit on current page.")
        except Exception:
            logger.warning("网页无法退出.")
            self.get_windows_img()

    def forward(self):
        """
        浏览器前进操作
        """
        # noinspection PyBroadException
        try:
            self.driver.forward()
            logger.info("Click forward on current page.")
        except Exception:
            logger.error("网页无法向前翻页.")
            self.get_windows_img()

    def back(self):
        """
        浏览器后退操作
        """
        # noinspection PyBroadException
        try:
            self.driver.back()
            logger.info("成功向后翻页浏览器.")
        except Exception:
            logger.error("网页无法向后翻页.")
            self.get_windows_img()

    def close(self):
        """
        点击关闭当前窗口
        """
        try:
            self.driver.close()
            logger.info("成功关闭当前窗口.")
        except Exception as e:
            logger.error(f"退出浏览器失败 {e}.")

    def implicit_wait(self, seconds):
        """
        隐式等待
        """
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(seconds)
            logger.info(f"隐式等待 {seconds} 秒.")
        except Exception:
            logger.warning("隐式等待失败.")
            self.get_windows_img()

    def forced_wait(self, *selector):
        """
        显式等待,进行操作之前都需要显式等待一下
        """
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(selector))
            logger.info('显式等待元素成功.')
        except Exception:
            logger.warning('显式等待元素失败.')

    def find_element(self, *selector):
        """
        定位元素方法
        传入元组
        传入的时候定义好定位的方式和元素
        """
        # noinspection PyBroadException
        try:
            # self.forced_wait(*selector)
            element = self.driver.find_element(*selector)
            logger.info(f"成功找到元素：{selector}")
            return element
        except Exception:
            logger.error(f"找不到元素: {self.get_element(*selector)}")
            self.get_windows_img()

    def get_element(self, *selector):
        """
        输入
        """
        try:
            element = self.driver.find_element(*selector)
            return element.text
        except Exception as e:
            logger.error(f"找不到元素: {e}")
            self.get_windows_img()

    def input(self, text, *selector):
        """
        输入框输入信息
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            element.clear()
            element.send_keys(text)
            logger.info(f"输入 {text} 成功")
        except Exception as e:
            logger.error(f"输入框输入 {e} 失败")
            self.get_windows_img()

    def clear(self, *selector):
        """
        清除文本框
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            element.clear()
            logger.info("清除了输入框.")
        except Exception as e:
            logger.warning(f"清除输入框 {e} 失败")
            self.get_windows_img()

    def click(self, *selector):
        """
        点击元素
        """
        self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            element = self.driver.find_element(*selector)
            element_name = self.get_element(*selector)
            element.click()
            logger.info(f"按钮 {element_name} 已被点击.")
        except Exception as e:
            logger.error(f"点击按钮 {e} 失败")
            self.get_windows_img()

    def actionchains_click(self, *selector):
        """
        移动鼠标点击
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            element_name = self.get_element(*selector)
            ActionChains(self.driver).move_to_element(element).click(element).perform()
            logger.info(f"按钮 {element_name} 已被点击.")
        except Exception as e:
            logger.error(f"点击按钮 {e} 失败")
            self.get_windows_img()

    def get_page_title(self):
        """
        获取网页标题
        """
        # noinspection PyBroadException
        try:
            logger.info(f"Current page title is {self.driver.title}")
            return self.driver.title
        except Exception:
            logger.warning("获取页面title失败.")
            self.get_windows_img()

    def get_wait_element(self, *selector):
        """
        找到显示等待的元素
        """
        self.forced_wait(*selector)
        # noinspection PyBroadException
        try:
            logger.info(f"找到 {self.get_element(*selector)} 按钮")
        except Exception:
            logger.error('找不到显式等待的元素')
            self.get_windows_img()

    def refresh_browser(self):
        self.driver.navigate().refresh()
        self.sleep(1)

    @staticmethod
    def sleep(seconds):
        """
        强制等待的提醒
        """
        time.sleep(seconds)
        logger.info(f"强制等待了 {} 秒")
