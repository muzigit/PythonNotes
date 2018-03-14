# 获取对象信息

# type()函数 的使用

# 1.用type() 判断基本类型
t1 = type(123)
print(t1)  # 输出:<class 'int'>

t2 = type(str)
print(t2)  # 输出:<class 'type'>

t3 = type(None)
print(t3)  # 输出:<class 'NoneType'>

# 比较两个变量的type是否相同
print(type(123) == int)  # 输出:True
print(type('abc') == type('123'))  # 输出:True
print(type('abc') == str)  # 输出:True

# 2.通过type模块中定义的常量 判断一个对象是否是函数
import types


def fn():
    pass


print(type(fn) == types.FunctionType)  # 输出:True
# BuiltinFunctionType:python内建函数
print(type(abs) == types.BuiltinFunctionType)  # 输出:True
print(type(lambda x: x) == types.LambdaType)  # 输出:True
print(type(x for x in range(10)) == types.GeneratorType)  # 输出:True

# 3.判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))  # 输出:True

# dir()函数的使用
# 1.作用:获取一个对象的所有属性和方法,它返回一个包含字符串的list

# 示例:获取一个str对象的所有属性和方法
print(dir('123'))  # 输出:['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']


# 2.配合getattr() setattr() hasattr() 可以操作一个对象的状态
# 示例:


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 2.1测试obj的属性

# 判断是否有属性 x
print(hasattr(obj, 'x'))  # 输出:True
# 判断是否有属性 y
print(hasattr(obj, 'y'))  # 输出:False
# 设置一个属性 y
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))  # 输出:True

# 获取属性 y
print(getattr(obj, 'y'))  # 输出:19
# 获取不存在的属性 会抛出AttributeError错误
# print(getattr(obj, 'z'))

# 也可以设置默认值  当找不到这个属性时 返回默认值
print(getattr(obj, 'z', 404))  # 输出:404

# 2.2 除了可以测试属性  还可以获取对象的方法

# 判断是否存在power函数
print(hasattr(obj, 'power'))  # 输出:True
# 获取power方法
p = getattr(obj, 'power')

# 因p已经指向了obj.power 所以可以调用power方法
print(p())  # 输出:81
