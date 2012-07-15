import os
import time

from itertools import cycle
from random import choice
#this package seems outdated, but it was super simple to set up
import tweepy
from markovbaby import MarkovName


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY =  os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_KEY_SECRET')
DELAY = 60*60  # start with once an hour

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
boys_chain = MarkovName('boys.txt')
girls_chain = MarkovName('girls.txt')
chains = cycle([("boy's", boys_chain), ("girl's", girls_chain)])
messages = ["Thinking about a {gender} name? how about {name}? {tags}",
            "Looking for a {gender} name? why not {name}? {tags}",
            "Would {name} be a good {gender} name? {tags}",
            "How about {name} as a {gender} name? {tags}",
            "I know! {name} would make an awesome {gender} name. {tags}"]

def send_tweet():
  gender, chain = chains.next()
  # total overkill for 'find the first name between 3 and 14 characters)
  name = (n for n in iter(chain.generate_name, '') if 2 < len(n) < 15).next()
  final_message = choice(messages).format(
    name=name,
    gender=gender,
    tags="#babynameideas"
  )

  try:
    print "trying to send: " + final_message
    api.update_status(final_message)
  except Exception as e:
    print e  #this will print to heroku logs

if __name__ == "__main__":
  while True:
    send_tweet()
    time.sleep(DELAY)
