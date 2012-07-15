import os
import time

#this package seems outdated, but it was super simple to set up
import tweepy

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY =  os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_KEY_SECRET')

print CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

FOOTERS = ["#markovbaby"]
DELAY = 60*60  # start with once an hour

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def send_tweet(message):
    final_message = message
    #add in footers (hashtags and users)
    for footer in FOOTERS:
        if len(final_message + " " + footer) <= 140:
            final_message += " " + footer
    try:
        print "trying to send: " + final_message
        print api.update_status(final_message)
        # TODO AMK: debug this manually - does tweepy even work?
    except Exception as e:
        #this will print to heroku logs
        print e

if __name__ == "__main__":
    while True:
        tweet_text = 'Bobina' # temp
        send_tweet(tweet_text) #Tweet! Tweet!

        time.sleep(DELAY) #Avoid Twitter rate limiting
