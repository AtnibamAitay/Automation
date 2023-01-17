import json
import time
import requests
from bs4 import BeautifulSoup
import re

# 如果地址失效，请发送邮件到 fastlink.ws@email.com 获取最新不用翻墙的域名
vpn_url = 'http://www.fastlink.pro'
# 备用
# vpn_url = 'http://www.fastlink.so'

# 注册请求的url
registration_request_url = vpn_url + '/auth/register'

# 使用时间戳创建email和name
timestamp = str(int(time.time()))
email = timestamp + "@qq.com"
username = email

# 使用时间戳创建passwd和repasswd
password = timestamp
repassword = password
register_code = "clashw"

# 组装发送的json数据
registration_data = {
    "email": email,
    "username": username,
    "passwd": password,
    "repasswd": repassword,
    "code": register_code
}

# 打印发送的json数据
print("发送的json数据:")
print(json.dumps(registration_data, ensure_ascii=False))

# 发送post请求
response = requests.post(registration_request_url, json=registration_data)

# 打印接收到的json数据
print("接收到的json数据:")
print(json.dumps(response.json(), ensure_ascii=False))

# 判断是否注册成功
if response.status_code == 200 and response.json()["ret"] == 1:
    print("注册成功！")
else:
    print("注册失败！")

# 登录请求的url
login_request_url = vpn_url + '/auth/login'

# 组装登录数据
login_data = {
    "email": email,
    "passwd": password
}

# 发送登录请求
login_response = requests.post(login_request_url, json=login_data)

# 打印登录结果
print("登录结果:" + json.dumps(login_response.json(), ensure_ascii=False))

# 获取cookies
cookies = login_response.cookies

# 访问需要登录后才能访问的页面
shop_page_url = vpn_url + '/user/shop'
response = requests.get(shop_page_url, cookies=cookies)

#使用beautifulsoup解析页面
soup = BeautifulSoup(response.text, 'lxml')

#执行相应的操作
subscribe_plan = soup.select_one('.pricing-cta')
if subscribe_plan:
    subscribe_plan.attrs['onclick'] = "subscribePlan('plan_5');"
else:
    print("3天体验套餐的按钮不存在")

coupon_button = soup.select_one('#coupon-btn')
if coupon_button:
    coupon_button.attrs['onclick'] = "couponBtn.click();"
else:
    print("coupon_btn not found")

coupon_code_input = soup.select_one('#coupon-code')
coupon_code_input.attrs['value'] = "599_f3cZ8bzm"

# 使用 BeautifulSoup 查找到类名为 modal-footer, bg-whitesmoke 的元素
update_coupon = soup.select_one('.modal-footer.bg-whitesmoke')
if update_coupon:
    # 查找到按钮
    update_coupon = update_coupon.find('button', class_='btn btn-primary')
    # update_coupon.click()
    update_coupon.attrs['onclick'] = "updateCoupon();"
else:
    print("验证优惠码的按钮不存在")

coupon_check_url = vpn_url + '/user/coupon_check'

data = {'ret': 1, 'name': '3天免费体验活动', 'credit': 100, 'onetime': 1, 'shop': '3', 'total': '0元'}

response = requests.post(coupon_check_url, cookies=cookies, json=data)


if response.status_code == 200:
    # get the json from the response
    print("coupon_check请求成功，结果为:" + json.dumps(response.json(), ensure_ascii=False))
else:
    print("coupon_check请求失败")

purchase_url = vpn_url + '/user/payment/purchase'

data = {'amount': 0}
response = requests.post(purchase_url, cookies=cookies, data=data)

if response.status_code == 200:
    # get the json from the response
    print("支付网关处理完毕，结果为:" + json.dumps(response.json(), ensure_ascii=False))
else:
    print("coupon_check请求失败")

# 购买请求的url
buy_url = vpn_url + '/user/buy'

data = {'coupon': '599_f3cZ8bzm', 'shop': '3', 'autorenew': '0', 'disableothers': '1'}

response = requests.post(buy_url, cookies=cookies, json=data)

if response.status_code == 200:
    # get the json from the response
    # print(response.text)
    print(json.dumps(response.json(), ensure_ascii=False))
else:
    print("Error")

# 访问需要登录后才能访问的页面
user_page_url = vpn_url + '/user'
response = requests.get(user_page_url, cookies=cookies)
soup_user_page = BeautifulSoup(response.text, 'lxml')

# 转化为字符串
html_text = str(soup_user_page)

# 输出clash url，前提是已经购买了3天套餐
# 使用正则表达式查找符合条件的内容
match = re.search("oneclickImport\s*\(\s*'clash'\s*,\s*'(.*?)'\s*\)", html_text)

if match:
    print("clash url：" + match.group(1))
else:
    print("匹配失败")