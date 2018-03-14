# StringIO:在内存中读写str
from io import StringIO, BytesIO

f = StringIO()
# 返回写入的字符长度
print(f.write('hello'))  # 输出:5
print(f.write(' '))  # 输出:1
print(f.write('world!'))  # 输出:6
# 获取写入后的str
print(f.getvalue())  # 输出:hello world!

# 在初始化StringIO时写入str,然后,像读文件一样读取
f = StringIO('Hello!\nHi!\nGoodBye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# 输出:
# Hello!
# Hi!
# GoodBye!


# BytesIO:在内存中读取bytes
b = BytesIO()
# 这里写入的不是str 而是经过utf-8编码的bytes
print(b.write('中文'.encode('utf-8')))  # 输出:6
print(b.getvalue())  # 输出:b'\xe4\xb8\xad\xe6\x96\x87'

# BytesIO也可以如StringIO一样 在初始化BytesIO时,写入数据
b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# 读取数据
print(b.read()) # 输出:b'\xe4\xb8\xad\xe6\x96\x87'
b.close()
