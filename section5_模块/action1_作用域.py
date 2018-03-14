# 作用域

# 正常的函数和变量名是 public,例:abc x123 PI

# 特殊变量: 类似 __xxx__ 是特殊变量,但是有特殊用途,例如:__name__,我们自己定义的变量一般不要用这种变量名

# 非公开变量 private :类似 _xxx or __xxx这样的函数和变量是非公开变量,不应该直接被引用,例如:_abc  __abc等

# 示例:
def _private1(name):
    return 'Hello,%s' % name


def _private2(name):
    return 'Hi,%s' % name


def greeting(name):
    if len(name) > 3:
        return _private1(name)
    else:
        return _private2(name)
