import os

from find_and_modify_readme import find_and_modify_readme
from markdown_img_code_modifier import markdown_img_code_modifier

# 目录扫描器

def print_directory_contents(path):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print(child_path)

            # TODO:需要什么自动化脚本，在这里调用即可，请注意脚本的使用规则
            # find_and_modify_readme(child_path)
            # markdown_img_code_modifier(child_path)

            print_directory_contents(child_path)

# 这里请输入要执行脚本的最高级路径，路径需要是包含 \ 反斜杠的
path = r"路径"
print_directory_contents(path)