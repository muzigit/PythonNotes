# 此章节为函数系列

# Python内置函数
# abs(参数) 求绝对值
a = abs(-2)
print(a)

# max(参数) 接受N个参数 返回最大的那个值
m = max(100, -1, 99, -100, 1.99)
print(m)

# int(参数) 将其他数据类型转换成int类型
i = int('123')
print(i)
i1 = int(12.23)
print(i1)

# float(参数) 将其他数据类型转换成float类型
f = float('12')
print(f)

# str(参数) 将其他数据类型转换成字符串
s = str(12.23)
print(s)
t = type(s)
print(t)

# bool(参数) 将其他数据类型转换成布尔类型
b = bool(12.23)
print(b)    # 输出:True
b1 = bool('')
print(b1)  # 输出:False

# 别名概念: 将函数赋值给一个变量,相当于给这个函数取了别名  可以通过这个变量来调用这个函数
a = abs
m = a(-1.09)
print(m)    # 输出:1.09

print('----------  练习  ----------')
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
h = hex(n1)
print(h)    # 输出:0xff
t = type(h)
print(t)
t1 = hex(n2)
print(t1)   # 输出:0x3e8
