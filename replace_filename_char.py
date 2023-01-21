import os

def replace_filename_char(path, old_char, new_char):
    path = os.path.normpath(path) # 转换路径为标准格式
    for root, dirs, files in os.walk(path):
        for file in files:
            if old_char in file:
                old_name = os.path.join(root, file)
                new_name = os.path.join(root, file.replace(old_char, new_char))
                os.rename(old_name, new_name)
                print("{} -> {}".format(old_name, new_name))
            else:
                print("{} 中无匹配字符，跳过。".format(file))


replace_filename_char(r"路径\路径", "文件名中需要被替换的字符", "替换后的字符")