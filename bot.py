#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, socket, traceback, argparse

class Bot():
    """ Class which implements the bots parsing game bot
        Github project: https://github.com/markusfisch/bots
    """
    def __init__(self, host, port):
        # connect to server
        self.s = socket.socket()
        self.s.connect((host, port))
        self.f = self.s.makefile()

        # count every turn from connecting to server
        self.turn_counter = 0

    def __enter__(self):
        return self

    # ...

    def __exit__(self, exc_type, exc_value, traceback):
        self.s.close()

if __name__ == '__main__':
    game_modes=["escape", "horde", "boom", "rumble", "training", "collect", "snakes", "avoid", "word"]
    
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', nargs=1, default="escape", choices=game_modes, metavar="MODE", help="Game mode")
    ap.add_argument('host', nargs=1, default="localhost", metavar="HOST", help="Host to connect to.")
    ap.add_argument('port', nargs=1, type=int, default=63187,metavar="PORT", help="Port of server to connect to.")

    host = sys.argv[1]
    port = int(sys.argv[2])
    
    with Bot(host, port) as bot:
        pass