# collections: python内建的一个集合模块,提供了许多有用的集合类

# namedtuple:
# namedtuple是一个函数,它用来创建一个自定义的tuple对象,并且规定了tuple元素的个数
# ,并可以用属性而不是用索引来引用tuple的某个元素

from collections import namedtuple

# 示例:定义一个点的二维坐标

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('p.x:', p.x, 'p.y:', p.y)  # 输出:p.x: 1 p.y: 2

# 验证Point是tuple的一个子类
print(isinstance(p, tuple))  # 输出:True

# ---------------------------------------------------
# deque:
# deque是为了高效实现插入和删除操作的双向列表,适用于队列和栈
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('e')
q.remove('d')
print(q)  # 输出:deque(['e', 'a', 'b', 'c', 'd'])

# ---------------------------------------------------
# defaultdict:
# 使用dict时,如果 key 不存在时,会抛出KeyError.如果希望key不存在时,返回一个默认值,可以使用defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # 输出:abc

# 当key值不存在时,返回定义的默认值
print(dd['key2'])  # 输出:N/A

# ---------------------------------------------------
# OrderedDict:
# 使用dict时,key是无序的.如要保持key的顺序,可以使用OrderedDict
from collections import OrderedDict

od = OrderedDict()
od['z'] = 1
od['b'] = 2
od['c'] = 3
# 按照插入的顺序返回
print(list(od.keys()))  # 输出:['z', 'b', 'c']


# 示例:
# 利用OrderedDict 实现一个FIFO(先进先出)的dict,当容量超出限制时,先删除最早添加的key

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.__capacity = capacity

    def __setitem__(self, key, value):
        containskey = 1 if key in self else 0
        if len(self) - containskey >= self.__capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containskey:
            del self[key]
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# 测试:
dict = LastUpdatedOrderedDict(3)
dict['a'] = 1
dict['b'] = 12
dict['c'] = 123
dict['d'] = 1234
dict['e'] = 12345
print(list(dict.items()))  # 输出:[('c', 123), ('d', 1234), ('e', 12345)]

# ---------------------------------------------------
# Counter:
# Counter是一个简单的计数器  Counter也是Dict的子类
from collections import Counter

# 示例:统计字符出现的个数
c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)  # 输出:Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
