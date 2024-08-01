'''
Author: Ikarospoipoi 35780303ssy@gmail.com
Date: 2024-08-01 21:52:11
LastEditors: Ikarospoipoi 35780303ssy@gmail.com
LastEditTime: 2024-08-01 22:03:09
FilePath: /undefined/Users/ikaros/Desktop/untitled folder 3/News/news.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def get_news_headlines(api_key):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()
    headlines = []
    if news_data['status'] == 'ok':
        for article in news_data['articles']:
            headlines.append(article['title'])
    return headlines

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_pass):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

news_api_key = '357af2d9137442898715e4dc18943c99'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = '35780303ssy@gmail.com'
# This is a dummy password. I fail to send this message due to the security issue.
smtp_pass = '*********'
to_email = 'daniel@thefullwiki.org'
from_email = smtp_user


headlines = get_news_headlines(news_api_key)


subject = f"Today's News Headlines - {datetime.today().strftime('%Y-%m-%d')}"
body = '\n'.join(headlines)


send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_pass)

print('Email sent successfully!')
