import curses
import RPi.GPIO as GPIO

screen = curses.initscr()
curses.noecho()
curses.cbreak()

screen.keypad(True)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()


while True:
        screen_input = screen.getch()
        if screen_input == ord('g'):
                screen.addstr(0, 0, 'Green!')

                GPIO.output(11,1)

                elif screen_input == ord('r'):
                        screen.addstr(0, 0, 'Red!')


                GPIO.output(16,1)

                elif screen_input == ord('b'):
                        screen.addstr(0, 0, 'Blue!')

                GPIO.output(22,1)

                elif screen_input == ord('q'):
                        curses.endwin()
                        break
    
                

