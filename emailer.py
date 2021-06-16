from os import environ
from email.mime.text import MIMEText
import smtplib

def example(address):
  username = environ["USERNAME"]
  password = environ["PASSWORD"]
  email_body = open("index.html").read()
  msg = MIMEText(email_body, 'html')
  msg['From'] = f"Test <{username}>"
  msg['To'] = address
  msg['Subject']  = "Test"
  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(username, password)
    smtp.send_message(msg)