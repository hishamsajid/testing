from flask import Flask

app = Flask(__name__)

from app import routes

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time
import atexit

from app.static.scripts.insert_tweets import insert_tweets


def demo():
    print('cron works')

scheduler = BackgroundScheduler()

scheduler.add_job(insert_tweets,
                  'cron', 
                   day_of_week='mon-sun', 
                   hour=10,
                   minute=35)


scheduler.start()

atexit.register(lambda:scheduler.shutdown())

if __name__ == '__main__':
    app.run()