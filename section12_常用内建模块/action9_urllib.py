# urllib
# urllib提供了一系列操作url的功能

# Get
# 利用urllib的request模块 发送一个get请求到指定的页面 并返回http的响应

# 示例:
# 对豆瓣的url https://api.douban.com/v2/book/2129650 进行抓取,并获取响应
from urllib import request, parse
import urllib
import ssl

url = 'https://api.douban.com/v2/book/2129650'

# with request.urlopen(url, context=ssl._create_unverified_context()) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' % (k, v))
#     print('Data:', data.decode('utf-8'))


# 模拟浏览器发送Get请求
# 示例:
# 模拟ipone6去请求豆瓣首页
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                             'AppleWebKit/536.26 (KHTML, like Gecko) '
                             'Version/8.0 Mobile/10A5376e Safari/8536.25')

# with request.urlopen(req, context=ssl._create_unverified_context()) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# -------------------------------------------------------------------------
# post
# 发送post请求,只需要将参数data以bytes形式传入

# 示例:
# 模拟微博登入,先读取登录的邮箱和口令,然后按照weibo.cn的登录页格式以 username=xxx&password=xxx 的编码传入：

print('Login to weibo.cn...')
emile = input('Emile:')
password = input('PassWord:')

login_data = parse.urlencode([
    ('username', emile),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                             'AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8'),context=ssl._create_unverified_context()) as f:
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# -------------------------------------------------------------------------
# Handler
# 通过Proxy访问网站,需要利用ProxyHandler来处理
# 示例:
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass