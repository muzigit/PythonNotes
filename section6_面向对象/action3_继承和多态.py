# 继承和多态

# 当我们定义一个class的时候,可以从某个现有的class继承,新的class 称为子类(subclass)
# ,而被继承的class称为基类 父类 或 超类(Baseclass Superclass)

# 示例:
# 定义一个动物类 Animal
class Animal(object):
    def run(self):
        print('Animal is running......')


# 定义Dog 和 Cat类 继承Animal
class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


# 子类继承父类可以获取父类的全部功能
# 当子类复写了父类的方法,则调用子类自己的方法
dog = Dog()
cat = Cat()

print(dog.run())
print(cat.run())

# 判断一个变量是否是某个类型
print(isinstance(dog, Animal))  # 输出: True
