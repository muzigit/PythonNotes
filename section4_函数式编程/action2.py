# map/reduce

# python内置了函数 map() 和reduce()函数

# map() 接收两个参数:一个是函数  另一个是Iterable  并将结果作为新的Iterator返回
# 示例:
# 有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

#             f(x) = x * x
#
#                   │
#                   │
#   ┌───┬───┬───┬───┼───┬───┬───┬───┐
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   2   3   4   5   6   7   8   9 ]
#
#   │   │   │   │   │   │   │   │   │
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   4   9  16  25  36  49  64  81 ]

def f(x):
    return x * x


m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# m 是一个map类型 通过list()函数将map转换成list
print(list(m))

# map() 不但可以计算简单的f(x) = x * x , 还可以计算任意复杂的函数
# 示例:将list中的数字全部转换成字符串
m1 = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(m1))

print('---------- 分割线 ----------')

# reduce
# reduce的用法: reduce把一个函数作用在一个序列[x1, x2, x3, ...]上,这个函数必须接收两个参数
# ,reduce把结果继续和序列的下一个元素做累计计算,其效果就是:
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 示例:对一个序列求和 用reduce实现:

from functools import reduce


def add(x, y):
    return x + y


# 除了下面这种方式  python内置的sum()函数也可以进行求和
n = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(n)


def fn(x, y):
    return x * 10 + y


# 将序列变成整数13579
n = reduce(fn, [1, 3, 5, 7, 9])
print(n)  # 输出:13579


# 将str转换成int的函数

def str2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


s = reduce(fn, map(str2num, '13579'))
print(s)  # 输出:13579

# 将上面两个函数整理成一个
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def str2num(s):
        return DIGITS[s]

    return reduce(fn, map(str2num, s))


# 调用:
s1 = str2int('13579')
print(s1)  # 输出:13579


# 使用lambda函数进一步简化上述函数
def str2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(str2num, s))


# 调用:
s2 = str2int('13579')
print(s2)  # 输出:13579

print('---------- 分割线 ----------')


# 练习一:
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']


def normalize(name):
    if not isinstance(name, str):
        name = str(name)
    # name.capitalize() 将首字符转换成大写
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 练习二:
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(s):
    return reduce(lambda x, y: x * y, s)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习三:
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):
    s = s.split('.')
    print('切割后的字符串:', s)

    # 处理小数点前面的数字
    def f1(x, y):
        return x * 10 + y

    # 处理小数点后面的数字
    def f2(x, y):
        return x / 10 + y

    # 字符串转换成数字
    def str2num(s):
        return DIGITS[s]

    return reduce(f1, map(str2num, s[0])) + reduce(f2, list(map(str2num, s[1]))[::-1]) / 10


print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
