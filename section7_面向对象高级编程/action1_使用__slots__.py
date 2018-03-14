# 使用__slots__
# __slots__:限制class实例能添加的属性

# 动态语言的灵活性:创建一个class后,可以给该实例绑定任何实例和方法
# 注:
# 1.__slots__定义的属性仅对当前类属性起作用 对继承的子类不起作用
# 2.如子类也定义__slots__ 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


class Student(object):
    pass


s = Student()
# 给该实例绑定属性name
s.name = 'Tom'
print(s.name)  # 输出:Tom


# 给该实例绑定方法
def set_age(self, age):
    self.age = age


from types import MethodType

# 给实例绑定方法
s.set_age = MethodType(set_age, s)
# 调用实例方法
s.set_age(18)
print(s.age)

# 给一个实例绑定的方法 在另一个实例中不起作用
s1 = Student()


# s1.set_age(20)
# print(s1.age)


# 给class绑定方法  可以给所有实例都绑定方法
def set_score(self, score):
    self.score = score


# 给Student类绑定方法
Student.set_score = set_score

# 给class绑定方法后 所有实例均可以访问
s.set_score(20)
print(s.score)  # 输出:20

s1.set_score(30)
print(s1.score)  # 输出:30


# __slots__的使用
class School(object):
    # 限制只能添加 name 和 address 属性
    __slots__ = ('name', 'address')


s2 = School()
s2.name = '南大'
s2.address = '江西南昌'
# 动态绑定属性ranking 直接报AttributeError错误
# s2.ranking = 12
print(s2.name, s2.address)
