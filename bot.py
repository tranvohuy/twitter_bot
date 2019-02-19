import time
import sys
import tweepy
from datetime import date

#from generate_advertisement import update_Craiglist

# from credentials import *  # use this one for testing

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

#INTERVAL = 60 * 60 * 6  # tweet every 6 hours
 INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    print("about to get ad...")
    #message = get_message()
    message = 'today is:' + date.today().isoformat()

    api.update_status(message)
    time.sleep(INTERVAL)
