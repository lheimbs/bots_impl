import math

class Bot():
    """Base-Class for Terrain parsing game 'bots' by marcusfisch: https://github.com/markusfisch/bots"""
    
    def __init__(self, target_char="o", enemy="^v<>", empty=".", field_size=32):
        # default vars
        self.target_char = target_char
        self.enemy = enemy
        self.empty = empty
        self.field_size = field_size

        # vars to be calculated at runtime:
        self.view = []
        self.fov = 2

        # vars for targeting [target_char]
        self.turned = False
        self.target = ()
        self.pos = [2,2]

        # vars for escape
        self.step = 0
        self.counter = 0
        self.stepper = 3

    def init(self):
        self.step = self.field_size - self.fov + 1
        self.step_total = self.step
        self.pos = [int(self.fov/2), int(self.fov/2)]

    def viewer(self, f):
        self.view = []
        line = f.readline().strip("\n")
        self.fov = len(line)
        self.view.append(line)
        for _ in range(0, self.fov-1):
            line = f.readline().strip("\n")
            self.view.append(line)
        if self.view == ['']:
            return False
        else:
            return True

    def work(self, f, turn):
        if self.viewer(f):
            if turn < 1:
                self.init()

            print(self.view)
            return self.escape(turn)
        else:
            return "q"

    def escape(self, turn):
        target = self.find_target(self.target_char)
        if target != (-1,-1):
            if self.target == ():
                self.target = target
            cmd = self.get_target(turn)
        else:
            if turn%self.step_total == 0 and turn > self.field_size / 2:
                self.counter += 1
                if self.stepper == 3:
                    if self.counter > 2:
                        self.stepper = 2
                        self.counter = 0
                        self.step -= self.fov
                else:
                    if self.counter > 1:
                        self.counter = 0
                        self.step -= self.fov
                self.step_total += self.step
                if self.step > 0:
                    cmd = "<"
                else:
                    cmd = "q"
            else:
                cmd = "^"
        return cmd

    def find_target(self, target_char):
        targets = []
        for i, line in enumerate(self.view):
            if target_char in line:# and i < 3:
                # (Spalte, Zeile)
                pos = (line.find(target_char), i)
                targets.append(pos)
        return targets    

    def get_target(self, turn):
        x_t, y_t = self.target
        if x_t == self.pos[0]:
            print("target straight ahead")
            cmd = "^"
        elif self.target in [(0,2), (1,2)]:
            print("turn left")
            cmd = "<"
        elif self.target in [(3,2), (4,2)]:
            print("turn right")
            cmd = ">"    
        else:
            if y_t < self.pos[1]:
                self.pos[1] -= 1
                print("target above me")
                cmd = "^"
            else:
                if not self.turned:
                    print("turn to target")
                    cmd = ">"
                    self.turned = True
                else:
                    if x_t < self.pos[0]:
                        print("target behind")
                        cmd = "v"
                    else:
                        print("target in front")
                        cmd= "^"
        return cmd