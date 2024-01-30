# sendmail.py
# author: Andrew Beatty
# sends an email via gmail

import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

subject = "Email Subject"
body = "This is the body of the text message"
sender = "andrewbeattycourse@gmail.com"
recipients = ["andrew.beatty@atu.ie"]
password = "cnkkmvamlcbjsknl"



send_email(subject, body, sender, recipients, password)
