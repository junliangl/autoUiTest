import os
from configparser import ConfigParser

dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = ConfigParser()
file_path = os.path.join(os.path.join(dir_name, 'config'), 'config.ini')
config.read(file_path)


# 得到配置里的 driver_name 和 url
class Message:
    def __init__(self):
        self.browser = config.get("browserType", "browserName")
        self.url = config.get("testServer", "URL")

    def get_driver(self):
        return self.browser

    def get_url(self):
        return self.url
