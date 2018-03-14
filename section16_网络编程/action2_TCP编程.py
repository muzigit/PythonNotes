# TCP编程
# 通常用一个Socket表示“打开了一个网络链接”,而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。


# 客户端
# 创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。
# 示例:
# 在浏览器中访问新浪时，我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。
# 如果一切顺利，新浪的服务器接受了我们的连接，一个TCP连接就建立起来的，后面的通信就是发送网页内容了

# 创建一个基于TCP连接的Socket:

import socket

# 创建一个socket  AF_INET:表示指定IPv4协议 AF_INET6:表示IPv6协议
import threading

import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 注:TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# 例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
# 发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接
s.close()

# 将Http头和网页分离
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    # 内容保存到文件
    f.write(html)

# ----------------------------------------
# 服务器
# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接
# 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket

# 示例:
# 创建一个简单的服务器程序,它接收客户端连接,把客户端发过来的字符串加上hello再发回去

# 创建一个IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听地址和端口
s.bind(('127.0.0.1', 9999))
# 开始监听端口 传入的参数表示等待连接的最大数量
s.listen(5)
print('Waiting for connection...')
# 设置一个永久循环来接受客户端的连接 accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

    # 每个连接都必须创建新线程(or进程)来处理
    def tcplink(sock, addr):
        print('Accept new connection from %s:%s...' % addr)
        sock.send(b'Welcome!')
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))


    sock.close()
    print('Connection from %s:%s closed.' % addr)


# 创建一个客户端程序来测试创建的TCP服务端:
# 注:测试时需要开启两个窗口方可进行测试
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s1.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s1.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s1.send(data)
    print(s1.recv(1024).decode('utf-8'))
s1.send(b'exit')
s1.close()
