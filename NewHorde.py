class Bot():
    def __init__(self):
        self.target_char = "e"
        self.spawn_char = "&"
        self.life_char  = "+"
        self.view = []

    def get_view(self, f):
        view = []
        #view.append(list(f.readline().strip("\n")))

        view = f.readline().replace("\n", "")
        if not view:
            return

        for _ in range(2, len(view)+1):
            line = f.readline().replace("\n", "")
            if not line:
                return  
            view += line

        print(view)

with open("test_input.txt", "r", encoding="utf-8") as f:


    bot = Bot()
    bot.get_view(f)