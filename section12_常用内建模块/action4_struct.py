# struct
# struct主要是用来解决bytes和其他二进制数据类型的转换

import struct

# struct的pack()函数把任意数据类型变成bytes

# 参数1:表示处理指令  >I的意思:  > 表示字节顺序big-endian 也就是网络序  I 表示4字节无符号整数
p = struct.pack('>I', 10240099)
print(p)  # 输出:b'\x00\x9c@c'

# unpack() 把bytes变成相应的数据类型
p1 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(p1)  # 输出:(4042322160, 32896)
