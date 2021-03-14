#!/usr/local/bin/python3

import tweepy
import datetime
import json

confPath = "./sweepstakes.conf"

# Make the text
endDate = datetime.date(2023, 7, 17)
today = datetime.date.today()
daysLeft = (endDate - today).days
tweetText = "There are %d days left in Michael Hancock's term." % daysLeft

# Get auth
conf = {}
with open(confPath, "r") as inF:
    conf = json.loads(inF.read())

# Send the tweet
consumer_key = conf["api"]["key"]
consumer_secret = conf["api"]["secret"]
access_token = conf["access"]["token"]
access_token_secret = conf["access"]["secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(tweetText)
