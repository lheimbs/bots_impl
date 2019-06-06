from BotClass import Bot

class BotEscape(Bot):
    """Gamemode Escape for Terrain parsing game 'bots' by marcusfisch: https://github.com/markusfisch/bots"""

    def __init__(self, target_char="o", enemy="^v<>", empty=".", field_size=32):
        super().__init__(self, target_char="o", enemy="^v<>", empty=".", field_size=32)
        self.step = 0
        self.counter = 0
        self.stepper = 3

    def escape(self, turn):
        target = super().find_target()
        if target != (-1,-1):
            if super().target == ():
                super().target = target
            cmd = super().get_target(turn)
        else:
            if turn % super().step_total == 0 and turn > super().field_size / 2:
                self.counter += 1
                if self.stepper == 3:
                    if self.counter > 2:
                        self.stepper = 2
                        self.counter = 0
                        self.step -= super().fov
                else:
                    if self.counter > 1:
                        self.counter = 0
                        self.step -= super().fov
                super().step_total += self.step
                if self.step > 0:
                    cmd = "<"
                else:
                    cmd = "q"
            else:
                cmd = "^"
        return cmd