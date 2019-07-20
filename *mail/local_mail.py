from email.header import Header
from email.mime.text import MIMEText
import smtplib

# 邮件正文(纯文本形式), plain可以传图片.文件
message = MIMEText('python email test', 'plain', 'utf8')
# 邮件头部信息：发件人、收件人、主题
message['From'] = Header('root', 'utf8')
message['TO'] = Header('student', 'utf8')
message['Subject'] = Header('py test', 'utf8')

# 发邮件：邮件服务器、发件人、收件人
smtp = smtplib.SMTP('localhost')
sender = 'root'
receivers = ['root', 'student']
smtp.sendmail(sender, receivers, message.as_bytes())