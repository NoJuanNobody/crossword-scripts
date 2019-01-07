from curses import *

def main():
    stdscr = initscr()
    stdscr.addstr(20, 20, "hello word")
    stdscr.getch()
    endwin()
    return 0

main()