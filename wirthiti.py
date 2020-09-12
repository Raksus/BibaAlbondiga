#!/usr/bin/env python

import api
import tweepy
import configparser
import time
import unicodedata
import os
import random

def convertir(texto):
	#Magia satanica anti-acentos
	texto = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
	#magia satanica mejorada
	# texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore')
	
	#Convierte el texto
	vocales=["a","e","i","o","u"]
	
	#Version inicial: Convierte todas
	texto0 = "".join("i" if char.lower() in vocales else char for char in texto)
	print("0= " + texto0)
	
	#Elimina las menciones si hay
	resultado = texto0
	resultado ="".join(word.capitalize()+" " if word.find("@")==-1 else "" for word in resultado.split()) 
		
	#Anade el #
	resultado= "@%s " % user + resultado

	return resultado


twitter = api.getApi()
img = os.path.abspath('./khaleesi.jpg')

config = configparser.ConfigParser()
config.read("wirthiti.conf")

lastId = int(config.get("tweetId", "lastId"))
user = config.get("user", "user")

try:
	tweets = twitter.user_timeline(user)
	for tweet in reversed(tweets):
		if(int(tweet.id_str) > lastId):
			if tweet.text[:3] != "RT ":
				print(tweet.text)
				print(convertir(tweet.text))
				print(img)
				# twitter.update_with_media(img, status=convertir(tweet.text), in_reply_to_status_id=tweet.id)
	
	lastId = tweets[0].id_str
	# lastId = str(1303738631920717824)
	print(lastId)
	config.set('tweetId', 'lastId', lastId)
	print(config)
	with open("wirthiti.conf", 'w') as cfg:
		config.write(cfg)
except tweepy.TweepError as e:
	print(e)
# time.sleep(30)

