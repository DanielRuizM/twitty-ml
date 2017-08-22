import requests
import json
import oauth2 as oauth
import sys
from credentials import dev_credentials as cred
import psycopg2
import time
import datetime

if len(sys.argv) !=3:
    print("""
    You are introducing wrong parameters, you need:
        --  database_username database_password
    """)
    exit();


user_bbdd=sys.argv[1]
pass_bbdd=sys.argv[2]

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
dia = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
hora = datetime.datetime.fromtimestamp(ts).strftime('%H%M%S')
mesdia = datetime.datetime.fromtimestamp(ts).strftime('%m%d')
mes_anio =datetime.datetime.fromtimestamp(ts).strftime('%m_%Y')
dia_insert = datetime.datetime.fromtimestamp(ts).utcnow().strftime('%Y-%m-%d')
hora_insert = datetime.datetime.fromtimestamp(ts).utcnow().strftime('%H:%M:%S')
date_insert=dia_insert+' '+hora_insert

hoy =  datetime.datetime.fromtimestamp(ts).utcnow()
stt = st[:8]
print("ejecucion: "+str(hoy))

consumer = oauth.Consumer(key=cred.consumer_key, secret=cred.consumer_secret)
access_tokens = oauth.Token(key=cred.access_token, secret=cred.access_token_secret)
client = oauth.Client(consumer, access_tokens)


NorthKorea = "https://api.twitter.com/1.1/search/tweets.json?q=%23NorthKorea&src=tyah"
response, data = client.request(NorthKorea)
twits=requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%23NorthKorea&src=tyah')
inserts="insert into twits values "
tweets = json.loads(data)
tweet_statuses_array=tweets['statuses']
for tweet_dic in tweet_statuses_array:
        created_at=tweet_dic['created_at']
        if type(created_at)== 'NoneType':
            created_at='null'
        id=tweet_dic['id']
        if type(id)== 'NoneType':
            id='null'
        twit=(tweet_dic['text'])
        if type(twit)== 'NoneType':
            twit='null'
        entities=tweet_dic['entities']
        hashtags_array=entities['hashtags']
        hashtags_list=[]
        for hashtag in hashtags_array:
            hashtag=hashtag['text']
            hashtags_list.append(hashtag)
        if type(hashtags_list) =='NoneType':
            hashtags_list='null'

        user_dic=tweet_dic['user']

        user_id=user_dic['id']
        if type(user_id)== 'NoneType':
            user_id='null'
        user_name=user_dic['name']
        if type(user_name) == 'NoneType':
            user_name='null'
        user_location=user_dic['location']
        if type(user_location)== 'NoneType':
            user_location='null'
        user_screen_name=user_dic['screen_name']
        if type(user_screen_name) =='NoneType':
            user_screen_name='null'
        followers_count=user_dic['followers_count']
        if type(followers_count) =='NoneType':
            followers_count='null'
        friends_count=user_dic['friends_count'] 
        if type(friends_count) == 'NoneType':
            friends_count='null'
        favourites_count=user_dic['favourites_count'] 
        if type(favourites_count) == 'NoneType':
            favourites_count='null'
        #print("{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{}".format(str(created_at),str(id),str(twit),str(hashtags_list),str(user_id),str(user_name),str(user_location),str(user_screen_name),str(followers_count),str(friends_count),str(favourites_count)))
        insert="('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'),".format(str(created_at).replace("'",""),str(id).replace("'",""),str(twit).replace("'",""),str(hashtags_list).replace("'",""),str(user_id).replace("'",""),str(user_name).replace("'",""),str(user_location).replace("'",""),str(user_screen_name).replace("'",""),str(followers_count).replace("'",""),str(friends_count).replace("'",""),str(favourites_count).replace("'",""))
        inserts=inserts+insert
inserts=inserts[:-1]+';'
try:
    conn = psycopg2.connect("dbname=twitty user="+user_bbdd+" host=localhost password="+pass_bbdd)
    cur = conn.cursor()
    cur.execute(inserts)
    conn.commit()
except psycopg2.Error as e:
    print(str(e))
    print('Fallo en la conexion a postgres')
    sys.exit(1)




