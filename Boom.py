import random

class BoomBot():
    def __init__(self):
        self.bomb_char = "123456789"
        self.obstacle_char = "Y"
        self.bonus_char  = "+"
        self.view_string = ""
        self.next_command = ""
        self.view_list = []
        self.fov = 0

    def get_view_string(self, f):
        view = []
        view = f.readline().strip("\n")
            
        self.fov = len(view)
        if not view:
            return

        for _ in range(2, len(view)+1):
            line = f.readline().strip("\n")
            if not line:
                return  
            view += line
        self.view_string = view

    def get_bombs(self):
        bomb_list = ""
        for char in self.view_string:
            if char in self.bomb_char:
                bomb_list += int(char)
            else:
                bomb_list += 0

    def check_bombs(self):
        bomb_front = range(4,40,9)
        bomb_left = range(36,40)
        bomb_right = range(41, 44)
        bomb_behind = range(49, 80, 9)
        bomb_top_left = range(0, 40, 10)
        bomb_top_right = range(8,40,8)
        bomb_lower_right = range(50,90,10)
        bomb_lower_left = range(48,80, 8)
        commands = "{}[]()^v"

        for index in bomb_front:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace("^", "")
        for index in bomb_left:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace("(", "")    
        for index in bomb_right:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace(")", "")  
        for index in bomb_behind:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace("v", "")  
        for index in bomb_top_left:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace("{", "")  
        for index in bomb_top_right:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace("}", "")
        for index in bomb_lower_left:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace("[", "")
        for index in bomb_lower_right:
            if self.view_string[index] in self.bomb_char:
                commands = commands.replace("]", "")
        #print(commands)
        if commands == "":
            commands = "."
        return commands

    def check_Y(self, commands):
        ys = [30,32,48,50]
        for index in ys:
            if self.view_string[index] in self.obstacle_char:
                if index == 30:
                    commands = commands.replace("{", "")
                elif index == 32:
                    commands = commands.replace("}", "")
                elif index == 48:
                    commands = commands.replace("[", "")
                else:
                    commands = commands.replace("]", "")
        return commands

    def worker(self, f):
        self.get_view_string(f)
        
        if self.next_command != "":
            cmd = self.next_command
            self.next_command = ""

        else:
            commands = self.check_bombs()
            commands = self.check_Y(commands)
            if len(commands) > 1:
                # check if diagonal is possible
                if any(x in commands for x in "{}[]"):
                    # BOMBENLEGEN und dann einen diagonalen von jetzt gehen im nächsten zug

                    cmd = "2"
                    length = len(commands) if len(commands) > 0 else 1
                    cmd_next = commands[random.randrange(20)%length]

                    while not cmd_next in "{}[]":
                        length = len(commands) if len(commands) > 0 else 1
                        cmd_next = commands[random.randrange(20)%length]
                    self.next_command = cmd_next
                else:
                    # go randomly in a übrige richtung
                    length = len(commands) if len(commands) > 0 else 1
                    cmd = commands[random.randrange(20)%length]
            else:
                cmd = commands
        #print(cmd)
        return cmd