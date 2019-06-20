import numpy

class Map():
    def __init__(self, size, fov):
        self._size = size
        self._fov = fov
        self._map = numpy.zeros((size,size), dtype='<U1')
        self._view_x = 0 #TODO
        self._view_y = 0 #TODO

    def update(self, view, orientation):
        view = self.rotate_view(view, orientation)

        self._map[self._size-self._fov:self._size, 
                    self._size-self._fov:self._size] = view
    
    def rotate_view(self, view, orientation):
        if orientation == "<":
            # rotate 90° array anti-clockwise once and turn the other paylers characters as well:
            # > to ^
            # ^ to <
            # < to v
            # v to >
            view = numpy.rot90(view, 1)
            view = numpy.char.replace(view, '>', 'a')
            view = numpy.char.replace(view, '^', 'b')
            view = numpy.char.replace(view, 'v', 'c')
            view = numpy.char.replace(view, '<', 'd')
            view = numpy.char.replace(view, 'a', '^')
            view = numpy.char.replace(view, 'b', '<')
            view = numpy.char.replace(view, 'c', '>')
            view = numpy.char.replace(view, 'd', 'v')
        elif orientation == ">":
            # rotate 270° array anti-clockwise once and turn the other paylers characters as well:
            # > to v
            # ^ to >
            # < to ^
            # v to <
            view = numpy.rot90(view, 3)
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
        screen.addstr(0,0, title)
        
        rows, cols = self._map.shape
        for row in range(rows):
            for col in range(cols):
                try: screen.addstr(row+x, col, self._map[row, col])
                except: pass
        screen.refresh()