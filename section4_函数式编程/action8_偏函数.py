# 偏函数(Partial function)
# python的functools模块中提供的功能

# 示例:
# int()函数可以将字符串转换成整数,当只传入字符串时 函数默认按十进制进行转换
i = int('123456')
print(i)

# int()函数还提供额外的base参数(默认值是10) 如果传入base参数 则可以进行N进制转换
i = int('123456', base=8)
print(i)  # 输出:42798
i = int('123456', 16)
print(i)  # 输出:1193046


# 定义一个进制转换的函数
def int2(x, base=2):
    return int(x, base)


# 测试:
i1 = int2('10000')
print(i1)  # 输出:16

i2 = int2('123', base=4)
print(i2)  # 输出:27

# functools.partial:帮助创建一个偏函数
# 当函数参数过多时,需要简化时 使用functools.partial可以创建一个新的函数
# 这个新函数可以固定原函数的部分参数 从而在调用时更简单

# 示例:通过functools.partial建立一个新的函数int2

import functools

int2 = functools.partial(int, base=2)
print(int2('10000'))  # 输出:16
print(int2('123', base=4))  # 输出:27
