import api, tweepy, ConfigParser

twitter = api.getApi()

config = ConfigParser.ConfigParser()
config.read("favs.conf")

last_id = config.get("favs", "last_id")

while True:
	try:
		to_compare = twitter.user_timeline(id="RaksusI") # count=1
		for tweet in reversed(to_compare):
			if(int(tweet.id_str) > last_id):
			if tweet.text[:3]!="RT ":
				twitter.create_favorite(id)
			last_id = int(tweet.id_str)
			config.set("favs", "last_id", last_id)
		with open("favs.conf", "wb") as cfg:
			config.write(cfg)
	except tweepy.TweepError as e:
		print e
