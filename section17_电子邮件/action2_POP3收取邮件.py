# POP3收取邮件
# python内置poplib模块,实现了pop3协议,可以直接用来收邮件

# 示例:
# 通过POP3收取邮件
import poplib
from email.parser import Parser
from section17_电子邮件.action2_邮件解析 import print_info

emile = '515944954@qq.com'
password = 'ktucjbbbsolgcacf'
pop3_server = 'pop.qq.com'

# 连接到pop3服务器
# server = poplib.POP3(pop3_server)
# 注:如报poplib.error_proto: b'-ERR Login fail. A secure connection is requiered(such as ssl)
# 表示需要一个安全连接 则使用POP3_SSL()进行连接 不使用POP3()连接
server = poplib.POP3_SSL(pop3_server)

server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(emile)
server.pass_(password)

# stat():返回邮件数量和占用空间
print('Messages:%s.Size:%s' % server.stat())
# list():返回所有邮件的编号
resp, mails, octets = server.list()
print(mails)

# 获取最新一封邮件,索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')

# 解析邮件:
msg = Parser().parsestr(msg_content)
print_info(msg)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)

# 关闭连接:
server.quit()
