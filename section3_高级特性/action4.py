# 生成器(generator)
# 定义: 一边循环一边计算的机制,称为生成器

# 创建一个generator
# 方式一: 将一个列表生成式的[]改成()

L = [x * x for x in range(0, 10)]  # 列表生成式
print(L)  # 输出:[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(type(L))  # 输出:<class 'list'>

L = (x * x for x in range(0, 10))
print(L)  # 输出:<generator object <genexpr> at 0x10220df10>
print(type(L))  # 输出:<class 'generator'>

# 迭代generator中的元素
print(next(L))  # 输出:0
print(next(L))  # 输出:1

from collections import Iterable

# 判断generator是否是可以迭代的
print(isinstance(L, Iterable))  # 输出: True

# 通过for循环迭代generator
for i in L:
    print(i)

print('--------- 分割线 ---------')


# 方式二: 通过关键字yield关键字 定义generator
# 打印斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # 这个式子等同于: a = b  b = a + b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)


# 将上面函数改成generator
def fib_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 一个函数中如果定义了yield 那这个函数就不是普通函数  而是一个generator
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f1 = fib_1(6)
print(f1)  # 输出:<generator object fib_1 at 0x102228fc0>

# 如果要获取generator的返回值 必须捕获StopIteration错误  返回值包含在StopIteration的错误中
while True:
    try:
        x = next(f1)
        print('f1:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# generator的执行顺序
# generator执行顺序和普通函数的执行顺序不一样 函数是顺序执行,遇到return就返回
# ,而generator 是每次调用next()时执行 再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
    return 'A'


o = odd()
print(o)
# 基本不会使用next来迭代
# next(o)

# 使用循环来迭代
for i in o:
    print(o)

print('--------- 分割线 ---------')


# 练习:
# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1

# 把每一行看做一个list，试写一个generator，不断输出下一行的list：


def triangles():
    L = [1]
    num = 0
    while True:
        num += 1
        yield L
        L = [L[i - 1] + L[i] for i in range(len(L))]
        if num == 6:
            return L


t = triangles()
while True:
    try:
        n = next(t)
        print('n:', n)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
