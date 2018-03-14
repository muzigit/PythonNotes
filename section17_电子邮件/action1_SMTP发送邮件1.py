# SMTP发送邮件
# SMTP是发送邮件的协议,可以发送纯文本/html/带附件的邮件  python内置对SMTP的支持

# python对SMTP支持有smtplib 和 email两个模块,email负责构建邮件,smtplib负责发送邮件
from email.header import Header
from email.mime.text import MIMEText
import smtplib

# 注意事项:
# QQ邮箱:
# 接收邮件服务器：imap.qq.com，使用SSL，端口号993
# 发送邮件服务器：smtp.qq.com，使用SSL，端口号465或587
# 如使用QQ邮箱登录SMTP服务器,使用的password是QQ邮箱的授权码(授权码获取方法参考:http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256)
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 构建一个简单的纯文本邮件
# 参数说明: 1.邮件正文  2.MIME的subtype,plain表示纯文本类型
# msg = MIMEText('hello,send by python...', 'plain', 'utf-8')

# 发送Html邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')

# Emile 和 口令
from_emile = '515944954@qq.com'
password = 'ktucjbbbsolgcacf'  # 515944954@qq.com邮箱授权码

# 收件人地址
to_emile = 'return91@163.com'

# SMTP服务器地址
server = smtplib.SMTP('smtp.qq.com', 587)

# 设置发件人
msg['From'] = _format_addr('Python爱好者<%s>' % from_emile)
# 设置收件人
msg['To'] = _format_addr('管理员<%s>' % to_emile)
# 设置主题
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# set_debuglevel()可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)

# 创建安全连接
# 注:如未加此代码  报:SMTPAuthenticationError: (530, b'Must issue a STARTTLS command first.')
server.starttls()

# 登录smtp服务器
server.login(from_emile, password)
# as_string() 把MIMEText对象变成str
server.sendmail(from_emile, [to_emile], msg.as_string())
server.quit()
