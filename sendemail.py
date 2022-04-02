import smtplib
import json
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

os.system('cls')

with open('server.json', 'r') as f:
    server = json.load(f)

login = server['login']
password = server['password']

server = smtplib.SMTP(server['host'], server['port'])
server.ehlo()
server.starttls()
server.login(login, password)

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = ''
email_msg['Subject'] = 'I love PYTHON <3'

email_msg.attach(MIMEText('Hello, World! <br> Is just a test sending email with <b>python</b>. \
                          <br> I sent a file too.', 'html'))

attachment = open('file.pdf', 'rb')
att = MIMEBase('application', 'octect-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition', f'attachment; filename=file.pdf')
attachment.close()

email_msg.attach(att)
try:
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.quit()
    print('Email successfully sent.')
except Exception as e:
    print(f'ERROR: {e}')
