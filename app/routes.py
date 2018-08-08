from flask import render_template
from flask_pymongo import PyMongo
from app import app

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

consumer_key = "RuDBYDBqgYXpuJhvsJyQ9Dd14"
consumer_secret = "cfkV3RaD75vwDc46pH8BJ0oXVmc9myJ9IogOtu9fb3FrtW9rjJ"
access_token = "701613212-M5xrNAFyU1k4u3LLQBNYba1jejs2SwYRZo9j4ym1"
access_secret = "2a7lGBnSbe2RfxWivyXZVsSM303wd8QgjvVOygsiHf1PC"

id_list = [
    {'T_id': '@BBhuttoZardari', 'party':'PPP','collection':'bbzardari'}, 
    {'T_id': '@ImranKhanPTI', 'party':'PTI','collection':'imrankhan'},
    {'T_id': '@Asad_Umar', 'party':'PTI','collection':'asadumar'},
    {'T_id': '@MaryamNSharif','party':'PMLN','collection':'marymanawaz'},

    ]

# app.config['MONGO_DBNAME'] = 'samaa-db-twitter-dev'

# app.config['MONGO_URI'] = 'mongodb://admin:admin123@ds215822.mlab.com:15822/samaa-db-twitter-dev'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test-db'
app.config['MONGO_DBNAME'] = 'test-db'

mongo = PyMongo(app)
# print(mongo_client)
# print(db)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/getTweets')
def getTweets():
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api = API(auth)
    
    for item in id_list:

        T_id = item['T_id']
        party = item['party']
        collection = item['collection']
        json_list = []

        print("getting tweets for " + T_id + "...")
        for tweet in Cursor(api.user_timeline, id = T_id,tweet_mode='extended').items(3200):
            

            tweet_json = {

            'user_name': tweet.user.screen_name,
            'party': party,
            'tweet_text': tweet.full_text,
            'location': tweet.user.location,
            'created_at': tweet.created_at,
            'favourites_count': tweet.favorite_count,
            'retweets':tweet.retweet_count,
            'followers_count': tweet.user.followers_count,
            'verified': tweet.user.verified,
            '_id': tweet.id
            }

            json_list.append(tweet_json)

            coll_obj = mongo.db.collection
            print("inserting into collection: "+ collection)

            for j_obj in json_list:
                return_text =  coll_obj.update({'_id':j_obj['_id']},j_obj,upsert=True)
                return str(return_text)


