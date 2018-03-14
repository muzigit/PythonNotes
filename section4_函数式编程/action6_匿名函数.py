# 匿名函数
# 注:匿名函数只能有一个表达式,不用写return 返回值就是该表达式的结果

# 示例:  计算f(x)=x2  直接传入匿名函数

# lambda 表示匿名函数 冒号前面的x 表示函数参数
L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(L)

# 匿名函数也是一个对象 也可以把匿名函数赋值给一个变量 再利用变量来调用该函数
f = lambda x: x * x
print(f)  # 输出:<function <lambda> at 0x100661e18>
print(f(3))  # 输出:9


# 匿名也可以作为返回值返回

def build(x, y):
    return lambda: x * x + y * y


# 测试:
b = build(3, 5)
print(b())  # 输出:34


# 练习:
# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1
#
#
# L = list(filter(is_odd, range(1, 20)))
# print(L)    # 输出:[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 方式一:
def is_odd(n):
    return lambda: n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)    # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# 方式二:
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
