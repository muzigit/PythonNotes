# 使用dict 和 set

# dict的定义
d = {'Michael': 80, 'Bob': 75, 'Tray': 85}

# 通过key来放入元素
# 一个key只能对应一个value 如果多次对一个key放入value 后面的值会把前面的值替换掉
d['Adam'] = 67

# 查询dict长度
print(len(d))

# 查:
# 判断dict中key是否存在的两种方法
# 方法一: 通过in来判断
f = 'Bobs' in d
print(f)

# 方法二:通过dict提供的get()方法来判断  当key不存在时,返回None
# 注:get()方法的第二个参数是一个默认值  当key不存在时,返回默认值
b = d.get('Bobs')
print(b)

# 删
# pop(key)方法: 根据key来删除一个键值对
d.pop('Bob')
print(d)

print('-----------set的使用-----------')
# set是一组key的集合 不存储value 它是无序的 没有重复的key 重复的元素会自动被过滤
# set的定义:创建一个set 需要提供一个list作为输入集合
s = set(['A', 'B', 'C', 'A'])
print(s)  # 输出:{'C', 'B', 'A'} 注:这里的输出顺序不固定

# 增:
# add(key)  可以重复添加相同的key 但是不会有效果
s.add('D')
print(s)
s.add('D')
print(s)

s.add('E')
print(s)

# 删:
s.remove('E')
print('删除:', s)
# 注:这里不要使用pop()删除 因为set是无序的

# set是无序无重复元素的集合  因此可以利用这一特性进行数学的交集和并集运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])


# 求交集
s3 = s1 & s2
print('s1和s2交集:', s3)


# 求并集
s4 = s1 | s2
print('s1和s2并集:', s4)

