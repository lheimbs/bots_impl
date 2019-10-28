#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
from . import Orientation
from . import Coordinates

class BotsMap():
    def __init__(self, screen, size, fov, player_collision=False):
        self._screen = screen
        self._size = size
        self._fov = fov
        self._map = numpy.zeros((size, size), dtype='<U1')
        self._map = numpy.char.replace(self._map, "", "-")
        self._old_view = None
        self._current_view = None
        self.orientation = Orientation.Orientation()
        self.coords = Coordinates.Coordinates(size, fov)
        self.player_collision = player_collision
        self._obstacle = "#~X"
        self._enemyobstacle = "<>^v"


    def update(self, view, command, turn):
        self._current_view = view
        

        if command == '<':
            # change orientation: rotate anti-clockwise
            self.orientation.turn_west()
        elif command == '>':
            # change orientation: rotate clockwise
            self.orientation.turn_east()
        elif command == '^' and not self.is_hit_obstacle(view, command):
            # move one step forward in current direction
            self.move_forward()
        elif command == 'v' and not self.is_hit_obstacle(view, command):
            # move one step backwards in current direction
            self.move_backward()
        else:
            pass

        view = self.rotate_map(view)
            
        self.debug_view(view)
        self._old_view = self._current_view  
        self._map = self.coords.set_map(view, self._map)
        return False

    def rotate_map(self, view):
        if self.orientation.ori == "north":
            view = numpy.char.replace(view, 'A', '▲')
        elif self.orientation.ori == "west":
            view = self.rotate_west(view)
        elif self.orientation.ori == "south":
            view = self.rotate_south(view)
        elif self.orientation.ori == "east":
            view = self.rotate_east(view)
        return view

    def rotate_south(self, view):
        view = numpy.rot90(view, 2) #rotate 180°
        view = numpy.char.replace(view, 'A', '▼')
        return view

    def rotate_east(self, view):
        view = numpy.rot90(view, 3) #rotate 180°
        view = numpy.char.replace(view, 'A', '▶')
        return view

    def rotate_west(self, view):
        view = numpy.rot90(view, 1) #rotate 90° anti-clockwise
        view = numpy.char.replace(view, 'A', '◀')
        return view

    def move_forward(self):
        if self.orientation.ori == "north":
            self.coords.move_north()
        elif self.orientation.ori == "west":
            self.coords.move_west()
        elif self.orientation.ori == "south":
            self.coords.move_south()
        elif self.orientation.ori == "east":
            self.coords.move_east()
        else:
            pass

    def move_backward(self):
        if self.orientation.ori == "north":
            self.coords.move_south()
        elif self.orientation.ori == "west":
            self.coords.move_east()
        elif self.orientation.ori == "south":
            self.coords.move_north()
        elif self.orientation.ori == "east":
            self.coords.move_west()
        else:
            pass

    def is_hit_obstacle(self, view, command):
        obstacle = self._obstacle
        if self.player_collision:
            obstacle += self._enemyobstacle

        if self._old_view[int(self._fov/2)-1, int(self._fov/2)] in obstacle and command == '^':
            # is obstacle in front
            return True
        elif self._old_view[int(self._fov/2)+1, int(self._fov/2)] in obstacle and command == 'v':
            # is obstacle underneath
            return True
        else:
            return False
    
    def is_found_finish(self, command):
        finish = self._finish

        if self._old_view[int(self._fov/2)-1, int(self._fov/2)] in finish and command == '^':
            # is obstacle in front
            return True
        elif self._old_view[int(self._fov/2)+1, int(self._fov/2)] in finish and command == 'v':
            # is obstacle underneath
            return True
        else:
            return False

    def debug_view(self, rotated_view):
        #debug string
        self._screen.addstr(1,1, "Orientation: %s Coordinate: %d : %d" % 
        (self.orientation.ori, self.coords._x, self.coords._y))

        # old view up top
        if self._old_view is not None:
            rows, cols = self._old_view.shape
            y = 2
            x = self._size + 5
            self._screen.addstr(y, x, "Old View:")
            for row in range(rows):
                for col in range(cols):
                    try: self._screen.addstr(row+y+1, col+1+x, self._old_view[row, col])
                    except: pass

        # current view recieved from server middle
        rows, cols = self._current_view.shape
        y = 2
        x = self._size + 2*5 + self._fov
        self._screen.addstr(y, x, "Current View:")
        for row in range(rows):
            for col in range(cols):
                try: self._screen.addstr(row+y+1, col+1+x, self._current_view[row, col])
                except: pass

        # new rotated view bottom
        if rotated_view is not None:
            rows, cols = rotated_view.shape
        y = 2
        x = self._size + 3*5 + 2*self._fov
        self._screen.addstr(y, x, "Rotated View:")
        for row in range(rows):
            for col in range(cols):
                try: self._screen.addstr(row+y+1, col+1+x, rotated_view[row, col])
                except: pass

    def print(self, title):
        x = 3
        #self.screen.clear()
        #height, width = screen.getmaxyx()
        self._screen.addstr(0, 5, title)
        
        rows, cols = self._map.shape
        try:
            self._screen.addstr(2, 0, "_" * cols+2*"_")
            self._screen.addstr(rows+x, 0, "‾" * cols+2*"‾")
        except: pass
        for row in range(rows):
            try: 
                self._screen.addstr(row+x, 0, "|")
                self._screen.addstr(row+x, cols+1, "|")
            except: pass
            for col in range(cols):
                try: self._screen.addstr(row+x, col+1, self._map[row, col])
                except: pass
        self._screen.refresh()
