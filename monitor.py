#!/usr/bin/env python
# __author__ = 'cahitonur'

from subprocess import Popen, PIPE
from postman import send_mail
import time

sender = 'monitor@example.com'
receiver = 'you@example.com'


def check_status():
    c1 = Popen(['ps', 'au'], stdout=PIPE)
    c2 = Popen(['grep', 'mysql'], stdin=c1.stdout, stdout=PIPE)

    c1.stdout.close()
    output, err = c2.communicate()

    if output:
        pass
    else:
        try:
            Popen(['service', 'mysql', 'start'])
            time.sleep(5)
            send_mail('MySql Server was down.', 'mail_text', sender, receiver)
        except Exception as e:
            raise e


if __name__ == '__main__':
    check_status()