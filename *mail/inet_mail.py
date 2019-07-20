#连接邮箱发送邮件

from email.header import Header
from email.mime.text import MIMEText
import smtplib
import getpass

def send_mail(host, password, sender, receivers, body, subject):
    msg = MIMEText(body, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(receivers[0], 'Utf8')
    msg['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, receivers, msg.as_bytes())

if __name__ == '__main__':
    sender = 'xxx@163.com'   #发件人
    receivers = ['xxx.com','xxx.com']  #收件人
    server = 'smtp.163.com'    #邮箱协议
    password = getpass.getpass()
    body = 'Hello from python.\n你好'
    subject = 'py mail test'
    send_mail(server, password, sender, receivers, body, subject)
