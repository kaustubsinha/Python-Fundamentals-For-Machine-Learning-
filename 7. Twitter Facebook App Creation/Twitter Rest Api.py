# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 23:19:23 2018

@author: Kaustub Sinha
"""
import oauth2
import time
import urllib.request  as urllib2 
import json

url1 = "https://api.twitter.com/1.1/search/tweets.json"

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }
consumer = oauth2.Consumer(key="TyMMcCUAmcvVteMFWiycc8De2", secret="8zgJNxtu6sp6YhfUDAxhf1leqWbTnythejqq1793S6uvilDBrh")
token = oauth2.Token(key="117302486-NrjqfbwlxZiFNULAfLq4lxrFMQEA9sAlM9LO3JYz",
                     secret="fFbqL02MrBusRkwj6Al4mcUmLLxiQApHirzIMwcF3kJoG")

params["oauth_consumer_key"] = consumer.key   # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key

params["q"] = "Jaipur"


req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))
print(data)

filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()