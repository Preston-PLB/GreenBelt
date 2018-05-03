import RPi.GPIO as GPIO



'''
How to start a GPIO program

In order to have a successful program you must type the next three lines of code
'''

#this tells GPIO to not report warnings. We know what we are doing and don't need warnings
GPIO.setwarnings(False)

#This tells python how we are numbering our pins on the pi. It essentially gives python our pin diagram
GPIO.setmode(GPIO.BOARD)

#This cleans up the mess left behind from previous programs that have been ran
GPIO.cleanup()

'''
Here is how to SETUP a pin 

GPIO.setup(pin#, GPIO.IN or GPIO.OUT)

pin# is the pin you want to use
The words after tell whether or not a pin is an output or input pin

input = GPIO.IN
output = GPIO.OUT

'''
GPIO.setup(11, GPIO.OUT)
# or
GPIO.setup(11, GPIO.IN)

'''
Here is how to use OUTPUT

GPIO.output(pin#, 1 or 0)

pin# is the pin you want to use
1 or 0 is on or off

on = 1
off = 0
'''
GPIO.output(11, 1)
# or
GPIO.output(11, 0)