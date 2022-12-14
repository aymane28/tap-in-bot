import tweepy
import configparser
import pandas as pd
import csv
from colorama import Fore, Back, Style
from difflib import SequenceMatcher


# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#api.update_status('Twitter bot in live')

tweets = api.mentions_timeline()



#for tweet in tweets:
#    print(str(tweet.id) + '-' + tweet.user.name + '-'+ tweet.text)

# user tweets
user = tweets[0].user.screen_name
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# create dataframe
columns = ['User', 'Tweet']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])
    if(similar(tweet.full_text, tweet.full_text)):
    #if('folicule' in tweet.full_text):
        val = True
        print("Le tweet ressemble fortement à:", end=" ") ; print(Fore.BLUE + tweet.full_text) ; print(Style.RESET_ALL)
        print(status.text)
        break
    else:
        val = False

df = pd.DataFrame(data, columns=columns)

if(val == True):
    print(Fore.MAGENTA + "Le tweet a déjà été écrit sur ce profile !") ; print(Style.RESET_ALL)
else:
    print("Le tweet n'a jamais étét écrit sur ce profile !") ; print(Style.RESET_ALL)




