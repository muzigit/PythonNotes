# 迭代器(Iterator)
# 定义:Iterator对象表示的是一个数据流,可以被next()函数调用并不断返回下一个值的对象,知道没有数据时,抛出StopIterator异常
# 可以把这个数据流看成是一个有序序列,但我们不能提前知道序列的长度

# 可以使用isinstance()函数判断一个对象是否是Iterator对象

from collections import Iterator

i1 = isinstance('abc', Iterator)
print(i1)  # False

i2 = isinstance((x * x for x in range(10)), Iterator)
print(i2)  # True

i3 = isinstance((), Iterator)
print(i3)  # False

i4 = isinstance([], Iterator)
print(i4)  # False

i5 = isinstance({}, Iterator)
print(i5)  # False

i6 = isinstance(123, Iterator)
print(i6)  # False

# list str tuple 是Iterable 但是却不是Iterator
# 将Iterable 转换成 Iterator 可以使用iter()函数
i7 = isinstance(iter(()), Iterator)
print(i7)  # True
i8 = isinstance(iter([]), Iterator)
print(i8)  # True
i9 = isinstance(iter('abc'),Iterator)
print(i9)   # True
