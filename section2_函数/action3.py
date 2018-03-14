# 函数的参数:
# 分类:必选参数 默认参数 可变参数 关键字参数
# 注:
# 1.必选参数 和 默认参数  必选参数在前,默认参数在后
# 2.当有多个参数时  变化大的参数放前面,变化小的放后面 变化小的参数可以作为默认参数

def add_end(L=[]):
    L.append('END')
    return L


# 在函数初始化的时候 L的值就被计算出来了 即:[]
# 同时L也是一个变量 指向[]  当每次调用函数时,如果改变了L的内容 则下次默认参数的值也随之改变
print(add_end())  # ['END']
print(add_end())  # ['END', 'END']


def add_end_2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 通过使用不变对象None 可以修复上述可变参数内容被修改问题
print(add_end_2())  # 输出:['END']
print(add_end_2())  # 输出:['END']


# -----------------------------
# 可变参数
# 可变参数的定义:
# 定义可变参数和list,tuple参数相比 就是在前面多了一个*  在函数内部,参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 调用可变参数 可以传入N个参数,包括0个参数 这些可变参数在函数调用时,自动组装成tuple
c = calc(1, 2, 3, 4, 5)
print(c)


# -----------------------------
# 关键字参数(作用:可以拓展函数函数的功能)
# 关键字参数允许你传入0个或任意个含参数名的参数,这些关键字参数在函数内部自动封装成dict
# 定义: **kw 就是关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 调用:
person('Tom', 30)

person('Jack', 28, city='BeiJing')
# 可以传入任意个数的关键字参数
person('Bob', 32, city='JiangXi', Job='Python')

# 除了上面那种调用方式  也可以先组装成一个dict,再将dict转换成关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Android'}

person('Adam', 24, city=extra['city'], job=extra['job'])
# 这种是上面的简化写法
person('John', 40, **extra)


# -----------------------------
# 命名关键字参数(作用:需要限制关键字参数的名字)
# 和关键字参数不同,命名关键字参数需要一个特殊分隔符*,*后面的参数就视为命名关键字参数
# 定义:
def user(name, age, *, city, job):
    print(name, age, city, job)


# 调用:
# 错误调用方式:
# user('Tom',34,)
# user('Tom',34,'Tianjing','professional')

# 正确调用方式: 命名关键字参数必须传入参数名
user('Hani', 32, city='Nanjing', job='Writer')


# 如果函数定义中已经有了一个可变参数,后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 注:当函数中没有可变参数时,则必须使用特殊分隔符*  否则解释器将所有参数视作位置参数
def user_1(name, age, *args, city, job):
    print(name, age, args, city, job)


# 调用:
# 错误调用方式: 命名关键字参数必须传入参数名,否则解释器将四个参数视作位置参数
# user_1('Hani', 32, 'Nanjing', 'Writer')

# 正确调用方式:
user('Hani', 32, city='Nanjing', job='Writer')


# 命名关键字参数可以有缺省 简化调用,如下 city有一个默认值,可传可不传
def user_2(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 调用:
user_2('Hani', 32, city='Nanjing', job='Writer')
# 可不传city参数
user_2('Bob', 32, job='Python')


# -----------------------------
# 参数组合
# 定义函数时,可以使用必选参数 默认参数 可变参数 关键字参数 命名关键字参数进行组合使用
# 注意事项:
# 参数定义的顺序必须是: 必选参数 --> 默认参数 --> 可变参数 --> 命名关键字参数 --> 关键字参数
# 示例:包含上述所有参数组合
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args:', args, 'kw:', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw:', kw)


# 调用:
f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)  # 输出:a= 1 b= 2 c= 3 args: ('a', 'b') kw: {'x': 99}
f1(1, 2, d=99, ext=None)  # 输出:a= 1 b= 2 c= 0 args: () kw: {'d': 99, 'ext': None}

# 通过一个tuple和dict 也可以调用上述函数
args = {1, 2, 3, 4}
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

print('----------  练习  ----------')


# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#     return x * y

def product(*numbers):
    L = [False for i in numbers if not isinstance(i, (int, float))]
    print('L=', L)
    if L:
        raise TypeError('bad input type')

    num = 0

    if len(numbers) > 0:
        num = 1
    else:
        raise TypeError('numbers length must > 0')

    for i in numbers:
        num = i * num
    return num


p = product(2, 3, 4)
print(p)
