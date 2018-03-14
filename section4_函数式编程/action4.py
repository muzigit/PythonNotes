# 高阶函数:sorted
# 作用:可以接收一个key函数来实现自定义的排序

# 排序算法

# 对list进行排序
L = [90, -1, 34, 32, 88, 77, -33]
s = sorted(L)
print(s)  # 输出:[-33, -1, 32, 34, 77, 88, 90]

# 接收一个函数 实现自定义排序
s = sorted(L, key=abs)
print(s)  # 输出:[-1, 32, -33, 34, 77, 88, 90]

# 对字符串排序
# 字符串默认排序方式:根据ASCII的大小进行排序  'Z' < 'a'
s = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(s)  # 输出:['Credit', 'Zoo', 'about', 'bob']

# 对字符串忽略大小写  按照字母序进行排序
s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(s)  # 输出:['about', 'bob', 'Credit', 'Zoo']

# 进行字符串反向排序
s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(s)  # 输出:['Zoo', 'Credit', 'bob', 'about']

# 练习:
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    # 忽略字母大小写方式
    # return t[0].lower()

    # 默认字母排序方式
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


# 再按成绩从高到低排序：
def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score)
print(L2)
