#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
from BotClass import Bot

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
            break
        turn += 1
    s.close()

if __name__ == '__main__':
    main( * sys.argv[1:])