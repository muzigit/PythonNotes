# 使用@property
# 作用:负责把一个方法变成属性调用


class Student(object):
    # 把一个getter方法变成属性 只需要加上@property即可
    @property
    def score(self):
        return self._score

    # @property本身又创建了另一个装饰器@score.setter,负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an Integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 在这里 birth是可读写属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 在这里age是只读属性 因为age是根据 birth计算出来的
    @property
    def age(self):
        return 2015 - self._birth


s = Student()
# 这里相当于 s.set_score(66)
s.score = 66
# 这里相当于 s.get_score()
print(s.score)  # 输出:66


# s.score = '123'   # 因为我们做了参数检查 因此这里会报错
# s.score = 1000    # 因为我们做了参数检查 因此这里会报错



# 练习:
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
