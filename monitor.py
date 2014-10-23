#!/usr/bin/env python
# __author__ = 'cahitonur'

from subprocess import Popen, check_output, CalledProcessError, STDOUT
from postman import send_mail
import time

sender = 'monitor@example.com'
receiver = 'you@example.com'


def check_status():
    try:
        check_output(['lsof', '-i', ':3306'], stderr=STDOUT)

    except CalledProcessError:

        Popen(['service', 'mysql', 'start'])
        time.sleep(5)
        send_mail('MySql Server was down.', '/root/mysql_monitor/mail_text', sender, receiver)

if __name__ == '__main__':
    check_status()