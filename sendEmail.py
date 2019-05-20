#! usr/bin/env python3
#-*- coding:utf-8 -*-
import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
def readData(file_path):
    with open(file_path,'rb') as f:
        data = f.read()
    return data
#带附件邮件
def emailSend(sender,spwd,rec,file_path,smtpserver):
    msgatt = MIMEMultipart('related') #生成附件对象
    msgatt['subject'] = Header(u'请接收图片')#邮件主题
    msgatt['From'] = Header(sender,'utf-8')
    # msgatt['To'] = Header(rec,'utf-8')
    msgatt['To'] = ','.join(rec)#发送给多个用户
    msgatt.attach(MIMEText('带附件的邮件发送测试....','plain','utf-8'))#邮件正文
   #不带附件时
    # message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')#邮件正文
    # message['From'] = Header(sender, 'utf-8')
    # message['To'] = Header(rec, 'utf-8')
    # subject = 'Python SMTP 邮件测试'
    # message['Subject'] = Header(subject, 'utf-8')#邮件主题


    att = MIMEText(readData(file_path), 'base64', 'utf-8')#附件
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="test.png"'#附件的名称：test.png
    msgatt.attach(att)

    smtp = smtplib.SMTP(smtpserver,25)
    smtp.login(sender,spwd)
    smtp.sendmail(sender,rec,msgatt.as_string())
    smtp.quit()
if __name__ == '__main__':
    emailSend('18928861576@189.cn','lwy901123',['luowy@wdcloud.cc'],r'D:\test_prj\test_image\test001.png','smtp.189.cn')


