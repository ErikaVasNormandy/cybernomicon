#############################################################################
# Twitter Python API Practice
#### Tutorial Used: https://blog.quantinsti.com/python-twitter-api/
#############################################################################

#############################################################################
# 0. Import Libraries
# > pip3 install tweepy
#############################################################################
import tweepy
import json
import os
from pprint import pprint
   ## pprint(vars(response))
from dotenv import load_dotenv, find_dotenv
load_dotenv()  # take environment variables from .env.

#############################################################################
# 1. Authenticate Using os, .env, and Twitter API credential
#############################################################################

api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#############################################################################
# Original authentication (didn't work for me, but I didn't delve deeply into configparser
#############################################################################
#original
# Read the values
#config = configparser.ConfigParser()
#config.read('config.ini')

#api_key = config['twitter']['api_key']
#api_key_secret = config['twitter']['api_key_secret']
#access_token = config['twitter']['access_token']
#access_token_secret = config['twitter']['access_token_secret']



def getUserNameFromID():
    print("\n---------------------------------------------------------------------------------------------------------- \nGet A Username from an ID Tweets\n---------------------------------------------------------------------------------------------------------- \n")
    put_your_user_id = "869660137"
    user1 = api.get_user(user_id = put_your_user_id)
    print(user1.name)
    # Output: 'QuantInsti'

def getIDFromUserName():
    print("\n---------------------------------------------------------------------------------------------------------- \nGet an ID from a Username Tweets\n---------------------------------------------------------------------------------------------------------- \n")
    put_your_screen_name = "quantinsti"
    user2 = api.get_user(screen_name=put_your_screen_name)
    print(user2.id)
    # Output: 869660137
    
def GetYourOwnTweets():
    print("\n---------------------------------------------------------------------------------------------------------- \nGet Your Own Tweets Tweets\n---------------------------------------------------------------------------------------------------------- \n")
    public_tweets = api.home_timeline()
    print(public_tweets)
    
def GetAnotherUsersTweets():
    #returns an array of this users tweets
    print("\n---------------------------------------------------------------------------------------------------------- \nGet Another Users Tweets\n---------------------------------------------------------------------------------------------------------- \n")
    user_name = 'BleepinComputer'
    #####get 4 tweeets from this user
    tweets = api.user_timeline(screen_name=user_name, count=4)
#    print(tweets)
#    pprint(vars(tweets))
    return tweets
    # In case you want to save this data to a csv file
    #df.to_csv('public_tweets.csv')

def jsonStuff(tweetsInput):
    print("\n---------------------------------------------------------------------------------------------------------- \nUnravel an Individual Tweet\n---------------------------------------------------------------------------------------------------------- \n")
    FirstTweetMinimum = tweetsInput[0]
    counter = 0
    pprint(vars(FirstTweetMinimum))
    
################################################## print(json_data ( entities)

#print("json_entities-------------------------------------------------------------------")
#for k, v in json_data.items():
#    print(k, v)
    
#tweetscontent_json_entities = json_data["entities"]
#print("we now have a dictionary object out of entities -----------------------------------------------------------------------------------------------------------------")
#print(tweetscontent_json_entities)
#
#print(tweetscontent_json_entities["urls"])
#
#tweetscontent_json_entities_urls = tweetscontent_json_entities["urls"]
#
##torrenting - they can get your ids
##usenet - only the servers

#print("\n\nexpanded url is ", tweetscontent_json_entities_urls[0]["expanded_url"])

#
#print("\n\n\n\n\n\printing tweets content -------------------------------------------------------------------------------------------------------")
##pprint(vars(tweetscontent))
#print(tweetscontent._json["text"])
#print("\n\n\n\n\n\ -------------------------------------------------------------------------------------------------------")
#
#print(len(tweets))


def main():
#    getUserNameFromID
#    GetYourOwnTweets()
#    getIDFromUserName()
    heartbeat = GetAnotherUsersTweets()
    jsonStuff(heartbeat)

if __name__ == "__main__":
    main()
