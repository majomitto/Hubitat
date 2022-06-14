#!/usr/bin/python
import smtplib
import cgi
fs = cgi.FieldStorage()

sender_email = "xxxxxhub@gmail.com"
receiver_email = "xxxxx@gmail.com"
if "subject" not in fs or "body" not in fs:
  SUBJECT = "Default Subject"
  TEXT = "Default body text"
else:
  SUBJECT = fs["subject"].value
  TEXT = fs["body"].value

message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email,'<sender password>')
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
    print 'Email sent!'
except:
    print 'Something went wrong...'
