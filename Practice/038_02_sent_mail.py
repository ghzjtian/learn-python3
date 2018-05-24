#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

#带附件的邮件

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import parseaddr, formataddr

import smtplib


# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')




def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEMultipart('alternative')
#网易邮箱如果不加下面的配置，就会出现 •554 DT:SPM 错误,http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/tianzeng/Desktop/ScreenShot2018-05-24_09.44.32.png','rb') as f:
    ## 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image','png',filename='ScreenShot2018-05-24_09.44.32.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition','attachment',filename='ScreenShot2018-05-24_09.44.32.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#带 html 链接
#在正文中带图片
msgText = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8')

msg.attach(msgText)



server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.starttls()#创建了安全连接
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


