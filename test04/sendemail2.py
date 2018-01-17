import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formataddr
from email.header import Header
from email import encoders

'''发送附件'''
my_sender = '15088132350@163.com'  # 发件人
my_pass = 'ASDFjkl123456789'  # 发件人密码(授权码)

# 邮件对象
msg = MIMEMultipart()
msg['From'] = formataddr(['大佬', my_sender])
msg['To'] = formataddr(['小弟', '1113522924@qq.com'])
msg['Subject'] = Header('发一张图片', 'utf-8').encode()

# 邮件正文是MIMEText
msg.attach(MIMEText('哈哈', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('D:/pythonTest/photo/photo24.png','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型
    mime = MIMEBase('image', 'png', filename='photo24.png')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='photo24.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

try:
    server = smtplib.SMTP_SSL('smtp.163.com', 465)
    server.login(my_sender, my_pass)
    server.sendmail(my_sender, ["1113522924@qq.com", "2776839490@qq.com"], msg.as_string())
    print('发送邮件成功')
except Exception:
    print('发送失败')
