#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import traceback
#from BotClass import Bot
from Rumble import RumbleBot
from Snake import SnakeBot
from Horde import HordeBot
from Boom import BoomBot
from Escape import EscapeBot

def main(host='192.168.1.201', port=63187):
    turn = 0
    s = socket.socket()
    s.connect((host, port))
    f = s.makefile()
    bot = Bot()
    while True:
        try:
            cmd = bot.work(f, turn)

            if cmd[0] == 'q':
                break
            else:
                s.send(bytearray(cmd[0], "utf-8") if cmd[0] != '\n' else b'^')
        except Exception as e:
            print(e)
            traceback.print_exc()
            break
        turn += 1
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
