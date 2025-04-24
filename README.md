# 自动化测试框架

基于Python + Selenium + Page Object模式实现的ERP系统自动化测试框架

## 功能特性
✅ ERP系统登录/登出测试  
✅ 销售计划模块基础操作测试  
✅ 验证码自动识别（集成百度OCR API）  
✅ 页面元素智能等待机制  
✅ 多环境配置支持（本地/测试环境）

## 技术栈
- **语言**: Python 3.12
- **核心框架**: Selenium 4.8
- **模式**: Page Object Model
- **OCR服务**: 百度文字识别API
- **日志系统**: logging模块
- **配置管理**: config.py

## 项目结构
```bash
.
├── Base                 # 基础组件
│   ├── base_page.py     # 页面基类
│   ├── config.py        # 环境配置
│   └── utils/           # 工具类
├── PageObject           # 页面对象
│   ├── page_login.py    # 登录页面V1
│   ├── page_login2.py   # 登录页面V2（增强版）
│   └── page_salesplan.py # 销售计划页面
├── TestCase             # 测试用例
│   ├── conftest.py      # pytest配置
│   └── test_login.py    # 登录测试用例
└── README.md            # 本文档
```