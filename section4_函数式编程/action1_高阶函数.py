# 高阶函数
# 定义:一个函数可以接收另一个函数作为参数,称为高阶函数

# 1.1 变量可以指向函数

# 要获得函数调用结果  可以将函数结果赋值给变量
a = abs(-10)
print(a)  # 输出:10

# 将函数本身赋值给变量
a = abs
# 结论:函数本身也可以赋值给变量 即:变量可以指向函数
print(a)  # 输出: <built-in function abs>

# 通过变量来调用函数
# 结论:变量a 已经指向函数本身 直接调用函数和调用变量a()完成相同
print(a(10))  # 输出:10


# 1.2 传入函数
# 示例:定义一个高阶函数

def add(x, y, f):
    return f(x) + f(y)


# 调用:
# x = -5  y = 6 f = abs  f我们传入一个系统内置的求绝对值的函数abs
f = add(-5, 6, abs)
print(f)
