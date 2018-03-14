# 使用list和tuple

# list中的元素  类型可以是不同类型
classmates = ['A', 'B', 12, 0.23, True]
print(classmates)

# len():可以获取list元素个数
print(len(classmates))

# list的索引是从0开始访问的
print(classmates[0])

# 查: 获取list最后一个元素
# 方式一:通过len()函数来获取
print(classmates[len(classmates) - 1])

# 方式二:可以直接通过-1来获取
print(classmates[-1])

# 增:往list中增加元素到末尾
classmates.append('C')
print(classmates)

# 将元素插入到指定位置
classmates.insert(2, 'D')
print(classmates)

# 删: pop():删除list末尾的元素
classmates.pop()
print(classmates)
classmates.pop(-2)
print(classmates)
classmates.pop(0)
print(classmates)

# 改:给某个元素赋值 可以指定索引位置进行赋值
classmates[0] = 'Z'
print(classmates)

# list也可以是另一个list 类似于java中的二维数组
s = [classmates, False, 'x', '中文字符']
print(s)

#  获取s中另一个list索引为1的元素
print(s[0][1])

# --------------tuple---------------- #
# tuple和list类似 但是tuple一旦确定了就不可修改
# tuple的定义

# 当tuple的元素个数是1个时,需要在元素后面加一个,   来消除和数学意义上的小括号的歧义
# 如未在后面加,  则按照小括号进行计算
tuple1 = (1,)
print(tuple1)

tuples = (1, 2, 2, 3, classmates)
# count():查询某个元素在tuple中的个数
t = tuples.count(2)
print(t)

# tuple的不可变指的是指向不可变  tuple里面包含了一个list元素 list本身是可变的
tuples[4][0] = 'A'
print(tuples)

print('#---------------------作业-----------------------#')
# 作业:用索引取出list的元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 方式一:
for i in L:
    # isinstance():判断变量是否是指定类型
    if (isinstance(i, list)):
        for j in i:
            print(j)
    print(i)

# 方式二:
print("方式二结果:",
      L[0][0], L[0][1], L[0][2],
      L[1][0], L[1][1], L[1][2], L[1][3],
      L[2][0], L[2][1], L[2][2]
      )
# 换行打印
print("方式二结果:", L[0][0]), print(L[0][1])
