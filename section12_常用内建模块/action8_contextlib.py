# contextlib

# 在python中,正确关闭文件资源的一个方法是使用try...finally
# 示例:
# try:
#     f = open('/path/to/file', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()

# 使用python的with语句可以很方便的使用资源,而不用担心资源没有关闭
# 示例:
# with open('/path/to/file', 'r') as f:
#     f.read()

# 任何对象只要实现了上下文管理,就可以使用with语句
# 实现上下文管理是通过__enter__和__exit__这个两个方法来实现的

# 示例:
class Query(object):
    def __init__(self, name):
        self.__name = name

    def __enter__(self):
        print('__enter__被调用')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.__name)


# 测试:
# 这样就可以把资源对象用于with语句
with Query('Tom') as q:
    q.query()

# 输出:
# __enter__被调用
# Query info about Tom...
# End

# -------------------------------------------------
# @contextmanager
# 编写__enter__ 和 __exit__依然很繁琐 因此contextlib提供了更简便的写法
from contextlib import contextmanager


class QueryTest(object):
    def __init__(self, name):
        self.__name = name

    def query(self):
        print('Query info about %s...' % self.__name)


@contextmanager
def create_query(name):
    print('Begin')
    q = QueryTest(name)
    yield q
    print('End')


# 测试:
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()


# 输出:
# Begin
# Query info about Bob...
# End


# 很多时候,我们希望在某段代码执行前后自动执行特定代码,也可以使用@contextmanager
# 示例:
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# 输出:
# <h1>
# hello
# world
# </h1>

# 代码的执行顺序是：
#
# 1.with语句首先执行yield之前的语句，因此打印出<h1>；
# 2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3.最后执行yield之后的语句，打印出</h1>


# -------------------------------------------------
# @closeing
# 如果一个对象没有实现上下文,就不能把它用于with语句,这个时候,可以使用@closeing把该对象变成上下文对象

# 示例:
from contextlib import closing
from urllib.request import urlopen
import ssl

# 请求http网站可以不设置context
with closing(urlopen('https://www.python.org', context=ssl._create_unverified_context())) as page:
    for line in page:
        print(line)


# closing也是一个经过@contextmanager装饰的generator
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
