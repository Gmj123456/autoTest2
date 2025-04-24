"""
定义fixture
登录
退出


"""
from selenium import webdriver
from Base.config import CHROME_DRIVER_PATH,ERP_URL,LOGIN_SUCCESS_URL,USERNAME,PASSWORD
from selenium.webdriver.chrome.service import Service
# from PageObject.page_login import PageLogin
from PageObject.page_login2 import LoginPage


service = Service(CHROME_DRIVER_PATH)  # 指定浏览器驱动的路径
driver = webdriver.Chrome(service=service)
driver.get(ERP_URL)  # 打开ERP系统的登录页面
driver.maximize_window()  # 最大化浏览器窗口
driver.implicitly_wait(10)  # 设置隐式等待时间为10秒

login_page = LoginPage(driver)  # 创建登录页面对象
login_page.login(USERNAME, PASSWORD)  # 调用登录方法进行登录操作
driver.get(LOGIN_SUCCESS_URL)  # 打开ERP系统的登录成功页面，用于验证登录是否成功，可根据实际情况修改URL或添加其他验证逻辑。


driver.implicitly_wait(10)  # 设置隐式等待时间为10秒


# 登录操作




# @pytest.fixture(scope="function")
# def login():
#     driver = webdriver.Chrome(service=service)
#     driver.get("http://www.baidu.com")