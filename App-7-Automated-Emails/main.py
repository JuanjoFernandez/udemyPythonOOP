import yagmail
import pandas as pd
import datetime as dt
import time

from config import e_mail_user, e_mail_password
from news import NewsFeed

def send_email(today, yesterday, row):
    news_feed = NewsFeed(interest=row['interest'],
                                from_date=yesterday, 
                                to_date=today)
            
    email = yagmail.SMTP(user=e_mail_user, password = e_mail_password)
    email.send(to=row['email'], 
                    subject=f"Your {row['interest']} news for today!",
                    contents=f"Hi {row['name']}\n See what's on about {row['interest']} today.\n{news_feed.get()}JJ",)

while True:
    if dt.datetime.now().hour == 15 and dt.datetime.now().minute == 1:

        people = pd.read_excel('people.xlsx', usecols="A:D")
        people.dropna(inplace=True)

        today = dt.datetime.now().strftime('%Y-%m-%d')
        yesterday = (dt.datetime.now() - dt.timedelta(days=1)).strftime('%Y-%m-%d')

        for index, row in people.iterrows():
            send_email(today, yesterday, row)
    
    time.sleep(60)