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

        if self._y < 1 - self._fov:
            self._y = self._size - self._fov

    def move_east(self):
        self._y += 1

        if self._y > self._size - self._fov:
            self._y = 1-self._fov

    def set_map(self, view, actual_map):
        print("x: %d, y: %d" % (self._x, self._y))

        if self.is_out_of_bounds_hori() and self.is_out_of_bounds_vert():
            slice_map_h_a = slice(0,self._fov + self._x)
            slice_map_h_b = slice(self._size + self._x, self._size)

            slice_map_v_a = slice(0,self._fov + self._y)
            slice_map_v_b = slice(self._size + self._y, self._size)

            slice_view_h_a = slice(self._x*-1,self._fov)
            slice_view_h_b = slice(0, self._x*-1)

            slice_view_v_a = slice(self._y*-1,self._fov)
            slice_view_v_b = slice(0, self._y*-1)
            
            actual_map[slice_map_h_a, slice_map_v_a] = view[slice_view_h_a, slice_view_v_a]
            actual_map[slice_map_h_a, slice_map_v_b] = view[slice_view_h_a, slice_view_v_b]
            actual_map[slice_map_h_b, slice_map_v_b] = view[slice_view_h_b, slice_view_v_b]
            actual_map[slice_map_h_b, slice_map_v_a] = view[slice_view_h_b, slice_view_v_a]

        elif self.is_out_of_bounds_hori() and not self.is_out_of_bounds_vert():
            slice_map_h_a = slice(0,self._fov + self._x)
            slice_map_h_b = slice(self._size + self._x, self._size)

            slice_map_v_a = slice(self._y ,self._fov + self._y)

            slice_view_h_a = slice(self._x*-1,self._fov)
            slice_view_h_b = slice(0, self._x*-1)

            slice_view_v_a = slice(0, self._fov)
            
            actual_map[slice_map_h_a, slice_map_v_a] = view[slice_view_h_a, slice_view_v_a]
            actual_map[slice_map_h_b, slice_map_v_a] = view[slice_view_h_b, slice_view_v_a]

        elif not self.is_out_of_bounds_hori() and self.is_out_of_bounds_vert():
            slice_map_v_a = slice(0,self._fov + self._y)
            slice_map_v_b = slice(self._size + self._y, self._size)

            slice_map_h_a = slice(self._x ,self._fov + self._x)

            slice_view_v_a = slice(self._y*-1,self._fov)
            slice_view_v_b = slice(0, self._y*-1)

            slice_view_h_a = slice(0, self._fov)
            
            actual_map[slice_map_h_a, slice_map_v_a] = view[slice_view_h_a, slice_view_v_a]
            actual_map[slice_map_h_a, slice_map_v_b] = view[slice_view_h_a, slice_view_v_b]
        else:
            slice_h = slice(self._x, self._x+self._fov)
            slice_v = slice(self._y, self._y+self._fov)
            actual_map[slice_h, slice_v] = view
        return actual_map

    """def get_rows(self):
        if self.is_out_of_bounds_hori() and not self.is_out_of_bounds_vert():
            # only horizontally out of bounds
            return slice(self._size - self._fov, self._size)
        else:
            return slice(self._x, self._x+self._fov)

    def get_cols(self):
        if self.is_out_of_bounds_hori() or self.is_out_of_bounds_vert():
            return slice(self._size - self._fov, self._size)
        else:
            return slice(self._y, self._y+self._fov)"""

    def is_out_of_bounds_hori(self):
        # view coord has overlap horizontally:
        #  - top of view in lower map
        #  - bottom of view in upper map 
        if self._x in range(1-self._fov, 0):
            return True
        else:
            return False

    def is_out_of_bounds_vert(self):
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