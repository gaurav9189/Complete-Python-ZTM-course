import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text()).substitute(name='Gaurav')

# print(html)
email = EmailMessage()
sender_email = 'gauravbigdata9@gmail.com'
password = input('Enter your email\'s password: ')
email['from'] = 'Gaurav Kumar'
email['to'] = 'gauravkumar_776@yahoo.co.in'
email['subject'] = 'You have now completed the email exercise with Templates'
# Added the formatting and message contents
email.set_content(html, 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user=sender_email, password=password)
    smtp.send_message(email)
