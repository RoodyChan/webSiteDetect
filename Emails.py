#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Email_send(object):
 def __init__(self,msgTo,data2,Subject):
  self.msgTo=msgTo
  self.data2=data2
  self.Subject=Subject
 def sendEmail(self):
  # (attachment,html) = content
  msg = MIMEMultipart()
  msg['Subject'] = self.Subject
  msg['From'] = 'XXX'
  msg['To'] = self.msgTo
  html_att = MIMEText(self.data2, 'html', 'utf-8')
  #att = MIMEText(attachment, 'plain', 'utf-8')
  msg.attach(html_att)
  #msg.attach(att)
  try:
   smtp = smtplib.SMTP()
   smtp.connect('smtp.XXX.com', 25)
   smtp.login(msg['From'], '') #改成自己的邮箱密码
   smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
   return('邮件发送成功')
  except Exception as e:
   print('--------------sss------',e)
