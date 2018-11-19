#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

relay_pins = [26,20,21]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for rp in relay_pins:
	GPIO.setup(rp,GPIO.OUT)

print("Setup The Relay Module is a success.")

try:
	while True:
		for rp in relay_pins:
			GPIO.output(rp,GPIO.LOW)
			print("Channel {}:The Common Contact is access to the Normal Open Contact!".format(rp))
			time.sleep(0.5)
	
			GPIO.output(rp,GPIO.HIGH)
			print("Channel {}:The Common Contact is access to the Normal Closed Contact!".format(rp))
			time.sleep(0.5)
except:
	print("except")
	GPIO.cleanup()
