# this file is running with cron every minute 
from tweet import post_tweet
from datetime import datetime


# WIP

def schedule_tweet():
    try:
        with open("scheduled_tweet.txt", "r") as f:
            content = f.read().strip()

        parts = content.split("|")
        print(parts)
    except FileNotFoundError:
        print("no scheduled tweets found")

schedule_tweet()