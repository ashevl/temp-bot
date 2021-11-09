def text_to_tweet():
	from twitter import tweet

	f = open('current_temp.txt', 'r')
	tweet(f.read())
	f.close

def dht22_to_text():

	import time
	import datetime
	import board
	import adafruit_dht

	dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

	temp = dhtDevice.temperature
	hum = dhtDevice.humidity

	#Repeats to make sure there is a good reading.
	temp = dhtDevice.temperature
	hum = dhtDevice.humidity

	x = datetime.datetime.now()
	current_time = x.strftime("%X")

	text = "The time is {}.\n\nThe current temperature is {}C.\nThe current humidity is {}%"

	f = open("current_temp.txt", "w")
	f.write(text.format(current_time,temp,hum))
	f.close()
