#import sys
import tweepy
from datetime import date


from os import environ
Consumer_key= environ['Consumer_key']
Consumer_secret = environ['Consumer_secret']
Access_key = environ['Access_key']
Access_secret = environ['Access_secret']



auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

if __name__=='__main__':
    print("about to update ststus...")
    #message = get_message()
    message = 'today is:' + date.today().isoformat()

    api.update_status(message)
