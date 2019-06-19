from BotClass import Bot
import random

class RumbleBot(Bot):
    """Gamemode Rumble for Terrain parsing game 'bots' by marcusfisch: https://github.com/markusfisch/bots"""

    def __init__(self, target_char="o", enemy="^v<>", empty=".", field_size=32):
        super().__init__(self)#, target_char="o", enemy="^v<>", empty=".", field_size=32)
        self.step = 0

    def find_wall(self, dir_char):
        target_char = "X"
        for i, line in enumerate(self.view):
            if target_char in line:
                if dir_char == "{" and (line.find(target_char), i) == (2,2):
                    return True
                elif dir_char == "[" and (line.find(target_char), i) == (2,6):
                    return True
                elif dir_char == "}" and (line.find(target_char), i) == (6,2):
                    return True
                elif dir_char == "]" and (line.find(target_char), i) == (6,6):
                    return True
                elif dir_char == "^" and (line.find(target_char), i) == (4,2):
                    return True
                elif dir_char == "v" and (line.find(target_char), i) == (4,6):
                    return True
                #elif dir_char == "(" and (line.find(target_char), i) == (4,6):
                #    return True
        return False    

    def work(self, f, turn):
        ecken_links_oben = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
        ecken_links_unten = [(5,0),(5,1),(5,2),(5,3),(6,0),(6,1),(6,2),(6,3),(7,0),(7,1),(7,2),(7,3),(8,0),(8,1),(8,2),(8,3)]
        ecken_rechts_oben = [(0,5),(0,6),(0,7),(0,8),(1,5),(1,6),(1,7),(1,8),(2,5),(2,6),(2,7),(2,8),(3,5),(3,6),(3,7),(3,8)]
        ecken_rechts_unten = [(5,5),(5,6),(5,7),(5,8),(6,5),(6,6),(6,7),(6,8),(7,5),(7,6),(7,7),(7,8),(8,5),(8,6),(8,7),(8,8)]

        if self.viewer(f):
            default_char = "["
            print(str(self.view))
            

            for target_char in self.enemy:
                target_pos = self.find_target(target_char)
                if target_pos != (-1,-1):
                    # directly in front
                    if target_pos in [(4,0), (4,1), (4,2), (4,3)]:
                        #if target_char in "<>v":
                        print("Shoot")
                        return "f"
                    elif target_pos in [(0,4), (1,4), (2,4), (3,4)] and target_char == ">":
                        if not self.find_wall("}"):
                            return "}"
                        elif not self.find_wall("]"):
                            return "]"
                        else:
                            return "{" if random.randrange(20)%2 != 0 else "["
                    elif target_pos in [(4,8), (4,7), (4,6), (4,5)] and target_char == "^":
                        if not self.find_wall("{"):
                            return "{"
                        elif not self.find_wall("}"):
                            return "}"
                        else:
                            return "[" if random.randrange(20)%2 != 0 else "]"
                    elif target_pos in [(5,4), (6,4), (7,4), (8,4)] and target_char == "<":
                        if not self.find_wall("{"):
                            return "{"
                        elif not self.find_wall("["):
                            return "["
                        else:
                            return "}" if random.randrange(20)%2 != 0 else "]"

                    elif turn > 75:
                        if target_pos in [(0,4), (1,4), (2,4), (3,4)]:
                            return "{"
                        elif target_pos in [(5,4), (6,4), (7,4), (8,4)]:
                            return "}"
                        elif target_pos in [(4,8), (4,7), (4,6), (4,5)]:
                            return "]"

                        if self.step < 5:
                            default_char = ")"
                            self.step += 1
                        else:
                            default_char =  "(" if random.randrange(20)%2 else ")"

                    elif target_pos in ecken_links_oben:
                        if not self.find_wall("]"):
                            return "]"
                        else:
                            return "v" if random.randrange(20)%2 != 0 else "["
                    
                    elif target_pos in ecken_links_unten:
                        if not self.find_wall("}"):
                            return "}"
                        else:
                            return "^" if random.randrange(20)%2 != 0 else "]"

                    elif target_pos in ecken_rechts_oben:
                        if not self.find_wall("["):
                            return "["
                        else:
                            return "v" if random.randrange(20)%2 != 0 else "{"

                    elif target_pos in ecken_rechts_unten:
                        if not self.find_wall("{"):
                            return "{"
                        else:
                            return "^" if random.randrange(20)%2 != 0 else "}"
            
        else:
            return "q"
        return default_char
        
    def move_random(self, f):
        num = random.randrange(20)%4
        self.viewer(f)
        if num == 0:
            return "{"
        elif num == 1:
            return "["
        elif num == 3:
            return "]"
        else:
            return "}"