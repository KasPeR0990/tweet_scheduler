from datetime import datetime
from dotenv import load_dotenv
from tweepy import Client
import tweepy
import json
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

# try catch just for checking if authed tweepy v2 (v1 didnt work)
# catch exception 
try:
    user = client.get_me().data
    print(f"\nverified, you are: {user.username} \n")
except Exception as e:
    print("auth failed:", e)
    exit()


today = datetime.now()
print(f"it is {today} \n")


# post function 
def post_tweet(tweet):
   client.create_tweet(text=tweet)

# check with user 
def check_with_user():
    with open("tweets.json", "r") as f:
        tweets = json.load(f)
        if not tweets:
            print("please write a tweet in tweet.json")
            exit()

    print("what tweet do you wanna post?:\n")
    print(f"{tweets}\n")

    tweet_id = input("pick one: ")
    tweet = tweets.get(tweet_id)
    if not tweet:
        print("invalid selection")
        exit()

    print(f"\nyou picked: {tweet}")

    confirm = input("\n type 'yes' to post: ")
    if confirm == 'yes':
        print("the tweet will be posted (date)", )
        post_tweet(tweet)
    else:
        print("tweet cancelled")
    

check_with_user()