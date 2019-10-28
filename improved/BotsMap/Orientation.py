#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Orientation Class """

class Orientation():
    """ Save orientation and handle turning east/west """

    def __init__(self):
        self.ori = "north"

    def turn_east(self):
        """ Set orientation var 'self.ori' to new value.
            rotating clockwise """
        if self.ori == "north":
            self.ori = "east"
        elif self.ori == "east":
            self.ori = "south"
        elif self.ori == "south":
            self.ori = "west"
        else:
            self.ori = "north"

    def turn_west(self):
        """ Set orientation var 'self.ori' to new value.
            rotating anti-clockwise """
        if self.ori == "north":
            self.ori = "west"
        elif self.ori == "west":
            self.ori = "south"
        elif self.ori == "south":
            self.ori = "east"
        else:
            self.ori = "north"
