# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:46:26 2018

@author: Kaustub Sinha
"""
"""
This Code is for Write On Twitter
"""

import tweepy
consumer_key = "YjuquFd0kj8ArCm4xKB31ZVpI"
consumer_secret = "W42RK6A8ffpXw7TNJ2rX05K2E59fAX2r0ZUa6O6qmbRuHLOizm"
access_token = "117302486-ajUTOecnUEBkYZhM6Zr9j1Ssd4lwCoasG3sRM4cX"
access_token_secret = "5qlZU0pckUknkfX2GaJjvON4wUoyup439iPjoUsEMUPJO"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status('Hello, This is Welcome from Python World')

"""
This Code is to read the Post from Twitter

"""

import tweepy
 
# Fill the X's with the credentials obtained by 
# following the above mentioned procedure.
consumer_key = "YjuquFd0kj8ArCm4xKB31ZVpI"
consumer_secret = "W42RK6A8ffpXw7TNJ2rX05K2E59fAX2r0ZUa6O6qmbRuHLOizm"
access_token = "117302486-ajUTOecnUEBkYZhM6Zr9j1Ssd4lwCoasG3sRM4cX"
access_token_secret = "5qlZU0pckUknkfX2GaJjvON4wUoyup439iPjoUsEMUPJO"
 
# Function to extract tweets
def get_tweets(username):
         
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
        tmp=[] 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
            tmp.append(j) 
        print(tmp)

if __name__ == '__main__':
    get_tweets("@kaustubsinha") 
    


