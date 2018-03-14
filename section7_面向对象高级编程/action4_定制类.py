# 定制类

# Python的class还有好多有特殊用途的函数

# __str__函数:


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student object (name %s)' % self.__name

    # 利用__getattr__方法 可以动态返回属性 或者 函数
    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25

    # __str__:返回的是用户看到的字符串
    # __repr__:返回程序开发者看到的字符串 __repr__主要是为调试服务的
    # 这两者返回的东西都是一样的
    __repr__ = __str__


s = Student('Tom')
# 当没有调用__str__函数 打印出来的是类似<__main__.Student object at 0x109afb310>这样的字符串
# 而调用__str__函数后 打印出来的是我们定义的字符串
print(s)


# __iter__函数:
# 如果一个类想被用于for...in循环,类似list和tuper那种,就必须实现__iter__函数,该函数返回一个迭代对象
# ,然后python的for循环就会不断调用该对象的next()方法拿到循环的下一个值,直到遇到StopIteration错误退出循环

# 示例:
# 以斐波那契数列为例，写一个Fib类，可以作用于for循环：


class Fib(object):
    def __init__(self):
        # 初始化两个计数器
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, item):
        a, b = 1, 1
        # item是int
        if isinstance(item, int):
            for i in range(item):
                a, b = b, a + b
            return a

        # item是切片
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 测试:把Fib作用于for循环
for i in Fib():
    # print(i)
    pass

# __getitem__函数:
# 要像list一样按照下标取元素,必须实现此函数
# 在Fib类中,再定义一个__getitem__()函数

# 测试:
f = Fib()
print(f[0])  # 输出:0
print(f[10])  # 输出:89

# list还有一个切片功能,如果Fib也要实现类似功能 需要在方法中进行类型判断
# 测试:
print(f[0:5])  # 输出:[1, 1, 2, 3, 5]
print(f[:10])  # 输出:[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 与__getitem__函数对应的该有__setitem__函数,把对象视作list或dict来对集合赋值

# __delitem__函数:用于删除某个元素


# __getattr__
# 当我们调用类的方法和属性时,如果不存在,则会报错
# 但是,python还有另一个机制,写一个__getattr__()方法,动态返回一个属性

# 测试:
s11 = Student('Mary')
# 在上面的Student类中 我们调用了__getattr__方法
# 当我们调用不存在的属性时,python解释器会视图调用__getattr__(self,'score')来尝试获取属性
print(s11.score)  # 输出:99

# 动态返回函数也是可以的
print(s11.age())  # 输出:25


# 示例:
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

#   http://api.server/user/friends
#   http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#
# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        print('self.__path:', self.__path, 'path:', path)
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__


# 测试:
print(Chain().status.user.timeline.list)  # 输出:/status/user/timeline/list


# __call__函数:直接对实例进行调用
# 示例:
class Student_1(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)


# 测试:
m = Student_1('Monica')
m()  # 输出:My name is Monica

# 判断一个变量是对象还是函数的方法:
# 判断这个对象是否可以被调用,能被调用的对象就是一个Callable对象

print(callable(s))  # 输出:False
print(callable(max))    # 输出:True
print(callable(Student))    # 输出:True
print(callable(None))    # 输出:False
print(callable(str))    # 输出:True
