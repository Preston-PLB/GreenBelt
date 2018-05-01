import curses

screen = curses.initscr()

curses.noecho()
curses.cbreak()

screen.keypad(True)

#SET UP GPIO HERE

while True:
    screen_input = screen.getch()
    if screen_input == ord('g'):
        screen.addstr(0, 0, 'Green!')

        #
        #Make Green LED light up
        #

    elif screen_input == ord('r'):
        screen.addstr(0, 0, 'Red!')

        #
        # Make Red LED light up
        #

    elif screen_input == ord('b'):
        screen.addstr(0, 0, 'Blue!')

        #
        # Make Blue LED light up
        #
    elif screen_input == ord('q'):
        curses.endwin()
        break
