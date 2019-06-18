from BotClass import Bot
import random

class HordeBot(Bot):
    def __init__(self, target_char="@", enemy="^v<>", empty=".", field_size=32):
        super().__init__(self)
        self.ffw = True

    def work(self, f, turn):
        if self.viewer(f):
            cmd = self.kill_monster("e")
            if not cmd:
                if self.ffw:
                    cmd = "^"
                    self.ffw = False
                else:
                    cmd = "v"
                    self.ffw = True
            return cmd
        else:
            return "q"

    def new_kill_monster(self, monster_char):
        pass

    def kill_monster(self, monster_char):
        cmd = ""
        monster_string = ""
        for i, line in enumerate(self.view):
            #if i > 2 and i < 6:
            monster_string += line
            print(line)
        print("")

        monster_ring = monster_string[30:33] + monster_string[39] + monster_string[41] + monster_string[48:51]



        command_ring = {1: "{", 2: "^", 3: "}", 
                        4: "(", 5: ")", 
                        6: "[", 7: "v", 8: "]"}
        
        if monster_char in monster_ring:
            cmd = command_ring[monster_ring.find(monster_char)+1]
            print(cmd)
        return cmd

    def wait_for_monster(self, monster_char):
        cmd = ""
        #monster_list = []
        outer_ring = [(2,2), (3,2) ,(4,2), (5,2),  (6,2),
                     (2,3),                        (6,3),
                     (2,4),                        (6,4),
                     (2,5),                        (6,5),
                     (2,6), (3,6) ,(4,6), (5,6),   (6,6)]

        for i, zeile in enumerate(self.view):
            for j, spalte in enumerate(zeile):
                position = (i,j)
                if position in outer_ring and zeile[spalte] == monster_char:
                    cmd = "."
        return cmd

        """monster_ring = ""
        for i, zeile in enumerate(self.view):
            for j, spalte in enumerate(zeile):
                position = (i,j)
                if position in inner_ring:
                    monster_ring+=spalte"""
                #monster_list = []
        """inner_ring = [(3,3), (4,3), (5,3),
                      (3,4),        (5,4),
                      (3,5), (4,5), (5,5)]"""