__author__ = "Jader Gabriel\n"
__copyright__ = "\nCopyright 2013\n"
__tags__ = ["Unimontes", "CCET", "DCC",
            "NOME DA DISCIPLINA", "Prfº: NOME DO PROFESSOR"]
__license__ = "GPL"
__email__ = "programacaoeti@outlook.com\n"
__status__ = "\nTrabalho NRO DO TRABALHO\n"
_data__ = '12/03/14'
#!/usr/bin/python
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
password = ''
sender = ''
recipient = ''
subject = 'Gmail SMTP Test'
body = 'blah blah blah'

"Sends an e-mail to the specified recipient."

body = "" + body + ""

headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)

session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()