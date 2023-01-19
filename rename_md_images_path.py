import os
import re

def rename_md_images_path(path):
    # 判断 "图表" 文件夹是否存在
    image_folder = os.path.join(path, '图表')
    if not os.path.exists(image_folder):
        print("图表文件夹不存在，结束程序")
        return
    # 遍历文件夹
    for root, dirs, files in os.walk(path):
        # 遍历子文件夹
        for dir in dirs:
            # 如果文件夹名字是“图表”
            if dir == "图表":
                # 新文件夹名字
                new_path = os.path.join(root, "images")
                # 如果新文件夹名字不存在
                if not os.path.exists(new_path):
                    # 更改文件夹名字
                    os.rename(os.path.join(root, dir), new_path)
        # 遍历文件
        for file in files:
            # 如果是.md文件
            if file.endswith(".md"):
                # 文件路径
                file_path = os.path.join(root, file)
                # 以读的方式打开文件
                with open(file_path, "r", encoding="utf-8") as f:
                    # 读取文件内容
                    content = f.read()
                    # 替换文件内容
                    new_content, number_of_subs_made = re.subn(r"!\[(.*)\]\(图表/(.*?)\)", lambda m: f"![{m.group(1)}](images/{m.group(2)})", content)
                    # 如果替换了
                    if number_of_subs_made>0:
                        # 输出文件名
                        print(f"{file}")
                        # 输出被修改前后的字符串
                        print(f"{content} -> {new_content}")
                        # 输出被替换的次数
                        print(f"{number_of_subs_made} substitution(s) made.")
                        # 以写的方式打开文件
                        with open(file_path, "w", encoding="utf-8") as f:
                            # 写入新的文件内容
                            f.write(new_content)


path = r"C:\Users\Atnibam Aitay\Downloads\新建文件夹"
rename_md_images_path(path)
