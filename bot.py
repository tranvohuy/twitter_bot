#import sys
import tweepy
from datetime import date
from messages import get_message
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials


from os import environ
Consumer_key= environ['Consumer_key']
Consumer_secret = environ['Consumer_secret']
Access_key = environ['Access_key']
Access_secret = environ['Access_secret']

json_cred = envirion['google_cred']


auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

scopes = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict=json_cred, scopes=scopes)
gc = gspread.authorize(creds)


if __name__=='__main__':
    
    message = get_message()

    print("about to update status...")
    api.update_status(message)
