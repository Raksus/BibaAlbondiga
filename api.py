#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import configparser

Config = configparser.ConfigParser()
Config.read("keys.conf")

# Configurar claves
CONSUMER_KEY = Config.get("keys", "consumer_key")
CONSUMER_SECRET = Config.get("keys", "consumer_secret")
ACCESS_KEY = Config.get("keys", "access_key")
ACCESS_SECRET = Config.get("keys", "access_secret")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def getApi():
	return api
