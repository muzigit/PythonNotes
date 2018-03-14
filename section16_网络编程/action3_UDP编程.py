# UDP编程

# TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
# 优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

import socket

# 创建服务端
# 首先绑定端口  SOCK_DGRAM:表示这个socket类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999)) # 127.0.0.1 是本机IP地址

print('Bind UDP on 9999...')
# 注:这里因是测试 所以未使用多线程
while True:
    # 接收数据  recvfrom()返回数据和客户端的地址和端口
    data,addr = s.recvfrom(1024)
    print('Receiver from %s:%s'% addr)
    # sendto()把数据用UDP发送给客户端
    s.sendto(b'Hello, %s!' % data, addr)


# -------------------------------------
# 创建客户端
# 注:如要测试 需开启两个窗口
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
