import requests
import json
import oauth2 as oauth
import sys
import credentials.dev_credentials as cred

if len(sys.argv) !=5:
    print("""
    You are introducing wrong parameters, you need:
        --  consumer_key consumer_secret access_token access_token_secret
    """)
    exit();

class TwitterSession(object):
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def add(self):
        self.x.append(1)

    def login(self):
        consumer = oauth.Consumer(key=self.consumer_key, secret=self.consumer_secret)
        access_tokens = oauth.Token(key=self.access_token, secret=self.access_token_secret)
        client = oauth.Client(consumer, access_tokens)
        return client



def main():

    twity=TwitterSession(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    ouath_client=twity.login()

    NorthKorea = "https://api.twitter.com/1.1/search/tweets.json?q=%23NorthKorea&src=tyah"
    response, data = ouath_client.request(NorthKorea)

    tweets = json.loads(data)
    #print(tweets)
    for tweet in tweets:
        print (tweet)



if __name__ == "__main__":
    main()






