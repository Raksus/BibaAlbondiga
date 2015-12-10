#!/usr/bin/env python

import api
import tweepy
import ConfigParser
import os
from time import sleep
from datetime import datetime, time

 #Intenta twitear un mensaje
def twittear(mensaje):
	try:
		print("twitea")
		print(mensaje)
		twitter.update_status(status=mensaje)
	except tweepy.TweepError as e:
		print(e)



#Twittea uno de los mensajes cada periodo segundos
def tweetPeriodico(user, periodo, frases):
	frases = ''.join(ch for ch in frases if ch != '\n')
	frases = frases.split(',')
	while (True):
		for frase in frases:
			twittear("@" + user + " " + frase)
			sleep(periodo)

def wait_start(runTime):
	startTime = time(*(map(int, runTime.split(':'))))
	while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
		sleep(1)# you can change 1 sec interval to any other
	return 0

def tweetHora(user, hora, frases):
	frases = ''.join(ch for ch in frases if ch != '\n')
 	frases = frases.split(',')
	print("esperando...")
	while (True):
		for frase in frases:
			wait_start(hora)
			twittear("@" + user + " " + frase)
			sleep(82800)

#------------------------------------------


twitter = api.getApi()

config = ConfigParser.ConfigParser()
config.read("frasesbot.conf")

for user in config.sections():
	print (user)
	newpid = os.fork()
	
	if newpid == 0:
		print (config.get(user,"periodo"))
		if config.get(user,"periodo") != '':
			tweetPeriodico(user, float(config.get(user,"periodo")), config.get(user,"frases"))
			break
		else:
			tweetHora(user, config.get(user,"hora"), config.get(user,"frases"))
			break
	else:
		continue

