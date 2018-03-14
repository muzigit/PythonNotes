# 使用枚举类

# 使用Python内置函数Enum类实现枚举类

from enum import Enum, unique

# 示例:
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 如上定义,获取到了Month类型的枚举类

# 遍历枚举类中的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 从Enum中派生出自定义类,可以更精准的控制枚举类型

@unique  # 检查是否有重复值
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问枚举类的方法:
day1 = WeekDay.Mon
print(day1)  # 输出:WeekDay.Mon
print(WeekDay['Sun'])  # 输出:WeekDay.Sun
print(WeekDay.Mon.value)  # 输出:1
print(day1 == WeekDay.Sun)  # 输出:False
print(WeekDay(1))  # 输出:WeekDay.Mon

# 遍历所有枚举类成员
for name, member in Month.__members__.items():
    print(name, ':', member)


# 练习:
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
