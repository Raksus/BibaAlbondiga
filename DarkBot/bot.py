#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

#argfile = str(sys.argv[1])

config = ConfigParser.ConfigParser()
config.read("keys")

# Configurar claves
CONSUMER_KEY = Config.get("keys", "consumer_key")
CONSUMER_SECRET = Config.get("keys", "consumer_secret")
ACCESS_KEY = Config.get("keys", "access_key")
ACCESS_SECRET = Config.get("keys", "access_secret")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#filename=open(argfile, 'r')
#f=filename.readlines()
#filename.close()

to_favorite = api.user_timeline(id="Darkwolffff", count=100)

i = 0
for twit in to_favorite:
	i += 1
	try:
		api.destroy_favorite(twit.id)
		print twit.text
	except tweepy.TweepError as e:
		print e
print i
#while(True):
#	for line in f:
#		api.update_status(status=line)
#		time.sleep(3600)
