# 迭代

# 字符串也可以通过for循环进行迭代

# 对dict进行迭代
d = {'a': 1, 'b': 2, 'c': 3}

# 默认情况下 dict迭代出的key
for key in d:
    print(key, d[key])

# 迭代dict中的value
for value in d.values():
    print(value)

# 同时迭代dict中key和value
for key, value in d.items():
    print(key, value)

# ---------- 如何判断一个对象是否是可以迭代的 ---------- #
# 通过collections中的Iterable来判断一个对象是否可以迭代

from collections import Iterable

# 字符串是可以迭代的
i1 = isinstance('abd', Iterable)  # True
print(i1)

# list是可以迭代的
i2 = isinstance([1, 2, 3], Iterable)  # True
print(i2)

# tuple是可以迭代的
i3 = isinstance((2, 3, 4), Iterable)  # True
print(i3)

# dict是可以迭代的
i4 = isinstance({'a': 1, 'b': 2, 'c': 3}, Iterable)  # True
print(i4)

# 整数是不可以迭代的
i5 = isinstance(1234, Iterable)  # False
print(i5)

# 实现类似java下标循环 可以通过python内置的enumerate 将函数变成 索引-元素对
for i, value in enumerate(['a', 'b', 'c', 'd']):
    print(i, value)

print('---------- 练习 ----------')


# 请使用迭代查找一个list中的最大值和最小值,并返回一个tuple

def findMinAndMax(L):
    t = ()
    if len(L) == 0:
        return (None, None)
    if not isinstance(L, Iterable):
        raise TypeError('对象是不可迭代的')

    x = max(L)  # 返回一个最大值
    y = min(L)  # 返回一个最小值
    t = (y, x)
    return t


print(findMinAndMax((1, 2, 30, 4, 5)))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
