# MySQL 是为服务端设计的数据库,能承受高并发访问,同时占用的内存远大于SQLite
# MySQL 内部有多种数据库引擎,最常用的引擎是支持数据库事务的InnoDB

# 示例:

# 1.导入mysql驱动
import mysql.connector
# mysql修改密码cmd命令:
# 　　mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass');
conn = mysql.connector.connect(user='root', password='123456', database='aa')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
# 关闭Cursor和Connection:
cursor.close()
