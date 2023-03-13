import smtplib
from email.message import EmailMessage

email = EmailMessage()
sender_email = 'gauravbigdata9@gmail.com'
password = input('Enter your email\'s password: ')
email['from'] = 'Gaurav Kumar'
email['to'] = 'gauravkumar_776@yahoo.co.in'
email['subject'] = 'You are now a CTO of the company you want'

email.set_content('You are doing amazing things in life')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user=sender_email, password=password)
    smtp.send_message(email)
