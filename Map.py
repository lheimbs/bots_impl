import numpy

class Map():
    def __init__(self, size, fov):
        self._size = size
        self._fov = fov
        self._map = numpy.zeros((size,size), dtype='<U1')
        self._map = numpy.char.replace(self._map, "", "-")
        #self._view_x =  #TODO
        #self._view_y = [size-fov, size] #TODO
        self._orientation = self.Orientation()
        self._coords = self.Coordinates(size, fov)

    def update(self, view, last_command):
        #view = self.rotate_view(view, last_command)

        if last_command == "<":
            # going forwards
            self._orientation.turn_west()
        elif last_command == ">":
            self._orientation.turn_east()
        
        elif last_command == "^":
            if self._orientation.ori == "north":
                self._coords.move_north()
            elif self._orientation.ori == "south":
                self._coords.move_south()
            elif self._orientation.ori == "west":
                self._coords.move_west()
            elif self._orientation.ori == "east":
                self._coords.move_east()

            self._map[self._coords.get_rows(), self._coords.get_cols()] = view

        elif last_command == "v":
            if self._orientation.ori == "north":
                self._coords.move_south()
            elif self._orientation.ori == "south":
                self._coords.move_north()
            elif self._orientation.ori == "west":
                self._coords.move_east()
            elif self._orientation.ori == "east":
                self._coords.move_west()

            self._map[self._coords.get_rows(), self._coords.get_cols()] = view
    
    def rotate_view(self, view, orientation):
        if orientation == "<":
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
        elif orientation == ">":
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

    def print(self, screen, title):
        x = 2
        screen.clear()
        #height, width = screen.getmaxyx()
        screen.addstr(0, 5, title)
        
        rows, cols = self._map.shape
        screen.addstr(1, 0, "_" * cols+2*"_")
        screen.addstr(rows+x, 0, "‾" * cols+2*"‾")
        for row in range(rows):
            try: 
                screen.addstr(row+x, 0, "|")
                screen.addstr(row+x, cols+1, "|")
            except: pass
            for col in range(cols):
                try: screen.addstr(row+x, col+1, self._map[row, col])
                except: pass
        screen.refresh()

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