# 一、automation
这里放一些，使用python实现的自动化代码

# 二、使用须知

## 2.1 AILabRandomGenerateSignInRecords.py
### 2.1.1 作用及实现规则
这个代码实现了一个根据下面的规则，自动生成签到记录表的功能：

1、时间范围为：20xx年x月x日-20xx年x月x日，换句话讲是从开学到期末

2、签到时间必须在早上八点到晚上八点

3、签退时间必须在中午十一点到晚上十一点之间

4、每个人每天至少最多有一条签到记录，也可以没有

5、签到时间随机生成后，再在3.5到4小时之间随机取一个时间点作为签退时间

### 2.1.2 使用方法
需要在和代码相同目录下，放一份表格，包括“名字、学号、班级”

## 2.2 AutomaticallyRegisterForVPNAndGetClash.py
### 2.2.1 作用及实现规则
这个代码实现了自动注册一个VPN账号，并自动登陆，获取3天免费套餐，然后自动返回一个clash url链接的功能

### 2.2.2 使用方法
直接运行，见控制台输出

### 2.2.3 报错解决办法

安装 lxml 库，可以通过以下命令来安装：

```
pip install lxml
```

或者

```
pip3 install lxml
```

## 2.3 SidebarGenerator.py
_sidebar.md 自动生成器
### 2.3.1 作用及实现规则
读取指定路径下的所有文件名，不包括文件名的后缀，并在该路径下生成一份markdown文档，文档名为_sidebar.md。

其中所读取的文件名，除了readme，其他文件名是有规律的，一般为开头为“第x章-”，其中x是阿拉伯数字，生成器会根据阿拉伯数字进行排序，如果文件名不符合"第x章"的格式，则会被排在最后，然后再按排序，生成文档_sidebar.md的内容，文档内容为：

```markdown
* [文件名1](/Document/BasisOfComputerEngineering/DataStructure/文件名1.md)
* [文件名2](/Document/BasisOfComputerEngineering/DataStructure/文件名2.md)
* [文件名3](/Document/BasisOfComputerEngineering/DataStructure/文件名3.md)
```

以此类推，如果存在文件名为readme的文件，那么文件名1一定为readme，之后的文件名按照读取排序
在生成_sidebar.md前，先判断文件路径下是否存在_sidebar.md，若已存在，则结束程序

### 2.3.2 使用方法
调用generate_sidebar("路径/路径")方法，传入需要生成 _sidebar.md 的目录。
目录下文件名命名规则：”readme.md“、以及“第x章-笔记章节标题”

## 2.4 MarkdownImageCodeModifier.py
Markdown 图片代码修改器
### 2.4.1 作用及实现规则
由于 docsify 无法识别图片

```markdown
<img src="图表/v2-530c9d4478398718c15632b9aa025c36_r.jpg" alt="preview" style="zoom: 67%;" />
```

这种格式的代码，只能识别

```markdown
![image](图表/v2-530c9d4478398718c15632b9aa025c36_r.jpg)
```

这种格式的，而人工去修改工作量很大，所以实现了这个程序，扫描指定目录下的所有 markdown，统一修改

## 2.5 scan_directory.py
目录扫描器

### 2.5.1 作用及实现规则

可以扫描指定目录下的所有目录，可以配合其他自动化脚本使用，自动化完成大量重复工作。

### 2.5.2 注意

自动化脚本执行的目录，不包括传入的路径本身，只在传入的目录下面的所有子目录执行

## 2.6 find_and_modify_readme

这个脚本纯粹是因为我的强迫症，我希望所有笔记的 README.md，全部统一大写，包括里面的内容和同目录下的 _sidebar.md 中的内容

### 2.6.1 作用及实现规则

这段代码的主要作用是在给定路径中查找 "readme.md" 或 "README.md" 文件，如果找到 "readme.md" 文件，则将其重命名为 "README.md"，并对其内容进行替换，将 "readme" 或者 "Readme" 替换为 "README"。如果找不到 "readme.md" 或 "README.md" 文件，则输出提示信息。最后，它还会检查是否有 "_sidebar.md" 文件，如果有，则对其内容进行相同的替换。

## 2.7 rename_note_files_name.py

### 2.7.1 作用及实现规则

扫描指定目录下的文件，对于文件名中含有 "第" 和 "章 "（注意有空格）的文件进行处理，将中文数字替换成阿拉伯数字，并将文件名中的空格替换成 "-",最后重命名文件，并在控制台显示文件名修改信息。

### 2.7.2 示例

第一章 内容.md -> 第1章-内容.md

第二章 内容.md -> 第2章-内容.md

## 2.8 rename_md_images_path.py

### 2.8.1 作用及实现规则

扫描指定目录下的所有后缀为.md文档的内容，将

```markdown
![图片名](图表 /图片名)
```

中的“图表”，替换为“images”。并将同目录下名字为“图表”的文件夹名字换成“images”。
该程序会在替换操作后在控制台输出被修改的文件、修改的地方和替换的次数。

## 2.9 analysis_html_generate_excel.py
这个代码纯粹是我不想手动去做一些体力劳动而写的一次性代码。
### 2.8.1 作用及实现规则

将一个html中的内容按照规则录入一份excel表格中。具体来说，该脚本会读取指定路径下的html文件，然后使用 BeautifulSoup 库解析其中的内容，每获取一个 <a> 标签，就将其 href 属性和内容录入表中。

该脚本会创建一个名为"websites.xls"的Excel文件，表头为：网站id，网站类型id，排序，网站名，网址、简介、访问要求，其中网站id和排序按照录入顺序依次递增，访问要求均为0，简介为空。

## 2.10 batch_download_bilibili_favorites.py

### 2.8.1 作用及实现规则

这段代码的主要作用是批量下载Bilibili用户的收藏夹中的视频。它实现了以下逻辑：

首先通过请求Bilibili API获取用户的所有收藏夹信息，并统计所有视频的总数。

在本地创建一个名为"run.bat"的文件，并在里面写入预处理代码，检查本地是否已安装you-get。

循环遍历所有收藏夹，并对于每个收藏夹，在"run.bat"文件中写入以下代码：

a. 首先检查是否是第一次写入mkdir，如果不是则在其上面加入“cd..”，返回上一层文件夹

b. 创建一个文件夹，名称为该收藏夹的名称

c. 切换到该文件夹中

d. 循环遍历该收藏夹中的所有视频

e. 为每个视频写入一条you-get命令，将该视频下载到当前文件夹中。

所有收藏夹和视频遍历完成后，运行该"run.bat"文件，即可开始批量下载视频。