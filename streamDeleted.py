import sys
import os
import shutil
import string
import re
import json
import requests
from subprocess import PIPE, Popen
from datetime import datetime
from dateutil import tz
# from queue import Queue
from threading import Thread
import tweepy
from tweepy import OAuthHandler
import configparser
import urllib
from ttp import ttp

# Contants.



# Classes.

class Listener(tweepy.StreamListener):

    tweetCounter =  0 

    def on_status(self, status):

        Listener.tweetCounter = Listener.tweetCounter + 1
        print(Listener.tweetCounter)
        try:
            json_str = json.dumps(status._json)
            print "Status", json_str
            # t = "u\""+status.author.screen_name+"\""
            # # print("screen_name= "+t)
            # t = "u\""+status.text+"\""
            # # print("tweet=" +t)            
            # # print("screen_name= "+status.author.screen_name.encode('utf-8')+ " tweet=" +status.text.encode('utf-8'))
            # # tweets.append(status.text.encode("utf-8"))
            # print("calling vidDownload...")
            # vidDownload(status.text.encode("utf-8"))
            # print("Vid D done")
        except Exception as e: 
            print(str(e))
            pass    
        if Listener.tweetCounter < Listener.stopAt:
            return True
        else:
            print('maxnum = '+str(Listener.tweetCounter))
        return False
    def on_delete(self, status_id, user_id):
        print "Deleted",status_id
        print "Deleted",user_id
        """Called when a delete notice arrives for a status"""
        return        


def login():
    CONSUMER_KEY = 'laNbHK9rHTSN3VDjGjxKzGVlS'
    CONSUMER_SECRET = '75usGshLnyRxGBa1kmgIMHS2GDQrjBG3ENzuDqJ2poT6nDpwv5'
    ACCESS_TOKEN = '120044061-y5OLv9WBCCy810uq2TD7q9GqdZ15KoAYmEfGbvVc'
    ACCESS_TOKEN_SECRET = 'HaXtD7ZRZrKMMGPGglaeXGGCa7Dzw0HE3jZ1oZbRSE0qM'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth

def getTweetsByText(stopAtNumber):
    Listener.stopAt = stopAtNumber
    auth = login()
    streaming_api = tweepy.streaming.Stream(auth, Listener(), timeout=60)
    streaming_api.filter(track=["#abhademasam123"])
    # streaming_api.filter(track=["#periscope"])

def vidDownload(tweet):
    p = ttp.Parser()    
    try:
        r = p.parse(tweet.decode('utf-8'))
        # print(r.urls)
        for link in r.urls:
            # print link
            resp = urllib.request.urlopen(link)
            print(resp.url)
            if "https://www.periscope.tv/w/" in resp.url:
                process(resp.url)
    except Exception as e:
        print(str(e))
        pass 


if __name__ == "__main__":
    getTweetsByText(20)