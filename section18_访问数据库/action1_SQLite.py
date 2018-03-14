# SQLite
# SQLite是一种嵌入式数据库 python内置了SQLite3
# SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用

# 表是数据库存放关系数据的集合,一个数据库中包含多个表.表与表之间通过外键关联
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

# 示例:
import sqlite3

# 连接到SQL数据库
# 如果文件不存在,会自动在当前目录创建
conn = sqlite3.connect('test.db')
# 创建一个cursor
curs = conn.cursor()
# 执行一个SQL语句  创建user表
curs.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY ,name VARCHAR(20))')

# 插入一条记录
curs.execute('INSERT INTO user (id,name) VALUES (\'1\',\'Michael\')')
# 获取插入的行数
print(curs.rowcount)  # 输出:1

# 执行查询语句
curs.execute('SELECT * FROM user WHERE id=?', ('1',))
# 获取查询结果集
print(curs.fetchall())  # 输出:[('1', 'Michael')]

# 如果SQL语句带有参数,需要将参数传给execute()方法,有几个?占位符就必须对应几个参数
# 例:cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

curs.close()
# 提交事务
conn.commit()
conn.close()
