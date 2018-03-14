# 文件读写

# 读文件:使用python内置的open()函数  传入文件路径和标示符

# read():一次性读取全部内容 (文件很小时,可以使用此方式)
# read(size):每次读取size个字节的内容 (不能确定文件大小时,可以反复调用此方法进行读取)
# readline():可以每次读取一行内容
# readlines():一次性读取全部内容,并按行返回list   (如果是配置文件,使用此方式最方便)

# 文件读写 可能产生IOError
path = '/Users/lifeng/Desktop/PythonWorkspace/section9_IO编程/test.txt'

# 方式一:
try:
    f = open(path, 'r')
    # 如文件不存在 会抛出IO异常
    # 如读取成功,调用read()方法 可以一次性读取文件的全部内容
    print(f.read())  # 输出:Hello World!

finally:
    # 最后一步 调用close()方法关闭文件
    if f:
        f.close()

# 方式二:
# python引入with语句自动调用close()方法
with open(path, 'r') as f:
    print(f.read())  # 输出:Hello World!

# 方式三:
for line in open(path, 'r').readlines():
    # 删除末尾的'\n'
    print(line.strip())

# file-like object
# 定义:file-like object 不要求从特定类继承,只要写个read()方法就行.像open()函数返回的这种有个read()方法的对象


# 二进制文件
# 要读取二进制文件,例:图片、视频等 用'rb'模式打开文件即可
imagePath = '/Users/lifeng/Desktop/PythonWorkspace/section9_IO编程/test.png'
f = open(imagePath, 'rb')
print(f.read())  # 输出的结果以十六进制字节表示的
f.close()

# 字符编码
# 要读取非UTF-8编码的文件,需要给open()函数传入encoding参数
xlsxPath = '/Users/lifeng/Desktop/盈通集团员工信息资料统计表.xlsx'

# encoding='utf-8' 设置编码格式
# 当遇到编码错误时,最简单的方法是使用errors='ignore' 直接忽略
f = open(xlsxPath, 'r', encoding='utf-8', errors='ignore')
print(f.read())

# 写文件
# 写文件和读文件一样 两者之间的区别就是 写文件传入标示符'w'和'wb' 表示写文件或写二进制文件
f = open(path, 'w')
f.write('add text')
f.close()

# 用with来写
with open(path, 'w') as f:
    f.write('Hello world!')

