# 定义函数

# 练习:
# 自定义一个求绝对值的my_abs函数：
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 调用定义的函数
m = my_abs(-1.99)
print(m)


# 定义一个空函数
def nop(x):
    # pass 表示什么也不做  主要是起到占位符的作用(注:在其他语句块中也可以使用)
    pass


# 参数检查
def my_abs_check(x):
    # 判断传进来的参数是否是int or float类型
    if isinstance(x, (int, float)):
        # 抛出TypeError异常
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# c = my_abs_check(11.11)
# print(c)

# 返回多个参数
import math


# 例子:在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  # 输出:151.96152422706632 130.0

r = move(100, 100, 60, math.pi / 6)
t1 = type(r)
print(r)
# python 返回的多个参数其实一个假象 其实就是返回一个tuple,但写起来更方便
print(t1)  # 输出: <class 'tuple'>

print('---------- 练习 ----------')


# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
#
# 的两个解。
def quadratic(a, b, c):
    # a和b只能是int类型或float类型
    if not isinstance(a, (int, float)) and not isinstance(b, (int, float)):
        raise TypeError(' bad operand type')
    if a == 0 and b == 0:
        return None

    n = b ** 2 - (4 * a * c)
    
    # math.sqrt() 计算平方根
    root1 = (-b + math.sqrt(n)) / 2 * a
    root2 = (-b - math.sqrt(n)) / 2 * a
    return root1, root2


# 测试
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
