# 高阶函数:filter

# python内建的函数 filter()的作用:用于过滤序列

# 和map()类似 filter()也接收一个函数和一个序列,和map不同的是
# ,filter将传入的函数作用于每一个元素,根据返回是True or False来决定保留还是丢弃该元素

# 在一个list中,删掉偶数 只保留奇数


def is_odd(n):
    return n % 2 == 1


f = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(f)  # 输出:[1, 3, 5, 7, 9]


# 将一个序列中的空字符串删除
def not_empty(s):
    return s and s.strip()


L = ['a', None, "", '', 'B']
f = filter(not_empty, L)
# filter返回的是一个惰性序列 iterator 如果要强迫filter完成计算 需要用list()函数获取所有结果并返回list
s = list(f)

print(s)  # 输出:['a', 'B']


# 用filter求素数:
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 不断筛下去，就可以得到所有的素数。

# 构建一个从3开始的无限序列:
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器,不断返回下一个函数
def primes():
    # 这个生成器先返回第一个素数2 然后不断刷选出新的序列
    yield 2
    # 初始化序列
    it = _odd_iter()
    while True:
        # 返回序列的第一个数
        n = next(it)
        yield n
        # 构建新的序列
        it = filter(_not_divisible, it)


# 调用:
# 打印1000以内的素数
for i in primes():
    if i >= 1000:
        break
    else:
        print(i)

print('--------- 练习 ----------')


# 练习:
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return n == int(str(n)[::-1])


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
