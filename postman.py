#!/usr/bin/env python
# __author__ = 'cahitonur'

import smtplib
from email.mime.text import MIMEText


def send_mail(subject, message, sender, receiver):
    #fp = open(message, 'rb')
    msg = MIMEText(message)
    #fp.close()

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    s = smtplib.SMTP('localhost')
    s.sendmail(sender, [receiver], msg.as_string())
    s.quit()