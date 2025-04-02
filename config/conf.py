from pathlib import Path
project_root = Path(__file__).parent.parent

# 指定chromedriver.exe路径
CHROME_DRIVER_PATH = project_root / 'utils' / 'chromedriver.exe'

ERP_URL = "http://192.168.150.222:3066"  # 本地环境
LOGIN_SUCCESS_URL = "http://192.168.150.222:3066/dashboard/analysis"

USERNAME = "guomj"  # 主测试账号
PASSWORD = "gmj123.."

# ocr识别
API_KEY = '5mPZWWtbEIcYzeFKmhpQ0Cat'
SECRET_KEY = 'GBd6NyH5oBqXzrZfkyAsKSChKlZEMMTk'