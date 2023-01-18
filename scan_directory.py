import os
from markdown_img_code_modifier import markdown_img_code_modifier

# 目录扫描器

def print_directory_contents(path):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print(child_path)
            markdown_img_code_modifier(child_path)
            print_directory_contents(child_path)

# print_directory_contents("A:/始于不足见，终于不可及/学习/编程/13.计算机通识/数据结构/2.Java")