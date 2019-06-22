from BotClass import Bot
import random

class SnakeBot(Bot):
    """Gamemode Escape for Terrain parsing game 'bots' by marcusfisch: https://github.com/markusfisch/bots"""

    def __init__(self, target_char="@", enemy="^v<>", empty=".", field_size=32):
        super().__init__(self)
        self.turned = False
        self.avoid = "*"
        self.step_till_turn = 20
        #self.step_total = 27

    def work(self, f, turn):
        if self.viewer(f):
            if turn < 1:
                self.init()

            print(self.view)
            return self.escape(turn)
        else:
            return "q"

    def get_target(self, turn, target_list):
        cmd = "^"
        for target in target_list:
            if target in [(2,0), (2,1)]:
                print("go forwands")
                cmd = "^"
                break
            elif target in [(0,2), (1,2)]:
                print("turn left")
                if not self.turned:
                    cmd = "<"
                    #self.turned = True
                break
            elif target in [(3,2), (4,2)]:
                print("turn right")
                if not self.turned:
                    cmd = ">" 
                    #self.turned = True
                break  
        return cmd

    def escape(self, turn):
        target_list = self.find_target("@")
        if target_list:
            cmd =  self.get_target(turn, target_list)
            if cmd in "<>":
                self.turned = True
            else:
                self.turned = False
        else:
            if turn % self.step_till_turn == 0 and turn > self.field_size / 2:
                if not self.turned:
                    cmd = "<" if random.randrange(20)%2 else ">"
            else:
                cmd = "^"
        return cmd

    def find_tail(self):
        pass