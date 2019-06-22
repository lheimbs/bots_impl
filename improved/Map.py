import numpy

""" TODO: rotation der map fixen
    TODO: map out of bounds weiter führen
    TODO: logstring wieder entfernen
"""

class Map():
    def __init__(self, screen, size, fov):
        self.screen = screen
        self._size = size
        self._fov = fov
        self._map = numpy.zeros((size,size), dtype='<U1')
        self._map = numpy.char.replace(self._map, "", "-")
        self._orientation = self.Orientation()
        self._coords = self.Coordinates(size, fov)
        self.old_view = None

        self.logstring = ""


    def update(self, view, last_command, turn):
        #view = self.rotate_view(view, last_command)
        if self.old_view is not None and numpy.array_equal(view, self.old_view):
            self.logstring += "same view; "
            # same view as before; and check if way is blocked -> no movement
            # or way is free -> map just has not changed (empty map or sth)
            if  self.is_hit_obstacle(view) and last_command in "^v":
                self.logstring += "hit obstacle; "
                return

        self.old_view = view

        if last_command == "<":
            self.logstring += "last cmd <; ori: " + self._orientation.ori + "; "
            # going forwards
            self._orientation.turn_west()
            self.view = self.rotate_west(view)
        elif last_command == ">":
            self.logstring += "last cmd >; ori: " + self._orientation.ori + "; "
            self._orientation.turn_east()
            self.view = self.rotate_east(view)
        
        elif last_command == "^":
            self.logstring += "last cmd ^; "
            if self._orientation.ori == "north":
                self.logstring += "move north; "
                self._coords.move_north()
            elif self._orientation.ori == "south":
                self.logstring += "move south; "
                self._coords.move_south()
            elif self._orientation.ori == "west":
                self.logstring += "move west; "
                self._coords.move_west()
            elif self._orientation.ori == "east":
                self.logstring += "move east; "
                self._coords.move_east()

            self._map[self._coords.get_rows(), self._coords.get_cols()] = view

        elif last_command == "v":
            self.logstring += "last cmd v; "
            if self._orientation.ori == "north":
                self.logstring += "move south; "
                self._coords.move_south()
            elif self._orientation.ori == "south":
                self.logstring += "move north; "
                self._coords.move_north()
            elif self._orientation.ori == "west":
                self.logstring += "move east; "
                self._coords.move_east()
            elif self._orientation.ori == "east":
                self.logstring += "move west; "
                self._coords.move_west()

            self._map[self._coords.get_rows(), self._coords.get_cols()] = view
        
        if turn == 0:
            self.logstring += "init show map; "
            self._map[self._coords.get_rows(), self._coords.get_cols()] = view

    def rotate_west(self, view):
        self.logstring += "rotate west; "
        # rotate 270° array anti-clockwise once and turn the other paylers characters as well:
        # > to ^
        # ^ to <
        # < to v
        # v to >
        view = numpy.rot90(view, 3)
        view = numpy.char.replace(view, '>', 'a')
        view = numpy.char.replace(view, '^', 'b')
        view = numpy.char.replace(view, 'v', 'c')
        view = numpy.char.replace(view, '<', 'd')
        view = numpy.char.replace(view, 'a', '^')
        view = numpy.char.replace(view, 'b', '<')
        view = numpy.char.replace(view, 'c', '>')
        view = numpy.char.replace(view, 'd', 'v')
        return view

    def rotate_east(self, view):
        self.logstring += "rotate east; "
        # rotate 90° array anti-clockwise once and turn the other paylers characters as well:
        # > to v
        # ^ to >
        # < to ^
        # v to <
        view = numpy.rot90(view, 1)
        view = numpy.char.replace(view, '<', 'a')
        view = numpy.char.replace(view, 'v', 'b')
        view = numpy.char.replace(view, '>', 'c')
        view = numpy.char.replace(view, '^', 'd')
        view = numpy.char.replace(view, 'a', '^')
        view = numpy.char.replace(view, 'b', '<')
        view = numpy.char.replace(view, 'c', 'v')
        view = numpy.char.replace(view, 'd', '>')
        return view

    def is_hit_obstacle(self, view, player_collision = False):
        obstacle = "#~X"
        if player_collision:
            obstacle += "^v<>"

        if view[int(self._fov/2)-1, int(self._fov/2)] in obstacle:
            return True
        elif view[int(self._fov/2)+1, int(self._fov/2)] in obstacle:
            return True
        else:
            return False

    def print(self, title):
        x = 3
        #self.screen.clear()
        #height, width = screen.getmaxyx()
        self.screen.addstr(0, 5, title)
        self.screen.addstr(1, 0, self.logstring)
        self.logstring = ""
        
        rows, cols = self._map.shape
        try:
            self.screen.addstr(2, 0, "_" * cols+2*"_")
            self.screen.addstr(rows+x, 0, "‾" * cols+2*"‾")
        except: pass
        for row in range(rows):
            try: 
                self.screen.addstr(row+x, 0, "|")
                self.screen.addstr(row+x, cols+1, "|")
            except: pass
            for col in range(cols):
                try: self.screen.addstr(row+x, col+1, self._map[row, col])
                except: pass
        self.screen.refresh()

    class Coordinates():
        def __init__(self, size, fov):
            self.rows = [size-fov, size]
            self.cols = [size-fov, size]

        def move_north(self):
            self.rows = [x-1 for x in self.rows]

        def move_south(self):
            self.rows = [x+1 for x in self.rows]

        def move_west(self):
            self.cols = [y-1 for y in self.cols]

        def move_east(self):
            self.cols = [y+1 for y in self.cols]

        def get_rows(self):
            return slice(self.rows[0], self.rows[1])

        def get_cols(self):
            return slice(self.cols[0], self.cols[1])
    
    class Orientation():
        def __init__(self):
            self.ori = "north"
        
        def turn_east(self):
            if self.ori == "north":
                self.ori = "east"
            elif self.ori == "east":
                self.ori = "south"
            elif self.ori == "south":
                self.ori = "west"
            else:
                self.ori = "north"

        def turn_west(self):
            if self.ori == "north":
                self.ori = "west"
            elif self.ori == "west":
                self.ori = "south"
            elif self.ori == "south":
                self.ori = "east"
            else:
                self.ori = "north"