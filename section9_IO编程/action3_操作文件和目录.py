# 操作文件和目录

# Python内置的os模块可以直接调用操作系统提供的接口函数

import os

# 获取操作系统类型
# 注:如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)  # 输出:posix

# 获取详细的系统信息
# 注:uname()在window系统中不提供
print(os.uname())
# 输出:posix.uname_result(sysname='Darwin', nodename='LiFengdeMacBook-Pro.local'
# , release='16.7.0', version='Darwin Kernel Version 16.7.0: Thu Jan 11 22:59:40 PST 2018;
# root:xnu-3789.73.8~1/RELEASE_X86_64', machine='x86_64')


# 环境变量
# 查看系统中定义的环境变量
print(os.environ)

# 获取某个环境变量保存的值:os.environ.get('path')
print(os.environ.get('SHELL'))  # 输出:/bin/bash
# 当找不到这个path时,则返回定义的默认值
print(os.environ.get('x', 'default'))

# 操作文件和目录
# 查看当前目录的绝对路径
print(os.path.abspath('.'))  # 输出:/Users/lifeng/Desktop/PythonWorkspace/section9_IO编程

# 在某个路径下创建新的目录 首先需要把新目录的完整路径表示出来
# 注:在进行路径拼接时,须使用os.path.join()  以正确处理不同操作系统的路径分隔符问题
testdirPath = os.path.join('/Users/lifeng/Desktop/PythonWorkspace', 'testdir')
print(testdirPath)  # 输出:/Users/lifeng/Desktop/PythonWorkspace/testdir

# 拆分路径:os.path.split()  后一部分总是最后级别的目录或文件名
print(os.path.split(testdirPath))  # 输出:('/Users/lifeng/Desktop/PythonWorkspace', 'testdir')

# 然后创建一个目录
# os.path.exists('path') 判断目录是否存在
if not os.path.exists(testdirPath):
    os.mkdir(testdirPath)

# 删除一个目录
if os.path.exists(testdirPath):
    os.rmdir('/Users/lifeng/Desktop/PythonWorkspace/testdir')

# 文件操作:

# 获取文件的路径名:os.path.splitext()
print(os.path.splitext('/Users/lifeng/Desktop/PythonWorkspace/section9_IO编程/test.txt'))
# 输出:('/Users/lifeng/Desktop/PythonWorkspace/section9_IO编程/test', '.txt')

# 判断文件是否存在
if os.path.exists('text1.py'):
    # 对文件重命名
    os.rename('text1.py', 'text1.py')
    # 删除文件
    os.remove('text1.py')

print('---------  分割线  ---------')
# 过滤文件:
# 1.首先列出当前目录下的所有文件
L = [x for x in os.listdir('.') if os.path.isfile(x)]
print(L)
# 输出:['__init__.py', 'action1_文件读写.py', 'action2_StringIO和BytesIO.py', 'action3_操作文件和目录.py', 'test.png', 'test.txt']

# 2.如要列出所有.py的文件
L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(L)  # 输出:['__init__.py', 'action1_文件读写.py', 'action2_StringIO和BytesIO.py', 'action3_操作文件和目录.py']
