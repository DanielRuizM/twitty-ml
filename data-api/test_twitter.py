import requests
import json
import oauth2 as oauth
import sys
from credentials import dev_credentials as cred

'''
if len(sys.argv) !=5:
    print("""
    You are introducing wrong parameters, you need:
        --  consumer_key consumer_secret access_token access_token_secret
    """)
    exit();
'''

consumer = oauth.Consumer(key=cred.consumer_key, secret=cred.consumer_secret)
access_tokens = oauth.Token(key=cred.access_token, secret=cred.access_token_secret)
client = oauth.Client(consumer, access_tokens)


NorthKorea = "https://api.twitter.com/1.1/search/tweets.json?q=%23NorthKorea&src=tyah"
response, data = client.request(NorthKorea)
twits=requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%23NorthKorea&src=tyah')
#print(twits.json())
#print(str(twits.text))

tweets = json.loads(data)
#print(tweets)
tweet_statuses_array=tweets['statuses']
for tweet_dic in tweet_statuses_array:
        #print(tweet_dic)
        print(tweet_dic['text'])
        



