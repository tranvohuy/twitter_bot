import time
import sys
import tweepy
from datetime import date


# use this for production; set vars in heroku dashboard
from os import environ
Consumer_key= environ['Consumer_key']
CONSUMER_SECRET = environ['Consumer_secret']
Access_key = environ['Access_key']
Access_secret = environ['Access_secret']

#INTERVAL = 60 * 60 * 6  # tweet every 6 hours
 INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

while True:
    print("about to get ad...")
    #message = get_message()
    message = 'today is:' + date.today().isoformat()

    api.update_status(message)
    time.sleep(INTERVAL)
