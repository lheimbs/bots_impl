#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import argparse
import curses
import time
from Escape import BotEscape
from BotClass import Bot

def main():
    turn = 0
    server = getServer()

    if server['mode'] == 'escape':
        pass
        #bot = BotEscape()
    else:
        print("Gamemode " + server["mode"] + " not recognised. Exiting...")


    s = socket.socket()
    s.connect((server['host'], server['port']))
    f = s.makefile()



    bot = Bot()
    while True:
        try:
            cmd = bot.work(f, turn)

            printStatus(bot.fov, bot.view, cmd)
            if cmd[0] == 'q':
                break
            else:
                s.send(bytearray(cmd[0], "utf-8") if cmd[0] != '\n' else b'^')
        except Exception as e:
            print(e)
            break
        turn += 1
        time.sleep(.5)
    s.close()

def getServer():
    parser = argparse.ArgumentParser(description="Bots implementation for 'Bots Coding Night'.")
    parser.add_argument('--host', '-H', metavar='HOST', help="Host IP-Addr of Bots-Server", required=True)
    parser.add_argument('--port', '-P', type=int, metavar='PORT', help="Port of Bots-Server", required=True)
    parser.add_argument('--mode', '-m', metavar='GAMEMODE', help="Game Mode", required=True)
    parser.add_argument('--filed_size', '-s', metavar='SIZE', help="Size of the playing field")
    return vars(parser.parse_args())

def printStatus(fov, field, cmd):
    for i, line in enumerate(field):
        if i != fov:
            stdscr.addstr(i, 0, str(i) + ": " + line)
        else:
            stdscr.addstr(line + "  Command: " + cmd)
    stdscr.refresh()
    

if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        main()
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
