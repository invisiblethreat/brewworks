#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
 
GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.cleanup()
