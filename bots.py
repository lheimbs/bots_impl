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

class Turn():
    def __init__(self):
        self.turn = [0]

def main(host='172.19.199.52', port=63187):#port=63187
    turn = Turn()
    s = socket.socket()
    s.connect((host, port))
    f = s.makefile()
    #bot = RumbleBot()
    bot = BoomBot()
    while True:
        try:
            cmd = bot.worker(f)
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
    print(str(turn))

if __name__ == '__main__':
    main( * sys.argv[1:])