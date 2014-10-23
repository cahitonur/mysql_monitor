#!/usr/bin/env python
# __author__ = 'cahitonur'

import time
import subprocess
from postman import send_mail


sender = 'monitor@example.com'
receiver = 'you@example.com'
subject = 'MySql Server was down..'
message = '..and started automatically @'


def check_status():

    try:
        subprocess.check_output(['lsof', '-i', ':3306'], stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError:

        subprocess.Popen(['service', 'mysql', 'start'])
        msg = message + time.ctime()
        time.sleep(5)
        send_mail(subject, msg, sender, receiver)

if __name__ == '__main__':
    check_status()