# requests:用于访问网络资源 在系统内置的urllib功能更强大 处理url资源更方便

import requests

# 示例:
# 1.通过GET访问豆瓣首页
r = requests.get('https://www.douban.com/')
# 设置响应超时时间
# r = requests.get('https://www.douban.com/', timeout=2.5) # 2.5秒后响应超时

# 获取状态码
print(r.status_code)  # 输出:200
# 获取响应文本
print(r.text)   # 返回响应的Html
# 获取响应头信息
print(r.headers)
# 获取指定Cookie  requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取
# print(r.cookies['ts'])


# 2.对于带参数的URL 传入一个dict作为请求参数
r1 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# 实际请求的URL
print(r1.url)  # 输出:https://www.douban.com/search?q=python&cat=1001
# requests自动检测编码 encoding:可以查看编码方式
print(r1.encoding)  # 输出:utf-8
# 无论响应是文本还是二进制内容,都可以用context属性获取bytes对象
print(r1.content)


# 3.requests对于特定的请求,例如JSON,可以直接获取
r2 = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r2.json())


# 4.需要传入HTTP header时,可以传入一个dict作为headers参数
r3 = requests.get('https://www.douban.com/',
                  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r3.text)


# 5.发送post请求 只需要将get改成post,传入data参数作为post请求的参数
r4 = requests.post('https://accounts.douban.com/login',
                   data={'form_email': 'abc@example.com', 'form_password': '123456'})
# requests默认使用 application/x-www-form-urlencoded 对post数据编码
# 如要传递JSON数据,可以直接传入JSON参数
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON


# 6.上传文件 需要使用 files参数
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)
# 注:在读取文件时,需要使用'rb'模式即二进制模式进行读取,这样获取的bytes长度才是文件长度

# 7.在请求中加入Cookie  只需要准备一个dict传入cookie参数
# cs = {'token': '12345', 'status': 'working')
# r = requests.get(url, cookies=cs)
