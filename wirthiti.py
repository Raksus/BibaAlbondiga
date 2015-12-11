#!/usr/bin/env python

import api
import tweepy
import ConfigParser
import time
import unicodedata
import os

def convertir(texto):
	#Magia satanica anti-acentos
	#texto = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
	#magia satanica mejorada
	texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore')
	
	
	#Convierte el texto
	vocales=["a","e","i","o","u"]
	texto = "".join("i" if char.lower() in vocales else char for char in texto)
	
	#Elimina las menciones si hay

	texto="".join(word.capitalize()+" " if word.find("@")==-1 else "" for word in texto.split()) 
		
	#Anade el #
	result= "@moonage180 " + texto
	return result


twitter = api.getApi()
img = os.path.abspath('/home/BibaAlbondiga/litmi.png')

config = ConfigParser.ConfigParser()
config.read("wirthiti.conf")

lastId = int(config.get("tweetId","lastId"))

while (True):
	try:
		tweets = twitter.user_timeline("moonage180")
		for tweet in reversed(tweets):
			if(int(tweet.id_str) > lastId):
				if tweet.text[:3] != "RT ":
					print(convertir(tweet.text))
					twitter.update_with_media(img, status=convertir(tweet.text), in_reply_to_status_id=tweet.id)
		
		lastId = int(tweets[0].id_str)
		config.set("tweetId","lastId",lastId)
		with open("wirthiti.conf", 'wb') as cfg:
			config.write(cfg)
	except tweepy.TweepError as e:
		print(e)
	time.sleep(30)

