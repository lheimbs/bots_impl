#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Configuration Class """

class Configuration():
    """ A place to collect the maps parameters:
         - map-size,        N[xN], default: 32x32
         - map-type,        ["plain", "random", "maze", "terrain"], default: "plain" 
         - custom-map,      default: False
         - obstacles,       characters a player cannot enter, default: depending on mode
         - flatland,        characters a player can enter, default: empty
         - multiplier,      multiplier of flatland string, default: 14
         - non-exclusive,   multiple players can occupy the same cell, default: False
         - translate-walls  translate '-' and '|' according to orientation, default: False
         - view-radius      how many fields a player can see in every direction, default: 2
         - shrink-after     shrink map after that many turns, default: 1024
         - shrink-step      amount of turns until next shrink, default: 1
    """

    def __init__(self, mode):
        """ Set all default settings """
        self.config = {
            "map-size": [32, 32],   
            "map-type": "plain",
            "custom-map": False,
            "obstacles": self.get_obstacles(mode),
            "flatland": "",
            "multiplier": 14,
            "non-exclusive": False,
            "translate-walls": False,
            "view-radius": 2,
            "shrink-after": 1024,
            "shrink-step": 1,
        }

    def get_obstacles(self, mode):
        if mode == "training":
            obstacles = "#~X"
        elif mode == "escape":
            obstacles = "#~X"
