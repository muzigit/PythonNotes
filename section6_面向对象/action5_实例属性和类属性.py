# 实例属性 和 类属性

# 给类本身绑定一个属性
# 示例:


class Student:
    # 这里定义的属性 属于类属性 归Student类所有
    # 虽然归类所有 但是所有的实例对象均可以访问这个属性
    name = 'Student'


# 测试:
s = Student()
# 这里实例属性本身没有name属性 但是依然可以访问到类属性
print(s.name)  # 输出:Student

# 打印类的name属性
print(Student.name)  # 输出:Student

# 设置实例的name属性值
s.name = 'Tom'
# 实例属性比类属性优先级高,因此会屏蔽掉类属性值
print(s.name)  # 输出:Tom

print(Student.name)  # 输出:Student

# 删除实例属性
del s.name

# 当实例属性找不到时,类属性就显示出来了
print(s.name)  # 输出:Student


# 练习:
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
