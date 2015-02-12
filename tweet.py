import twitter
import random
import sys
import os
from local_settings import *
from markov import *

def connect():
    api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                          consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                          access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                          access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    return api

if __name__ == "__main__":
	chance = random.random()
	if chance > CHANCE:
		print "not tweeting this time: ", chance
		sys.exit()

	tries = 0

	while tries < MAX_TRIES:
		tries += 1

		tweet = markov()

		# Tweet is too long
		if len(tweet) > MAX_CHARACTERS:

			# Cap the length
			if CAP_LENGTH == True:
				tweet = tweet[:MAX_CHARACTERS]
			else:
				print "Tweet too long: " + str(len(tweet))
				continue

		if DEBUG == False:
			api = connect()
			status = api.PostUpdate(tweet)
			print status.text.encode('utf-8')    		
		else:
			print tweet

		sys.exit()