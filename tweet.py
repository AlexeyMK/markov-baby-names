from itertools import cycle
import os
from random import choice
import time

#this package seems outdated, but it was super simple to set up
import tweepy

import markovbaby

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY =  os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_KEY_SECRET')

DELAY = 60*60  # start with once an hour

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
boys_chain = markovbaby.create_chain('boys.txt')
girls_chain = markovbaby.create_chain('girls.txt')
chains = cycle([("boy's", boys_chain), ("girl's", girls_chain)])
messages = ["Thinking about a {gender} name? how about {name}?",
            "Looking for a {gender} name? why not {name}?",
            "Would {name} be a good {gender} name?",
            "How about {name} as a {gender} name?",
            "I know! {name} would make an awesome {gender} name."]

def send_tweet():
    gender, chain = chains.next()
    name = markovbaby.generate_name(chain)
    final_message = choice(messages).format(
        name=name,
        gender=gender
    )

    final_message+= " #babynameideas"

    try:
        print "trying to send: " + final_message
        print api.update_status(final_message)
    except Exception as e:
        #this will print to heroku logs
        print e

if __name__ == "__main__":
    while True:
        send_tweet() #Tweet! Tweet!
        time.sleep(DELAY) #Avoid Twitter rate limiting
