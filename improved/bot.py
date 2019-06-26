#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, socket, traceback, argparse
import numpy as np
import curses

# my packages
import _Bot
from Map import Map

class Game(_Bot.Mixin):
    """ Class which implements the bots parsing game bot
        Github project: https://github.com/markusfisch/bots
    """
    def __init__(self, host, port):
        # connect to server
        self.s = socket.socket()
        self.s.connect((host, port))
        self.f = self.s.makefile()

        # view specific variables
        self.view = None
        self.get_view()

        # count every turn from connecting to server
        self.turn_counter = 0
    
    def __enter__(self):
        return self

    def get_view(self):
        view = self.f.readline().strip("\n")
        self.fov = len(view)
        
        if not view:
            return False

        for _ in range(2, len(view)+1):
            line = self.f.readline().strip("\n")
            if not line:
                return False
            view += line
        self.view = np.array(list(view)).reshape(self.fov, self.fov)
        return True

    def send_command(self, command):
        try:
            self.s.send(bytearray(command[0], "utf-8") if command[0] != '\n' else b'^')
            return True
        except Exception as e:
            print(e)
            traceback.print_exc()
            return False
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.s.close()


def parse_auguments():
    game_modes=["escape", "horde", "boom", "rumble", "training", "collect", "snakes", "avoid", "word"]

    ap = argparse.ArgumentParser()
    ap.add_argument('mode', nargs=1, default="escape", choices=game_modes, metavar="MODE", help="Game mode")
    ap.add_argument('host', default="localhost", metavar="HOST", help="Host to connect to.")
    ap.add_argument('port', nargs='?', type=int, default=63187,metavar="PORT", help="Port of server to connect to.")
    ap.add_argument('-s', '--size', dest='size', type=int, default=32, metavar="MAPSIZE", help="Mapsize of playingfiles on server.")
    ap.add_argument('-v', '--view', dest='fov', type=int, default=5, metavar='FOV', help='Size of Matrix the bot recieves from server.')
    return ap.parse_args()

def main(stdscr):
    args = parse_auguments()
    
    host = args.host[0]
    mode = args.mode[0]
    port = args.port
    size = args.size
    fov  = args.fov

    curses.curs_set(0)
    stdscr.addstr(0,0, "Connecting...")
    stdscr.refresh()

    with Game(host, port) as game:
        map = Map(stdscr, size, fov)
        command = ""
        while True:
            stdscr.clear()
            map.update(game.view, command, game.turn_counter)
            map.print("Game " + mode[0].upper() + mode[1:])

            # Call [mode]-method of bot
            command = getattr(Game, mode)(game)

            
            if command == "q":
                break
            game.send_command(command)
            

if __name__ == '__main__':
    curses.wrapper(main)