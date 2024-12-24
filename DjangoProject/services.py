import smtplib
from email.mime.text import MIMEText

from django.shortcuts import render
from django.template.loader import render_to_string

from DjangoProject.settings import EMAIL_HOST_USER, EMAIL_PORT, EMAIL_HOST_PASSWORD, EMAIL_HOST


def send_email(html_template, subject, to_email, context=None):
    to_email = [to_email]
    html_massage = render_to_string(html_template, context)

    msg =MIMEText(html_massage, 'html')
    msg['Subject'] = subject
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = ', '.join(to_email)

    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as smtp_server:
        smtp_server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtp_server.sendmail(EMAIL_HOST_USER, to_email, msg.as_string())
    print("Massage sent")