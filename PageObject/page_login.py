from Base.base_page import BasePage
from Base.utils.ocr import BaiduOCR
from Base.config import API_KEY, SECRET_KEY
import os

class PageLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # 调用父类的初始化方法，传入driver对象
        self.ocr_client = BaiduOCR(API_KEY, SECRET_KEY)  # 初始化BaiduOCR对象，传入API_KEY和SECRET_KEY
    # 定位器
    username_input = ("css selector", "input[placeholder='请输入用户名']")
    password_input = ("css selector", "input[placeholder='请输入密码']")
    code_image = ("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/form/div[1]/form/div[3]/div[2]/img")
    code_input = ("css selector", "input[placeholder='请输入验证码']")
    login_button = ("css selector", "button.login-button")

    # 输入用户名
    def input_username(self, username):
        self.input(self.username_input, username)

    # 输入密码
    def input_password(self, password):
        self.input(self.password_input, password)

    # 验证码截图保存
    def get_code_image(self):
        import os
        # 获取项目根目录路径
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # 构建相对路径
        code_path = os.path.join(project_root, "Base", "utils", "code_image.png")
        # 确保目录存在
        os.makedirs(os.path.dirname(code_path), exist_ok=True)
        # 调用截图方法
        self.save_element_screenshot(self.code_image, code_path)
        return code_path  # 新增返回值
    # 调用工具识别验证码
    def get_code(self):
        # 使用动态生成的路径（需要从get_code_image方法获取）
        code_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Base", "utils", "code_image.png")
        code = self.ocr_client.ocr_accurate_basic(code_path)
        return code
    # 输入验证码
    def input_code(self, code):
        self.input(self.code_input, code)

    # 点击登录按钮
    def click_login_button(self):
        self.click(self.login_button)

    # 登录业务流程
    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.get_code_image()  # 截图验证码
        code = self.get_code() # 识别验证码
        self.input_code(code) 
        self.click_login_button()
    