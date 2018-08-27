from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from pymongo import MongoClient
from datetime import datetime


def insert_tweets():

    consumer_key = "RuDBYDBqgYXpuJhvsJyQ9Dd14"
    consumer_secret = "cfkV3RaD75vwDc46pH8BJ0oXVmc9myJ9IogOtu9fb3FrtW9rjJ"
    access_token = "701613212-M5xrNAFyU1k4u3LLQBNYba1jejs2SwYRZo9j4ym1"
    access_secret = "2a7lGBnSbe2RfxWivyXZVsSM303wd8QgjvVOygsiHf1PC"

    auth = OAuthHandler(consumer_key,consumer_secret)

    auth.set_access_token(access_token,access_secret)

    api = API(auth)

    client = MongoClient('localhost',27017)
    db = client['test-db']



    id_list = [
        {'T_id': '@BBhuttoZardari', 'party':'PPP','collection':'bbzardari'}, 
        {'T_id': '@ImranKhanPTI', 'party':'PTI','collection':'imrankhan'},
        {'T_id': '@Asad_Umar', 'party':'PTI','collection':'asadumar'},
        {'T_id': '@MaryamNSharif','party':'PMLN','collection':'maryamnawaz'},
        {'T_id': '@JahangirKTareen','party':'PTI','collection':'jahangirktareen'},
        {'T_id': '@sherryrehman','party':'PPP','collection':'sherryrehman'},
        {'T_id': '@ShireenMazari1','party':'PTI','collection':'shireenmazari'},
       ]

    
    for item in id_list:
        T_id = item['T_id']
        party = item['party']
        collection = item['collection']

        

        json_list = []

        print("getting tweets for " + T_id + "...")
        for tweet in Cursor(api.user_timeline, id = T_id,tweet_mode='extended').items(200):
            

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
            
        

        
        col_obj = db[collection]
        print("inserting into collection: "+ collection)



        for j_obj in json_list:
            col_obj.update({'_id':j_obj['_id']},j_obj,upsert=True)
            
