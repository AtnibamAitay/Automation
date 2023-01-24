import xlwt
from bs4 import BeautifulSoup

def generate_excel(html_file_path, excel_file_path):

    # 创建 Excel 表格
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')

    # 设置表头
    worksheet.write(0, 0, 'website_id')
    worksheet.write(0, 1, 'website_type_id')
    worksheet.write(0, 2, 'sort')
    worksheet.write(0, 3, 'website_name')
    worksheet.write(0, 4, 'website_url')
    worksheet.write(0, 5, 'website_intro')
    worksheet.write(0, 6, 'access_requirement')

    # 读取 HTML 文件
    with open(html_file_path, 'r', encoding='UTF-8') as f:
        html_content = f.read()

    # 解析 HTML 内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 定义变量
    row = 1
    current_type = ''
    current_sort = 1

    # 遍历所有 a 标签
    for a_tag in soup.find_all('a'):
        # 获取网址
        website_url = a_tag['href']
        # 获取网站名
        website_name = a_tag.get_text()

        # 判断网站类型
        if a_tag.find_previous('h3'):
            if a_tag.find_previous('h3').get_text() != current_type:
                current_sort = 1
                current_type = a_tag.find_previous('h3').get_text()
            else:
                current_sort += 1

        # 将信息写入表格
        worksheet.write(row, 0, row)
        worksheet.write(row, 1, current_type)
        worksheet.write(row, 2, current_sort)
        worksheet.write(row, 3, website_name)
        worksheet.write(row, 4, website_url)
        worksheet.write(row, 5, '')
        worksheet.write(row, 6, 0)

        row += 1

    # 保存 Excel 表格
    workbook.save(excel_file_path)


# 使用示例
generate_excel('C:/Users\Atnibam Aitay/Downloads/bookmarks_2023_1_24.html', 'websites.xls')
