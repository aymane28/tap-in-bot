import tweepy
import configparser
import pandas as pd
import csv
from colorama import Fore, Back, Style


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
print("Le bot est appelé par:", end=" ") ; print( Fore.RED + tweets[0].user.screen_name) ; print(Style.RESET_ALL)
print("Le contenu du tweet:", end=" ") ; print(Fore.GREEN+ tweets[0].text) ; print(Style.RESET_ALL)
#print(str(tweets[0].id) + '-----' + tweets[0].text  + '-----' + tweets[0].user.screen_name)



#for tweet in tweets:
#    print(str(tweet.id) + '-' + tweet.user.name + '-'+ tweet.text)

# user tweets
user = tweets[0].user.screen_name
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# create dataframe
columns = ['User', 'Tweet']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])
    if('folicule' in tweet.full_text):
        val = True
        print("Le tweet ressemble fortement à:", end=" ") ; print(Fore.BLUE + tweet.full_text) ; print(Style.RESET_ALL)
        break
    else:
        val = False

df = pd.DataFrame(data, columns=columns)

if(val == True):
    print(Fore.MAGENTA + "Le tweet a déjà été écrit sur ce profile !") ; print(Style.RESET_ALL)
else:
    print("Le tweet n'a jamais étét écrit sur ce profile !") ; print(Style.RESET_ALL)




