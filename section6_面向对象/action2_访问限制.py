# 访问限制

# 这里访问限制可以理解为JavaBean内容
# 当我们定义一个成员变量时,为保护成员变量不被随意修改,对成员变量进行私有化,然后提供get() and set()方法,以供外部访问

# 示例:

class Student(object):
    # 在python中 以 _abc __abc 这种格式的视为私有变量,无法直接从外部访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    # 对外提供get() set()方法供外部访问
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    # 在设置方法中  可以检查参数有效性
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
