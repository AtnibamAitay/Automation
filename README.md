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

这种格式的，而人工去修改工作量很大，所以实现了这个程序，扫描指定目录下的所有markdown，统一修改