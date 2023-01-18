import os

def find_and_modify_readme(path):
    readme_file = os.path.join(path, 'readme.md')
    if os.path.exists(readme_file):
        # 重命名为README.md
        os.rename(readme_file, os.path.join(path, 'README.md'))
        readme_file = os.path.join(path, 'README.md')
        print(f"{readme_file} -> {os.path.join(path, 'README.md')}")
    else:
        readme_file = os.path.join(path, 'README.md')
        if not os.path.exists(readme_file):
            print("在指定目录中未找到readme.md或README.md文件。")
            return

    # 打开 README.md 文件并读取其内容
    with open(readme_file, 'r', encoding='utf-8') as f:
        readme_contents = f.read()
    original_readme = readme_contents
    # 替换 readme 为 README
    readme_contents = readme_contents.replace("readme", "README")
    readme_contents = readme_contents.replace("Readme", "README")
    if original_readme != readme_contents:
        print(f"{'readme'} -> {'README'}")
        print(f"{'Readme'} -> {'README'}")

    # 将修改后的内容写回文件
    if original_readme != readme_contents:
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_contents)

    # Check for _sidebar.md
    sidebar_file = os.path.join(path, '_sidebar.md')
    sidebar_contents = ""
    if os.path.exists(sidebar_file):
        with open(sidebar_file, 'r', encoding='utf-8') as f:
            sidebar_contents = f.read()
    original_sidebar = sidebar_contents
    sidebar_contents = sidebar_contents.replace("readme", "README")
    sidebar_contents = sidebar_contents.replace("Readme", "README")
    if original_sidebar != sidebar_contents:
        print("该目录下的 _sidebar.md 中的 readme 或者 Readme 被修改为了 README。")

    if original_sidebar != sidebar_contents:
        with open(sidebar_file, 'w', encoding='utf-8') as f:
            f.write(sidebar_contents)