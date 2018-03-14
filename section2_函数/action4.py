# 递归函数
# 定义:在一个函数内部调用自身,这个函数就是递归函数

# 示例:求阶乘
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n


def fact(n):
    if not isinstance(n, (int, float)):
        raise TypeError('bad input type')
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


# 注:递归并不是无限递归的  递归层次过多会导致栈溢出(例:fact(1000))
# 解决递归栈溢出可以通过 尾递归优化
# 尾递归:指的是在函数返回的时候,调用自身本身,并且,return语句不能包含表达式
f = fact(100)
print(f)


# 使用尾递归优化
def fact_1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, product * num)


# 调用:
# 注:尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
f1 = fact_1(100)
print(f1)


# 练习:
# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


print(move(1, 'A', 'B', 'C'))
print(move(2, 'A', 'B', 'C'))
print(move(3, 'A', 'B', 'C'))
