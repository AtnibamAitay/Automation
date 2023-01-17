import os
import re

path = "路径/路径"

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            print(file)
            with open(file_path, "r", encoding='utf-8') as f:
                content = f.read()
                new_content = re.sub(r'<img src="(.*?)" (.*?) style="zoom: (.*?);" />', r'![image](\1)', content)
                for match in re.finditer(r'<img src="(.*?)" (.*?) style="zoom: (.*?);" />', content):
                    before = match.group()
                    after = re.sub(r'<img src="(.*?)" (.*?) style="zoom: (.*?);" />', r'![image](\1)', before)
                    print(f'{before} -> {after}')
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(new_content)
            print()