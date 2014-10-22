#!/usr/bin/env python
# __author__ = 'cahitonur'

from subprocess import Popen, check_call, CalledProcessError
from postman import send_mail
import time

sender = 'monitor@example.com'
receiver = 'you@example.com'


def check_status():
    try:
        check_call(['lsof', '-i', ':3306'])

    except CalledProcessError:

        Popen(['service', 'mysql', 'start'])
        time.sleep(5)
        send_mail('MySql Server was down.', 'mail_text', sender, receiver)

if __name__ == '__main__':
    check_status()