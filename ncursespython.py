#!/usr/bin/env python

import curses
import curses.textpad
import time
import clientpy3

stdscr = curses.initscr()

curses.noecho()
#curses.echo()
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)



while(True):

    cash = ("Cash is : " + str(clientpy3.run("___","____","MY_CASH")))
    secs = ("Securities are : "
            + str(clientpy3.run("___","____","MY_SECURITIES")))
    orders = ("My orders are are : " + str(clientpy3.run("___","____","MY_ORDERS")))
    clientpy3.run("___","____","CLOSE_CONNECTION");
    try:
        # Run your code here
        stdscr.addstr(1, 0, cash)
        stdscr.addstr(3, 0, secs)
        stdscr.addstr(5, 0, orders)
        stdscr.refresh()
        time.sleep(2)
    finally:
        curses.nocbreak()
        stdscr.keypad(0)
        #curses.endwin()
