import configparser
import tweepy
import json
from pprint import pprint
import os


from dotenv import load_dotenv, find_dotenv
load_dotenv()  # take environment variables from .env.
##https://stackoverflow.com/questions/65401324/python-error-modulenotfounderror-no-module-named-dotenv
##



api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user_name = 'BleepinComputer'
tweets = api.user_timeline(screen_name=user_name, count=5)

counter = 0
for i in tweets:
    print("\n\n-----------------------------------------------------------\nTweet #%s\n-----------------------------------------------------------" % counter)
    minimalTitleText = i.text
    expanded_url = i.entities["urls"][0]["expanded_url"]
    createdDate = i._json["created_at"]
    
#    pprint(vars(i))
    
    print(createdDate)
    print(minimalTitleText)
    print(expanded_url)
    counter = counter + 1
