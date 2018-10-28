"""
simple email module to send a preset email message from localhost
"""

from mgr_module import MgrModule
from email.mime.text import MIMEText
import smtplib
import email.utils
import errno
from config import recipient_email, send_from


class Email(MgrModule):
    COMMANDS = [
        {
            "cmd": "simplemail "
                   "name=recipient,type=CephString,req=false",
            "desc": "Sends preset email message",
            "perm": "r"
        },
    ]

    def handle_command(self, inbuf, cmd):
        sender = send_from
        if 'recipient' in cmd:
            send_to = cmd['recipient']
        else:
            send_to = recipient_email
        return self.send_email(send_to, sender)

    def send_email(self, to_addr, from_addr):
        msg = MIMEText("Don't worry, it's Ceph to start!")
        msg['To'] = to_addr
        msg['From'] = email.utils.formataddr(('Ceph Hello', from_addr))
        msg['Subject'] = 'Ceph Hello test message'

        server = smtplib.SMTP('localhost')

        try:
            to_addr_unpacked = to_addr.split(',')
            server.sendmail(from_addr, to_addr_unpacked, msg.as_string())
            return 0, '', 'Message sent successfully'

        except smtplib.SMTPRecipientsRefused as e:
            return e.errno, "", "Recipient refused"
        except smtplib.SMTPHeloError as e:
            return e.errno, "", "Remote server responded incorrectly"
        except smtplib.SMTPSenderRefused as e:
            return e.errno, "", "From address rejected by server"
        except smtplib.SMTPDataError as e:
            return e.errno, "", "An unknown data error occurred"

        finally:
            server.quit()

