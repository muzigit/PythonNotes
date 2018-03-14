# 类和实例

# 定义一个Student类 括号中的object 是继承的类

# 实例:


class Student(object):
    # 绑定实例属性方式一:可以在创建实例的时候  绑定实例
    # __init__:在这里__init__相当于java中的构造函数
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __init__(self):
        pass


bart = Student()
# 0x101a442b0 表示的是内存地址
print(bart)  # 输出: <__main__.Student object at 0x101a442b0>

# 绑定实例属性方式二: 给实例bart绑定一个属性
bart.name = 'Tom'
print(bart.name)
