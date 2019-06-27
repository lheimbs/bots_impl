import numpy
import Map_Help

class Map():
    def __init__(self, screen, size, fov):
        self.screen = screen
        self._size = size
        self._fov = fov
        self._map = numpy.zeros((size,size), dtype='<U1')
        self._map = numpy.char.replace(self._map, "", "-")
        self._orientation = Map_Help.Orientation()
        self._coords = Map_Help.Coordinates(size, fov)
        self.old_view = None
        self.current_view = None

    def update(self, view, command, turn):
        #view = self.rotate_view(view, last_command)
        self.current_view = view
        

        if command == '<':
            self._orientation.turn_west()
        elif command == '>':
            self._orientation.turn_east()
        elif command == '^':
            # move one forward in current direction
            self.move_forward()
        elif command == 'v':
            # move one backwards in current direction
            self.move_backward()
        else:
            pass

        self.rotate_map()
            
        self.debug_view(view)
        self.old_view = self.current_view  
        return False

    def rotate_map(self):
        if self._orientation == "north":
            return True
        elif self._orientation == "west":
            view = numpy.rot90(view, 1)

        return

    def move_forward(self):
        if self._orientation == "north":
            self._coords.move_north()
        elif self._orientation == "west":
            self._coords.move_west()
        elif self._orientation == "south":
            self._coords.move_south()
        elif self._orientation == "east":
            self._coords.move_east()
        else:
            pass

    def move_backward(self):
        if self._orientation == "north":
            self._coords.move_south()
        elif self._orientation == "west":
            self._coords.move_east()
        elif self._orientation == "south":
            self._coords.move_north()
        elif self._orientation == "east":
            self._coords.move_west()
        else:
            pass



    def debug_view(self, rotated_view):
        # old view up top
        if self.old_view is not None:
            rows, cols = self.old_view.shape
            y = 2
            x = self._size + 5
            self.screen.addstr(y, x, "Old View:")
            for row in range(rows):
                for col in range(cols):
                    try: self.screen.addstr(row+y+1, col+1+x, self.old_view[row, col])
                    except: pass

        # current view recieved from server middle
        rows, cols = self.current_view.shape
        y = 2
        x = self._size + 2*5 + self._fov
        self.screen.addstr(y, x, "Current View:")
        for row in range(rows):
            for col in range(cols):
                try: self.screen.addstr(row+y+1, col+1+x, self.current_view[row, col])
                except: pass

        # new rotated view bottom
        rows, cols = rotated_view.shape
        y = 2
        x = self._size + 3*5 + 2*self._fov
        self.screen.addstr(y, x, "Rotated View:")
        for row in range(rows):
            for col in range(cols):
                try: self.screen.addstr(row+y+1, col+1+x, self.current_view[row, col])
                except: pass

    def print(self, title):
        x = 3
        #self.screen.clear()
        #height, width = screen.getmaxyx()
        self.screen.addstr(0, 5, title)
        
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