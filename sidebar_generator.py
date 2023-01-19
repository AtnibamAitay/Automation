import os
import re

def generate_sidebar(path):
    # 判断是否已存在 _sidebar.md 文件
    if os.path.exists(os.path.join(path, "_sidebar.md")):
        print("_sidebar.md 已经存在，程序退出。")
        return
    # 获取文件夹中所有文件名
    file_names = [file.name for file in os.scandir(path) if file.is_file() and file.name.endswith('.md')]
    # 按照章节顺序进行排序
    file_names = sorted(file_names, key=lambda x: int(re.search('(?<=第)\d+(?=章)', x).group(0)) if x.startswith("第") else float('inf'))
    # 将 readme 文件放到第一位
    if 'README.md' in file_names:
        file_names.remove('README.md')
        file_names.insert(0, 'README.md')
    # 构造文档内容
    content = ""
    for file in file_names:
        file_name = file.replace(".md", "")
        content += f"* [{file_name}](/Document/Programming/Python/BasicGrammar/{file})\n"
    # 在指定路径下生成 _sidebar.md 文档
    with open(os.path.join(path, "_sidebar.md"), "w") as f:
        f.write(content)

# 示例用法
path = r"A:\始于不足见，终于不可及\学习\编程\3.Python\1.基础语法"
generate_sidebar(path)