#!/usr/bin/env python

import api
import tweepy
import ConfigParser
import time
import unicodedata
import os
import random

def convertir(texto):
	#Magia satanica anti-acentos
	#texto = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
	#magia satanica mejorada
	texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore')
	
	#Convierte el texto
	vocales=["a","e","i","o","u"]
	
	#Version inicial: Convierte todas
	texto0 = "".join("i" if char.lower() in vocales else char for char in texto)
	
	#Primera version: ignora vocales de forma uniforme
	texto1 = "".join("i" if char.lower() in vocales and random.randrange(5)!=0 else char for char in texto)
	print("a= " + texto1)
	
	#Segunda version: prioridad a las primeras ya que solo hay una ignorada por palabra
	texto2=""
	for word in texto.split():
		flag = False
		for c in word:
			if c.lower() in vocales:
				if not (not flag and random.randrange(2) ==0):
					c="i"
				else:
					flag = True
			texto2+=c
		#Las palabras en mi idioma se separan con espasios
		texto2+=" "
	print ("b= " + texto2)
	
		#Elimina las menciones si hay
	resultado = texto1
	resultado ="".join(word.capitalize()+" " if word.find("@")==-1 else "" for word in resultado.split()) 
		
	#Anade el #
	resultado= "@moonage180 " + resultado

	return resultado


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

