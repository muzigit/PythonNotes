# 循环

# for...in...循环

names = ['Michael','Bob','Tracy']
for name in names:
    print(name)

# 计算1-10的整数之和
num = 0
for i in[1,2,3,4,5,6,7,8,9,10]:
    num = num + i
print(num)

# range():可以生成一个整数序列  list():可以转换成list

# 生成从0开始 小于5的整数序列
r = range(5)
print(r)
l = list(r)
print(l)


# while...循环


# 计算100以内奇数之和
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)


# 练习:
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for name in  L:
    print('Hello,%s!'%name)
