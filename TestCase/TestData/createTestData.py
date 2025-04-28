from faker import Faker
import csv
import logging
from pathlib import Path
import pandas as pd

def generate_test_data(output_file, num_records=100):
    fake = Faker('zh_CN')
    fake.seed_instance(2023)
    fixed_email = "service@jianlian.com"

    # 读取Excel模板数据和下拉选项
    excel_template = Path(__file__).parent / "私有网红模板 (8).xls"
    try:
        # 获取表头
        df = pd.read_excel(excel_template, nrows=0)
        fieldnames = df.columns.tolist()
        
        # 动态生成下拉选项字典（真实场景需要实现数据验证规则解析）
        # 设置默认下拉选项（需用户提供实际选项）
        dropdown_options = {
            '性别': ['男', '女'],
            '签约状态': ['已签约', '未签约', '洽谈中'],
            '内容': ['短视频', '直播', '图文'],  # 新增内容选项
            '标签': ['科技', '时尚', '美食'],    # 新增标签选项
            '类目1': ['美妆', '服饰', '数码', '食品', '家居'],
            '建联邮箱': ['service@jianlian.com']  # 固定邮箱作为唯一选项
        }
        
        # 补充其他类目字段的选项
        for i in range(2,6):
            dropdown_options[f'类目{i}'] = dropdown_options['类目1']
        
        # 示例：真实场景需要从Excel数据验证规则中提取实际选项
        # 这里需要用户提供实际下拉选项或实现自动解析逻辑
        
    except Exception as e:
        logging.error(f"读取模板文件失败: {str(e)}")
        raise

    try:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for _ in range(num_records):
                data = {
                    '账号': fake.bothify(text='???????', letters='abcdefghijklmnopqrstuvwxyz'),  # 生成5-15位纯小写英文
                    '性别': fake.random_element(dropdown_options['性别']),
                    '电话': fake.phone_number(),
                    '邮箱': fake.random_element(dropdown_options.get('邮箱', [fake.email()])),
                    '均播(K)': fake.random_int(1, 1000),
                    '国家': fake.country(),
                    '内容': fake.random_element(dropdown_options['内容']),
                    '标签': fake.random_element(dropdown_options['标签']),
                    '建联邮箱': fake.random_element(dropdown_options['建联邮箱']),
                    '粉丝数(K)': fake.random_int(100, 100000),
                    '签约费用': f"¥{fake.random_int(1000, 1000000):,}",
                    '建联邮箱': fake.random_element([fixed_email]),  # 固定值作为唯一选项
                    '备注': fake.sentence(nb_words=8),
                    **{f'类目{i}': fake.random_element(dropdown_options[f'类目{i}']) 
                      for i in range(1, 6)}
                }
                writer.writerow(data)
                
        logging.info(f"成功生成 {num_records} 条测试数据至: {output_path}")
        
    except Exception as e:
        logging.error(f"数据生成失败: {str(e)}")
        raise

# 新增以下代码用于读取Excel文件头（需要安装pandas和openpyxl）
def get_excel_headers(file_path):
    df = pd.read_excel(file_path, nrows=0)
    return df.columns.tolist()

# 在main函数中添加：
if __name__ == "__main__":
    excel_template = Path(__file__).parent / "私有网红模板 (8).xls"
    if excel_template.exists():
        headers = get_excel_headers(excel_template)
        print("实际Excel文件字段：", headers)
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # 生成测试数据文件（示例路径）
    output_file = Path(__file__).parent / "generated_test_data.csv"
    generate_test_data(output_file)