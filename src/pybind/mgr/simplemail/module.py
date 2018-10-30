"""
simple email module to send an email message from localhost
modification info at doc/mgr/simplemail.rst
"""

import smtplib
import errno
import json
import email.utils
from email.mime.text import MIMEText
from mgr_module import MgrModule
from simplemail.config import recipient_email, send_from


class Email(MgrModule):
    COMMANDS = [
        {
            "cmd": "simplemail "
                   "name=recipient,type=CephString,req=false",
            "desc": "Sends email message",
            "perm": "r"
        },
    ]

    def handle_command(self, inbuf, cmd):
        try:
            h = self.get('health')
            health_status = str(json.loads(h['json'])['status'])
        except:
            return -errno.EINVAL, "", "Health check returned an error"

        sender = send_from
        if 'recipient' in cmd:
            send_to = cmd['recipient']
        else:
            send_to = recipient_email

        return self.send_email(send_to, sender, health_status)

    def send_email(self, to_addr, from_addr, messg):
        msg = MIMEText("Ceph Health Alert = " + messg)
        msg['To'] = to_addr
        msg['From'] = email.utils.formataddr(('Ceph Hello', from_addr))
        msg['Subject'] = 'Ceph Hello test message'

        server = smtplib.SMTP('localhost')

        try:
            to_addr_unpacked = to_addr.split(',')
            server.sendmail(from_addr, to_addr_unpacked, msg.as_string())
            return 0, '', 'Message sent successfully'

        except smtplib.SMTPRecipientsRefused:
            return -errno.EINVAL, "", "Recipient address was refused"
        except smtplib.SMTPHeloError:
            return -errno.EINVAL, "", "Remote server responded incorrectly"
        except smtplib.SMTPSenderRefused:
            return -errno.EINVAL, "", "From address rejected by server"
        except smtplib.SMTPDataError:
            return -errno.EINVAL, "", "An unknown data error occurred"

        finally:
            server.quit()
