# itertools
# itertools提供了非常有用的用于操作迭代对象的函数

import itertools

# itertools 提供的几个无限迭代器

# 第一种:count()会创建一个无限的迭代器,以下代码会打印出自然序列,无限循环下去
n = itertools.count(1)
# for i in n:
# print(i)

# 第二种:cycle()负责传入的序列无限重复下去
cy = itertools.cycle('ABC')
# for i in cy:
#     print(i)

# 第三种:repeat()负责把一个元素无限重复下去 设置参数二可以限定循环次数
r = itertools.repeat('ABC', 3)
for i in r:
    print(i)

# takewhile()函数 根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))  # 输出:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# chain() : 可以把一组迭代对象串联起来,形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)  # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

# groupby() : 把迭代器中相邻的重复元素挑出来放一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 输出:
# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']

# 如要忽略字母大小写分组
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

# 输出:
# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']
