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

	x = datetime.datetime.now()
	current_time = x.strftime("%X")

	dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

	temp = dhtDevice.temperature
	hum = dhtDevice.humidity

	#Repeats to make sure there is a good reading.
	temp = 0.0
	hum = 0.0

	i = 0
	while i < 10:
		temp += dhtDevice.temperature
		hum += dhtDevice.humidity
		i += 1

	temp = temp / 10
	hum = hum / 10

	text = "The time is {}.\n\nThe current temperature is {:.1f}\N{DEGREE SIGN}C.\nThe current humidity is {:.1f}%."

	f = open("current_temp.txt", "w")
	f.write(text.format(current_time,temp,hum))
	f.close()

def dht22_to_xlsx():

	import time
	import datetime
	import board
	import adafruit_dht
	from openpyxl import load_workbook
	from datetime import date

	today = date.today()
	now = datetime.datetime.now().time()

	dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

	temp = dhtDevice.temperature
	hum = dhtDevice.humidity

	#Repeats to make sure there is a good reading.
	temp = dhtDevice.temperature
	hum = dhtDevice.humidity

	wb = load_workbook('temperature.xlsx')
	sheet = wb['Sheet1']

	row = (today, now, temp, hum)
	sheet.append(row)

	print(today)
	print(now)
	print(temp)
	print(hum)

	wb.save('temperature.xlsx')
