#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, argparse
import curses

# my packages
from Map2 import Map
from Game import Game

def parse_arguments():
    game_modes=["escape", "horde", "boom", "rumble", "training", "collect", "snakes", "avoid", "word"]

    ap = argparse.ArgumentParser()
    ap.add_argument('host', nargs=1, metavar="HOST", help="Host to connect to.")
    ap.add_argument('mode', nargs=1, default="escape", choices=game_modes, metavar="MODE",    help="Game mode")
    ap.add_argument('-p', '--port', dest='port', type=int, default=63187,  metavar="PORT",    help="Port of server to connect to.")
    ap.add_argument('-s', '--size', dest='size', type=int, default=32,     metavar="MAPSIZE", help="Mapsize of playingfiles on server.")
    ap.add_argument('-v', '--view', dest='fov',  type=int, default=5,      metavar='FOV',     help='Size of Matrix the bot recieves from server.')
    return ap.parse_args()

def main(stdscr):
    print("Hallo")
    args = parse_arguments()
    
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
            if game.get_view():
                map.update(game.view, command, game.turn_counter)
                map.print("Game " + mode[0].upper() + mode[1:])

                # Call [mode]-method of bot
                command = getattr(Game, mode)(game)

                if command == "q":
                    break

                game.send_command(command)
            

if __name__ == '__main__':
    curses.wrapper(main)
    #main(None)