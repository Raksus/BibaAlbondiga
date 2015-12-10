#!/usr/bin/env python

import api
import tweepy
import ConfigParser

def convertir(texto):
	#Elimina las menciones si hay
	texto="".join(word.capitalize() if word.find("@")==-1 else "" for word in texto.split()) 
	
	#Convierte el texto
	vocales=["a","e","i","o","u"]
	texto = "".join("i" if char.lower() in vocales else char for char in texto)
	
	#Añade el #
	result= "#" + texto
	return result

twitter = api.getApi()

config = ConfigParser.ConfigParser()
config.read("wirthiti.conf")

lastId = int(config.get("tweetId","lastId"))

while (True):
	try:
		tweets = api.user_timeline("moonage180")
		for tweet in reversed(tweets):
			if(int(tweet.id_str) > lastId):
				if tweet.text[:3] != "RT ":
					print(convertir(tweet.text))
					#api.update_status(convertir(tweet.text),tweet.id)
		
		lastId = int(tweets[0].id_str)
		config.set("tweetId","lastId",lastId)
		with open("wirthiti.conf", 'wb') as cfg:
			config.write(cfg)
	except:
		print("Salto una excepcion, continua ejecucion")
	time.sleep(30)


