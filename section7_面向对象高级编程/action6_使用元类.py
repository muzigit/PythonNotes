# 使用元类

# type()
# type()函数既可以返回一个对象的类型,又可以创建出新的类型

# 示例:
# 通过type()函数创建一个Hello类

# 先定义函数
def fn(self, name='world'):
    print('Hello %s' % name)


# 创建Hello class  type()函数需要传入3个参数
# 1.class的名称
# 2.继承的父类集合(注:Python支持多继承,如只有一个父类,使用tuple的单元素写法)
# 3.class的方法名称与函数绑定,这里把函数fn绑定在方法名hello上
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()  # 输出:Hello world

print(type(Hello))  # 输出:<class 'type'>
print(type(h))  # 输出:<class '__main__.Hello'>


# metaclass:元类
# 作用:控制类的创建行为

# metaclass是类的模板 必须从type类型派生
class ListMetaclass(type):

    # 参数说明:
    # 1.当前准备创建的类的对象
    # 2.类的名字
    # 3.类继承的父类集合
    # 4.类的方法集合
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 当传入metaclass参数后,python解释器在创建MyList时,要通过ListMetaclass.__new__()来创建
# ,在此,我们可以修改类的定义(例:加上新的方法,然后,返回修改后的定义)
class MyList(list, metaclass=ListMetaclass):
    pass


# 测试:
L = MyList()
L.add(1)
print(L)    # 输出:[1]
