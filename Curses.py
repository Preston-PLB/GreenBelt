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

while True:
    screen_input = screen.getch()
    if screen_input == ord('g'):
        screen.addstr(0, 0, 'Green!')
        #Flash light
        GPIO.output(13, 1)
        time.sleep(1)
        GPIO.output(13, 0)

    elif screen_input == ord('r'):
        screen.addstr(0, 0, 'Red!')
        #Flash light
        GPIO.output(15, 1)
        time.sleep(1)
        GPIO.output(15, 0)

    elif screen_input == ord('b'):
        screen.addstr(0, 0, 'Blue!')
        #Flash light
        GPIO.output(17, 1)
        time.sleep(1)
        GPIO.output(17, 0)
        
    elif screen_input == ord('q'):
        curses.endwin()
        GPIO.cleanup()
        break
