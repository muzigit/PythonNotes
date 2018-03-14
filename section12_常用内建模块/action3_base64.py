# base64
# Base64是一种用64个字符来表示任意二进制数据的方法

import base64

# 使用内置的base64模块进行编解码操作

# 编码:
e = base64.b64encode(b'binary\x00string')
print(e)    # 输出:b'YmluYXJ5AHN0cmluZw=='

# 解码:
d = base64.b64decode(e)
print(d)    # 输出:b'binary\x00string'

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数
# ，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
e = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e)    # 输出:b'abcd++//'
d = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(d)    # 输出:b'abcd--__'
d = base64.urlsafe_b64decode('abcd--__')
print(d)    # 输出:b'i\xb7\x1d\xfb\xef\xff'
