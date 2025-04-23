"""
定义fixture
登录
退出


"""
from selenium import webdriver
from config.conf import CHROME_DRIVER_PATH
from selenium.webdriver.chrome.service import Service

service = Service(CHROME_DRIVER_PATH)  # 指定浏览器驱动的路径

driver = webdriver.Chrome(service=service)
driver.get("http://www.baidu.com")

#
# @pytest.fixture(scope="function")
# def login():
#     driver = webdriver.Chrome(service=service)
#     driver.get("http://www.baidu.com")