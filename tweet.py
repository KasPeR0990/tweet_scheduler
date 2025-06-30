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

    choice = input("\nDo you want to (1) post now or (2) schedule for later? Enter 1 or 2: ")
    if choice == "1":   
        confirm = input("\nType 'yes' to post now: ")
        if confirm == 'yes':
            print("posting now...", )
            post_tweet(tweet)
            print("tweeted")
        else:
            print("tweet cancelled")
    elif choice == "2":
        schedule_date = input("\nEnter date and time to post (format: YYYY-MM-DD HH:MM): ")

        with open("scheduled_tweet.txt", "w") as f:
            f.write(f"{schedule_date}|{tweet}")
        
        print(f"\nTweet scheduled for {schedule_date}")
                    
if __name__ == "__main__":
    check_with_user() 