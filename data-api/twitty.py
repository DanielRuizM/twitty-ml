import requests
import json
import oauth2 as oauth
import sys






if len(sys.argv) !=5:
    print("""
    You are introducing wrong parameters, you need:
        --  consumer_key consumer_secret access_token access_token_secret
    """)
    exit();

if len(sys.argv)==6:
	consumer_key=sys.argv[1]
	consumer_secret=sys.argv[2]
	access_token=sys.argv[3]
	access_token_secret=sys.argv[4]

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_tokens = oauth.Token(key=access_token, secret=access_token_secret)
client = oauth.Client(consumer, access_tokens)

NorthKorea = "https://api.twitter.com/1.1/search/tweets.json?q=%23NorthKorea&src=tyah"
response, data = client.request(timeline_endpoint)
twits=requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%23NorthKorea&src=tyah')
print(twits.json())
print(str(twits.text))

tweets = json.loads(data)
for tweet in tweets:
    print (tweet['text'])




if __name__ == "__main__":
  main()