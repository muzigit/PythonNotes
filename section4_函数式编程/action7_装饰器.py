# 装饰器(Decorator)
# 定义:在函数运行期间增加功能的方式

# 函数对象有一个__name__属性 可以获取函数名
def now():
    print('2017-3-1')


print(now.__name__)  # 输出:now

# 因函数也是一个对象 也可以将函数对象赋值给变量 通过变量来调用
f = now
print(f.__name__)  # 输出:now


# 示例:
# 定义一个能打印日志的Decorator

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# Decorator接受一个函数作为参数 并返回一个函数
@log    # 把@log放在f()函数定义处 相当于执行了语句:  f = log(f)
def f():
    print('2017年3月1日')


# 调用f()函数  不仅会运行f()函数本身  还会在运行前打印一行日志
print(f())
# 输出:
# call f():
# 2017年3月1日
