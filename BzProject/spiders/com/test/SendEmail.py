# # -*- coding: utf-8 -*-
# import smtplib
# from email.mime.text import MIMEText
#
# msg_from='1346024431@qq.com'
# pwd='nrxkjykvavoyihha'
# msg_to='625201089@qq.com'
# title="python 测试"
# content="测试qq邮箱"
# msg=MIMEText(content)
# msg['Subject']=title
# msg['From']=msg_from
# msg['To']=msg_to
# try:
#     s=smtplib.SMTP_SSL("smtp.163.com",465)#
#     s.login(msg_from,pwd)
#     s.sendmail(msg_from,msg_to,msg.as_string())
#     print("发送成功")
# except Exception as e:
#     print(e)
