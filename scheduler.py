import tweepy
from tweepy import Client
import time
from datetime import datetime
from dotenv import load_dotenv
import os


# load env. twitter credentials and tweepy auth
load_dotenv()

client = Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)


# try catch getting stuff with tweepy v2 (v1 didnt work)

try:
    user = client.get_me().data
    print("verified, you are:", user.username)
except:
    print("auth failed:")
    exit()




# post function 

def post_tweet(content):
   client.create_tweet(text=content)

# check with user 
def check_with_user(user):
    with open("tweet.txt", "r") as f:
        content = f.read()
        if not content:
            print("please write a tweet in tweet.txt")
            exit()

    print(f"{user.username} do you wanna tweet this?:\n")
    print(content)

    confirm = input("\n type 'yes' to post: ")
    if confirm == 'yes':
        print("the tweet will be posted (date)", )
        post_tweet(content)
    else:
        print("tweet cancelled")


check_with_user(user)