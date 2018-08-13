from flask import render_template, Response
from flask_pymongo import PyMongo
from app import app

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

# from backend.gettweets import get_tweets
# from backend.idlist import id_list


from app.static.scripts.gettweets import get_tweets
from app.static.scripts.idlist import id_list
consumer_key = "RuDBYDBqgYXpuJhvsJyQ9Dd14"
consumer_secret = "cfkV3RaD75vwDc46pH8BJ0oXVmc9myJ9IogOtu9fb3FrtW9rjJ"
access_token = "701613212-M5xrNAFyU1k4u3LLQBNYba1jejs2SwYRZo9j4ym1"
access_secret = "2a7lGBnSbe2RfxWivyXZVsSM303wd8QgjvVOygsiHf1PC"


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
    return render_template('index.html')

@app.route('/index_2')
def index_2():
    return render_template('index2.html')


@app.route('/getUsersTweets')
def getUsersTweets():
    return render_template('users.html',id_list=id_list)


@app.route('/getAsad')
def getAsad():
    table_df = get_tweets('asadumar')
    csv = table_df.to_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=asadUmar.csv"})

@app.route('/getImran')
def getImran():
    table_df = get_tweets('imrankhan')
    csv = table_df.to_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=imranKhan.csv"})

@app.route('/getBBzardari')
def getBBzardari():
    table_df = get_tweets('bbzardari')
    csv = table_df.to_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=bbZardari.csv"})
@app.route('/getMaryam')
def getMaryam():
    table_df = get_tweets('maryamnawaz')
    csv = table_df.to_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=maryamNawazSharif.csv"})

@app.route('/getJKT')
def getJKT():
    table_df = get_tweets('jahangirktareen')
    csv = table_df.to_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=JKT.csv"})
   
@app.route('/getSherry')
def getSherry():
    table_df = get_tweets('sherryrehman')
    csv = table_df.to_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=sherryRehman.csv"})

@app.route('/getShireen')
def getShireen():
    table_df = get_tweets('shireenmazari')
    csv = table_df.to_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=shireenMazari.csv"})
