import os

def rename_note_files_name(path):
    # 定义对应的中文数字和阿拉伯数字字典
    cn_num_dict = {'一': '1', '二': '2', '三': '3', '四': '4', '五': '5', '六': '6', '七': '7', '八': '8', '九': '9'}

    for filename in os.listdir(path):
        # 判断是否是文件
        if os.path.isfile(os.path.join(path, filename)):
            # 判断文件名是否符合要求
            if filename.startswith('第') and '章 ' in filename:
                # 提取中文数字
                cn_num = filename.split('第')[1].split('章')[0]
                # 判断中文数字是否在字典中
                if cn_num in cn_num_dict:
                    # 替换成阿拉伯数字
                    new_filename = filename.replace(cn_num, cn_num_dict[cn_num])
                    #替换空格
                    new_filename = new_filename.replace(" ", "-")
                    # 重命名文件
                    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
                    #输出文件名修改信息
                    print(f"{filename} -> {new_filename}")

# 这里请输入要执行代码的路径，路径需要是包含 \ 反斜杠的
path = r"C:\Users\Atnibam Aitay\Downloads\新建文件夹"
rename_note_files_name(path)