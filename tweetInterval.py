#!/usr/bin/env python

import api
import tweepy
import ConfigParser
import os
import time

#Twittea uno de los mensajes cada periodo segundos
def tweetPeriodico(user, periodo, frases):
	frases = ''.join(ch for ch in frases if ch != '\n')
	frases = frases.split(',')
	for frase in frases:
		twittear("@" + user + " " + frase)
		time.sleep(periodo)
			

#Intenta twitear un mensaje
def twittear(mensaje):
	try:
		print("twitea")
		print(mensaje)
		#api.update_status(status=mensaje)
	except:
		print(":C")






twitter = api.getApi()

config = ConfigParser.ConfigParser()
config.read("frasesbot.conf")

tweetPeriodico("moonage180", float(config.get("moonage180","periodo")), config.get("moonage180","frases"))

exit (0)

for user in config.sections():
	print (user)
	newpid = os.fork()
	
	if newpid == 0:
		if config.get(user,"periodo") == None:
			tweetPeriodico(user, float(config.get(user,"periodo")), config.get(user,"frases"))
		else:
			print("TODO")
	else:
		continue

