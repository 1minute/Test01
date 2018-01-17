import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
'''利用第三方登录发送邮件'''
my_sender = '15088132350@163.com'  # 发件人
my_pass = 'ASDFjkl123456789'  # 发件人密码(授权码)
my_user = '1113522924@qq.com'  # 收件人


def mail():
    ret = True
    try:
        msg = MIMEText('smtp 测试', 'plain', 'utf-8')
        msg['From'] = formataddr(['15088132350', my_sender])  # 发件人昵称，发件人邮箱
        msg['To'] = formataddr(['简凡', my_user])  # 收件人昵称，收件人邮箱
        msg['Subject'] = "Python发送邮件测试"

        server = smtplib.SMTP_SSL('smtp.163.com', 465)  # 发件人邮箱中SMTP服务器，端口默认是25
        server.login(my_sender, my_pass)  # 发件人邮箱账号密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 发件人邮箱账号，收件人账号(可以多个，用列表表示)，发送邮件

        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print('邮件发送成功')
else:
    print('邮件发送失败')
