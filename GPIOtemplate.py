import RPi.GPIO as GPIO

'''
To set up a GPIO pin type the command below. 

The first number is the pin number
The words after tell whether or not a pin is an output or input pin

input = GPIO.IN
output = GPIO.OUT

'''
GPIO.setup(11, GPIO.OUT)
