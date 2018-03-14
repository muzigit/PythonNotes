# 切片

# 示例:
# 取一个list中的前三个元素

L = ['测试1', '测试2', '测试3', '测试4', '测试5']

# 方式一:
print(L[0], L[1], L[2])

# 方式二:通过循环来取
r = []
for i in range(3):
    r.append(L[i])
print(r)

# 方式三:使用Python提供的切片方式  也是最简便的方法
L1 = L[0:3]  # [0:3]表示从索引0开始取,但是不包括索引3
print(L1)
# 上面的简写
L11 = L[:3]
print(L11)

# 支持倒数切片
L2 = L[-2:]
print(L2)

L3 = L[-2:-1]
print(L3)

# 切片的运用

# 创建一个0-100的list
I = list(range(100))

# 取前10个数据
i1 = I[:10]
print(i1)

# 取后10个数据
i2 = I[-10:]
print(i2)

# 取前11 - 20的数据
i3 = I[11:20]
print(i3)

# 取前10个数据  每两个数据取一个
i4 = I[:10:2]
print(i4)

# 每5个取一个数
i5 = I[::5]
print(i5)

# 什么都不写 可以原样复制一个list
i6 = I[:]
print(i6)

# tuple也是一种list 也可以使用切片  只是操作结果仍旧是tuple

t = (1, 2, 3, 4, 5)[:2]
print(t)

# 字符串'xxx' 也可以看做是一种list 也可以使用切片操作

s = 'ABCDEFG'[:3]
s1 = 'ABCDEFG'[::2]
print(s)
print(s1)

print('----------  练习  ----------')


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(s):
    if len(s) == 0:
        return ''
    if not isinstance(s, str):
        # 不是字符串的先转换成字符串
        s = str(s)
    while s[:1] == ' ':
        if s[:1] != ' ':
            break

        s = s[1:]

    while s[-1:] == ' ':
        if s[-1:] != ' ':
            break
        s = s[:-1]
    return s


s = trim('  hello  ')
print(s,len(s))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
