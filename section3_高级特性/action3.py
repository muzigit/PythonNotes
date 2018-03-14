# 列表生成式

# 例子:生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = range(1, 11)
l = list(r)

for i in l:
    print(i)

# 例子:生成[1*1,2*2,3*3,...,10*10]

# 方法一:通过循环

L = []
for i in range(1, 11):
    L.append(i * i)
    # L.append(str(i) + '*' + str(i))
print(L)

# 通过列表生成式可以一句话替换上面的代码
# 写列表生成式时,将要生成的元素x * x放在前面,后面跟上for循环
L = [x * x for x in range(1, 11)]

print(L)

# 在for循环后面还可以跟上布尔表达式
L1 = [x * x for x in range(1, 11) if x % 2 == 0]
# 在这里我们通过布尔表达式 筛选出偶数
print(L1)

# 使用双循环 实现字符串全排列
L2 = [m + n for m in 'ABC' for n in 'XYZ']
print(L2)

# 列表表达式的运用
# 列出当前目录下的所有文件
import os

L3 = [file for file in os.listdir('.')]  # os.listdir  可以列出文件和目录
print(L3)

# 使用列表表达式 通过两个变量来接收
L = {'a': 'A', 'b': 'B', 'c': 'C'}
L11 = [k + '=' + v for k, v in L.items()]
print(L11)

# 把一个字符串中字符全部变成小写
L = ['Hello', 'World', 'Apple', 'Google']
L12 = [s.lower() for s in L]
print(L12)

print('----------  练习 ----------')
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L = ['Hello', 'World', 18, 'Apple', None]
#  [s.lower() for s in L]
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L13 = [s.lower() for s in L if isinstance(s, str)]


# 测试:
print(L13)
if L13 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

