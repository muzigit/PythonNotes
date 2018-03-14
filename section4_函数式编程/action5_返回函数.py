# 函数作为参数返回

# 示例:实现一个可变参数的求和

# 这个是普通求和方式的定义
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = n + ax
    return ax


# L = [1, 2, 3, 4]
# print(calc_sum(L))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


# 测试:
L = (1, 2, 3, 4)
f = lazy_sum(L)

# 调用lazy_sum()返回的不是求和结果 而是求和函数sum()
print(f)  # 输出:<function lazy_sum.<locals>.sum at 0x102a26598>
# TODO 此处运行报错 暂未找到错误原因

# 只有调用函数f() 才返回真正的求和结果
# print(f())

# 当调用lazy_sum()函数时,每次都会返回一个新的函数 即使是传入相同的参数
f1 = lazy_sum((1, 2, 3, 4))
f2 = lazy_sum((1, 2, 3, 4))
print(f1)  # 输出:<function lazy_sum.<locals>.sum at 0x101a26620>
print(f2)  # 输出: <function lazy_sum.<locals>.sum at 0x101a266a8>

# f1() & f2() 的调用结果互不影响
print(f1 == f2)  # 输出:False


# 闭包
# 定义:在函数A中定义了函数B,内部函数B可以引用外部函数A的参数和局部变量
# ,当函数A返回函数B时,相关参数和变量都保存在返回的函数中

# 注:返回闭包时,返回函数不要引用循环变量,或后续会发生变化的变量

# 示例:
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
# 输出:
# <function count.<locals>.f at 0x101a46840>
# <function count.<locals>.f at 0x101a468c8>
# <function count.<locals>.f at 0x101a46950>
print(f1, f2, f3)

print(f1(), f2(), f3())  # 输出:9 9 9


# 练习:
# 利用闭包返回一个计数器函数,每次调用它返回递增函数
def createCounter():
    # 方式一:
    n = [0]

    def counter():
        n[0] = n[0] + 1
        return n[0]

    # 方式二:
    # n = 0
    # def counter():
    #     nonlocal n
    #     n = n + 1
    #     return n

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
