class Coordinates():
    def __init__(self, size, fov):
        # use top-left coordinate for view tracking
        self._x = size-fov
        self._y = size-fov

        self._fov = fov
        self._size = size

    def move_north(self):
        self._x -= 1

        if self._x < 1 - self._fov:
            self._x = self._size - self._fov

    def move_south(self):
        self._x += 1

        if self._x > self._size - self._fov:
            self._x = 1-self._fov

    def move_west(self):
        self._y -= 1

    def move_east(self):
        self._y += 1

    def get_rows(self):
        if self.check_oob_horizontal() or self.check_oob_vertical():
            return slice(self._size - self._fov, self._size)
        else:
            return slice(self._x, self._x+self._fov)

    def get_cols(self):
        if self.check_oob_horizontal() or self.check_oob_vertical():
            return slice(self._size - self._fov, self._size)
        else:
            return slice(self._y, self._y+self._fov)

    def check_oob_horizontal(self):
        # view coord has overlap horizontally:
        #  - top of view in lower map
        #  - bottom of view in upper map 
        if self._x in range(1-self._fov, 0):
            return True
        else:
            return False

    def check_oob_vertical(self):
        # view coord has overlap vertically:
        #  - right of view in left map
        #  - left of view in right map 
        if self._y in range(1-self._fov, 0):
            return True
        else:
            return False

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