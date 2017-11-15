import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'fj969421258@163.com'
msg['to'] = '3301257530@qq.com'
msg['subject'] = 'test'
content = "你好这是一封自动发送的邮件。"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
server = smtplib
server = smtplib.SMTP()
server.connect('smtp.163.com','25')
server.login('fj969421258@163.com','love74520')
server.sendmail('fj969421258@163.com','3301257530@qq.com',str(msg))
server.quit()