import pandas as pd
import random
import datetime

# 读取member.xlsx中的内容
members = pd.read_excel('member.xlsx')

# 判断AILabSignInRecord.xlsx是否存在，如果不存在就生成
try:
    sign_in_records = pd.read_excel('AILabSignInRecord.xlsx')
except:
    # 生成表头
    sign_in_records = pd.DataFrame(columns=['签入时间', '名字', '班级', '学号', '任务', '签出时间', '备注'])

# 设置随机生成签到记录的时间段
start_date = datetime.datetime(2023, 2, 18)
# end_date = datetime.datetime(2023, 6, 18)
# 签到记录截止到今天
end_date = datetime.datetime.now()

# 遍历所有成员
for index, member in members.iterrows():
    # 遍历所有日期
    for i in range((end_date - start_date).days + 1):
        # 随机生成是否生成签入记录
        if random.random() < 0.5:
            # 随机生成签入时间
            sign_in_time = start_date + datetime.timedelta(days=i, hours=random.randint(8, 20), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
            # 随机生成签退时间
            sign_out_time = sign_in_time + datetime.timedelta(hours=random.uniform(3.5, 4))
            # 确保签退时间在当日晚上11点之前
            while sign_out_time.time() > datetime.time(23, 0, 0):
                sign_out_time = sign_in_time.replace(hour=random.randint(22, 23), minute=random.randint(0, 59), second=random.randint(0, 59))
            sign_out_time = datetime.datetime.combine(sign_out_time.date(), sign_out_time.time())
            # 生成数据并插入到表格最后
            sign_in_records = pd.concat([sign_in_records, pd.DataFrame({
                '签入时间': sign_in_time,
                '名字': member['名字'],
                '班级':member['班级'],
                '学号': member['学号'],
                '任务': '项目开发',
                '签出时间': sign_out_time,
                '备注': ''
                }, index=[0])])
            # 保存签到记录表格
            sign_in_records = sign_in_records.sort_values(by='签入时间')
            sign_in_records.to_excel('AILabSignInRecord.xlsx', index=False)