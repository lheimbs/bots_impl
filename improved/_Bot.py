class Mixin:
    turn_counter = 0
    def training(self):
        #----Training Game Mode----
        import training
        #if self.turn_counter != 0:
        #    if not self.get_view():
        #        return 'q'
        self.turn_counter += 1
        cmd = training.getch()

        if cmd == 'w':
            cmd = '^'
        elif cmd == 's':
            cmd = 'v'
        elif cmd == 'a':
            cmd = '<'
        elif cmd == 'd':
            cmd = '>'
        return cmd

    def escape(self):
        #----Escape Game Mode----
        pass

    def collect(self):
        #----Collect Game Mode----
        pass

    def snakes(self):
        #----Snakes Game Mode----
        pass

    def rumble(self):
        #----Rumble Game Mode----
        pass

    def avoid(self):
        #----Avoid Game Mode----
        pass

    def word(self):
        #----Word Game Mode----
        pass

    def boom(self):
        #----Boom Game Mode----
        pass

    def horde(self):
        #----Horde Game Mode----
        pass

    def dig(self):
        #----Dig Game Mode----
        pass