from Base.base_page import BasePage

class PageLogin(BasePage):
    # 定位器
    username_input = ("id", "username")
    password_input = ("id", "password")
    code_input = ("id", "code")
    login_button = ("id", "loginBtn")

    # 输入用户名
    def input_username(self, username):
        self.input(self.username_input, username)

    # 输入密码
    def input_password(self, password):
        self.input(self.password_input, password)

    # 输入验证码
    def input_code(self, code):
        self.input(self.code_input, code)

    # 点击登录按钮
    def click_login(self):
        self.click(self.login_button)

    # 登录业务流程
    def login(self, username, password,code):
        self.input_username(username)
        self.input_password(password)
        self.input_code(code) 
        self.click_login()
    