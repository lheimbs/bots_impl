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