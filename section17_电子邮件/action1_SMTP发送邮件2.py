from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.utils import parseaddr, formataddr


# 创建一个发送附件的邮件

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_emile = '515944954@qq.com'
password = 'ktucjbbbsolgcacf'
to_emile = 'return91@163.com'
server = smtplib.SMTP('smtp.qq.com', 587)

# 构建邮件对象
msg = MIMEMultipart()

msg['From'] = _format_addr('Python爱好者<%s>' % from_emile)
msg['To'] = _format_addr('管理员<%s>' % to_emile)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# 设置邮件正文

# 发送附件形式发送邮件
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# ------------------------------------
# 发送图片(将图片嵌入到邮件内容中):
# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后
# ，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
# 把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片

# ------------------------------------
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#                     '<p><img src="cid:0"></p>' +
#                     '</body></html>', 'html', 'utf-8'))

# ------------------------------------
# 同时支持Html和Plain格式
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/lifeng/Desktop/PythonWorkspace/section13_常用第三方模块/test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名,这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server.set_debuglevel(1)
server.starttls()
server.login(from_emile, password)
server.sendmail(from_emile, [to_emile], msg.as_string())
server.quit()
