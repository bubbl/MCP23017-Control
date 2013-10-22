#!/usr/bin/env python
from os import system
import curses

def get_param(prompt_string): #initiate curses
    screen.clear()
    screen.border(0)
    screen.addstr(22, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(24, 10, 60)
    return input

def execute_cmd(cmd_string): #what to do if a key is pressed
    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with error"
    raw_input("Press enter")
    print ""

x = 0

while x != ord('q'): #if key != q, do:
    screen = curses.initscr()

    screen.clear() #create menu
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    screen.border(0)
    screen.addstr(2, 2, "Select an Option:")
    screen.addstr(4, 4, "1 - One On")
    screen.addstr(5, 4, "2 - One Off")
    screen.addstr(7, 4, "3 - Two On")
    screen.addstr(8, 4, "4 - Two Off")
    screen.addstr(10, 4, "5 - Three On")
    screen.addstr(11, 4, "6 - Three Off")
    screen.addstr(13, 4, "7 - Four On")
    screen.addstr(14, 4, "8 - Four Off")
    screen.addstr(16, 4, "9 - Five On")
    screen.addstr(17, 4, "0 - Five Off")
    screen.addstr(20, 4, "Q - Exit")
    screen.refresh()

    x = screen.getch() #wait for input

#menu options with commands
    if x == ord('1'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b b -o 0 -s high")
    if x == ord('2'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b a -o 0 -s high")
    if x == ord('3'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b b -o 1 -s high")
    if x == ord('4'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b a -o 1 -s high")
    if x == ord('5'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b b -o 2 -s high")
    if x == ord('6'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b a -o 2 -s high")
    if x == ord('7'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b b -o 3 -s high")
    if x == ord('8'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b a -o 3 -s high")
    if x == ord('9'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b b -o 4 -s high")
    if x == ord('0'):
        curses.endwin()
        execute_cmd("./mcp23017.py -b a -o 4 -s high")

curses.endwin()
