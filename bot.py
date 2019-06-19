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

        # view specific variables
        self.view_string = ""
        self.fov = 0

        # count every turn from connecting to server
        self.turn_counter = 0

    def __enter__(self):
        return self

    def training(self):
        print("----Training Game Mode----")

    def escape(self):
        print("----Escape Game Mode----")

    def collect(self):
        print("----Collect Game Mode----")

    def send_command(self, command):
        try:
            self.s.send(bytearray(command[0], "utf-8") if cmd[0] != '\n' else b'^')
        except Exception as e:
            print(e)
            traceback.print_exc()

    def get_view_string(self):
        view = self.f.readline().strip("\n")
        self.fov = len(view)
        
        if not view:
            return

        for _ in range(2, len(view)+1):
            line = self.f.readline().strip("\n")
            if not line:
                return  
            view += line
        self.view_string = view
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.s.close()

if __name__ == '__main__':
    game_modes=["escape", "horde", "boom", "rumble", "training", "collect", "snakes", "avoid", "word"]
    
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', nargs=1, default="escape", choices=game_modes, metavar="MODE", help="Game mode")
    ap.add_argument('host', nargs=1, default="localhost", metavar="HOST", help="Host to connect to.")
    ap.add_argument('port', nargs=1, type=int, default=63187,metavar="PORT", help="Port of server to connect to.")

    args = vars(ap.parse_args())
    host = args["host"][0]
    port = args["port"][0]
    mode = args["mode"][0]

    with Bot(host, port) as bot:
        # Call [mode]-method of bot
        getattr(Bot, mode)(bot)