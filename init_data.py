import os
import json

def ensure_data_directory():
    """确保data目录存在"""
    if not os.path.exists('data'):
        os.makedirs('data')
        print("创建data目录")

def init_data_files():
    """初始化数据文件"""
    # 确保data目录存在
    ensure_data_directory()
    
    # 检查articles.json是否存在
    if not os.path.exists('data/articles.json'):
        # 创建一个空的文章列表
        with open('data/articles.json', 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        print("创建articles.json文件")
    
    # 检查translations.json是否存在
    if not os.path.exists('data/translations.json'):
        # 创建一个空的翻译词典
        with open('data/translations.json', 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        print("创建translations.json文件")

if __name__ == '__main__':
    init_data_files()
    print("数据目录和文件初始化完成！") 