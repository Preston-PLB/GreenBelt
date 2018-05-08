import curses
import RPi.GPIO as GPIO
import time

screen = curses.initscr()

curses.noecho()
curses.cbreak()

screen.keypad(True)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

pin_list = [13,15,17]
GPIO.setup(pin_list, GPIO.out)

pin_13 = GPIO.PWM(13, 100)
pin_15 = GPIO.PWM(15, 100)
pin_17 = GPIO.PWM(17, 100)

pin_13.start(0)
pin_15.start(0)
pin_17.start(0)

while True:
    screen_input = screen.getch()
    if screen_input == ord('g'):
        screen.addstr(0, 0, 'Green!')
        #Flash light
        for x in range(50)
            pin_13.setDutyCycle(x)
            time.sleep(0.1)
        
        for x in range(50)
            pin_13.setDutyCycle(50-x)
            time.sleep(0.1)

    elif screen_input == ord('r'):
        screen.addstr(0, 0, 'Red!')
        #Flash light
        for x in range(50)
            pin_15.setDutyCycle(x)
            time.sleep(0.1)
        
        for x in range(50)
            pin_15.setDutyCycle(50-x)
            time.sleep(0.1)

    elif screen_input == ord('b'):
        screen.addstr(0, 0, 'Blue!')
        #Flash light
        for x in range(50)
            pin_17.setDutyCycle(x)
            time.sleep(0.1)
        
        for x in range(50)
            pin_17.setDutyCycle(50-x)
            time.sleep(0.1)
        
    elif screen_input == ord('q'):
        curses.endwin()
        GPIO.cleanup()
        break
