# tweet

hey! built this simple tool just to learn a bit python today. 

i block social media with coldturkey but still want to post, so i made this script with tweepy. thinking of using cron to schedule it

## how to use this:

### 1. get your twitter api credentials

- go to https://developer.x.com and sign in
- create a new project (name it whatever you want)
- create an app within that project
- for app permissions, select "read and write"
- for callback url, enter "http://localhost/callback"
- for website url, enter any url (your github or just "http://localhost")
- in app settings > authentication settings > enable oauth 1.0a
- generate and save your api keys, bearer token, and access tokens
- copy all these values to your `.env` file (use `.env.example` as template)

### 2. install tweepy and dotenv
- pip3 install -r requirements.txt

### 2. set up your tweets

- add what you want to tweet to `tweet.txt`following the current structure

### 3. run the script

- run `python3 tweet.py` in terminal
- confirm when prompted
 

happy tweeting! 

notes to myself:
- make so that you can post media too 
- cron to schedule 
