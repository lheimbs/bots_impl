"""def bot(view):
    
    top = [0,1,2,3]
    left = [5,10,15,20]
    right = [4,9,14,19]
    bottom = [21,22,23,24]

    schritt = 28
    #drehen = 3



    if "o" in view:
        pos = view.find("o")
        if pos in top:
            # o ist oben -> 2x hoch gehen





        cmd = 0
        print("o found")
        pos = view.find("o")
        input()

        if pos in possible_pos_outer_top:
            if go_if_found > 0:
                print("top")
                cmd = "^"
            else:
                if possible_pos_outer_top[pos] == 2:
                    cmd = "q"
                elif possible_pos_outer_top[pos] < 2:
                    if not turn_walk:
                        cmd = "<"
                    else:
                        cmd = "^"
                else:
                    if not turn_walk:
                        cmd = ">"
                    else:
                        cmd = "^"


        elif pos in possible_pos_outer_left:
            if go_if_found == 2:
                print("left go 2")
                cmd = "<"
            elif go_if_found > 0:
                print("left")
                cmd = "^"
            else:
                if possible_pos_outer_left[pos] == 10:
                    cmd = "q"
                elif possible_pos_outer_left[pos] < 10:
                    if not turn_walk:
                        cmd = ">"
                    else:
                        cmd = "^"
                else:
                    if not turn_walk:
                        cmd = "<"
                    else:
                        cmd = "^"


        elif pos in possible_pos_outer_right:
            if go_if_found == 2:
                print("right go 2")
                cmd = ">"
            elif go_if_found > 0:
                print("right")
                cmd = "^"
            else:
                if possible_pos_outer_right[pos] == 14:
                    cmd = "q"
                elif possible_pos_outer_right[pos] < 14:
                    if not turn_walk:
                        cmd = ">"
                    else:
                        cmd = "^"
                else:
                    if not turn_walk:
                        cmd = "<"
                    else:
                        cmd = "^"

        elif pos in possible_pos_outer_bottom:
            if go_if_found > 0:
                print("bottom")
                cmd = "v"
            else:
                if possible_pos_outer_bottom[pos] == 22:
                    cmd = "q"
                elif possible_pos_outer_bottom[pos] < 22:
                    if not turn_walk:
                        cmd = ">"
                    else:
                        cmd = "^"
                else:
                    if not turn_walk:
                        cmd = "<"
                    else:
                        cmd = "^"

    else:
    if param[0] != 0:
        param[0] -= 1
        cmd = "^"
    else:
        #input()
        if param[1] == 0:
            schritt -= 2
        param[0] = schritt
        param[1] -= 1
        cmd = "<"
    print(str(param[0]) + " - " + str(param[1]))
    return cmd

def check_hindernis(view):
    if view[7] in hindernis:
        return "<" #links drehen
    else:
        return "^" #vorwärts laufen

def bot(view, turns):
    if turns == 0:
        view = view.replace("\n","")
        print(view)
        pos_o_absolut = view.find("o")
        print(pos_o_absolut)
        pos_o_relativ = where_relative[pos_o_absolut]
        print("O-Pos: " + str(pos_o_relativ[0]) + " - " + str(pos_o_relativ[1]))

        cmd = check_hindernis(view)
    else:
        view = view.replace("\n","")
        cmd = check_hindernis(view)
    return cmd

def check_hindernis(view):
    global ecke_alt, ecke_neu
    ecke_neu = check_ecke(view)
    if view[13] in hindernis:# or (view[17] in hindernis)
        print("hindernis rechts")
        cmd = "^"
    if view[7] in hindernis:
        print("hindernis vorne")
        cmd = "<" #links drehen
    if view[7] == "." and view[13] == ".":#in hindernis and not view[13] in hindernis:
        cmd = ">"
    

    ecke_alt = ecke_neu
    return cmd

def check_ecke(view):
    print(view)
    if (view[11] == ".") and (view[13] in hindernis):
        print("rechts")
        return "rechts"
    if (view[11] in hindernis) and (view[13] == "."):
        print("rechts")
        return "links"
    if (view[11] == ".") and (view[13] == "."):
        print("rechts")
        return "keins"
    print("none 11: " + str(view[11]) + " 13: " + str(view[13]))

    pos_self = (0, 0)
#oben, unten, rechts, links = 0
ecke_neu = ""
ecke_alt = ""

where_relative = [(-2,2),  (-1,2),  (0,2),  (1,2),  (2,2),
                  (-2,1),  (-1,1),  (0,1),  (1,1),  (2,1),
                  (-2,0),  (-1,0),  (0,0),  (1,0),  (2,0),
                  (-2,-1), (-1,-1), (0,-1), (1,-1), (2,-1),
                  (-2,-2), (-1,-2), (0,-2), (1,-2), (2,-2)]

hindernis = ["X","~","#"]


def bot(view, turns):
    if turns == 0:
        view = view.replace("\n","")
        print(view)
        pos_o_absolut = view.find("o")
        print(pos_o_absolut)
        pos_o_relativ = where_relative[pos_o_absolut]
        print("O-Pos: " + str(pos_o_relativ[0]) + " - " + str(pos_o_relativ[1]))

    cmd = check_hindernis(view)
    return cmd

def check_hindernis(view):
    global ecke_alt, ecke_neu
    ecke_neu = check_ecke(view)
    if view[13] in hindernis:# or (view[17] in hindernis)
        print("hindernis rechts")
        cmd = "^"
    elif view[7] in hindernis:
        print("hindernis vorne")
        cmd = "<" #links drehen
    if view[7] == "." and view[13] == ".":#in hindernis and not view[13] in hindernis:
        cmd = ">"
    return cmd


def bot_shoot(view, turns):
    global random
    random -= 1
    view = view.replace("\n","")
    pos_at = view.find("@")
    pos_st = view.find("*")
    if view[2] in enemys:
        print("FIRE")
        return "f"
    elif pos_st == 2 or pos_st == 7:
        if randint(1,2) == 1:
            print("TURN LEFT")
            return "<"
        else:
            print("TURN RIGHT")
            return ">"
    elif view[10] in enemys or view[14] in enemys or view[22]:
        return "^"
    else:
        if random != 0:
            print("MOVE")
            return "^"
        else:
            random = randint(4,9)
            if randint(1,2) == 1:
                print("TURN LEFT")
                return "<"
            else:
                print("TURN RIGHT")
                return ">"

def bot_gems(view, turns, zeug):
    view = view.replace("\n","")
    pos_st = view.find("*")

    if view[2] in enemys:
        print("FIRE")
        return "f"
    elif pos_st == 2 or pos_st == 7:
        if randint(1,2) == 1:
            print("TURN LEFT")
            return "<"
        else:
            print("TURN RIGHT")
            return ">"
    elif turns%zeug == 0:
        if randint(1,2) == 1:
            print("TURN LEFT")
            return "<"
        else:
            print("TURN RIGHT")
            return ">"
    else:
        return "^"

    def bot(view, turn):
    view = view.replace("\n","")

    if view[4] in hindernis:
        # drehen
        if randint(1,2) == 1:
            cmd = ">" # rechts
        else:
            cmd = "<" # links
    else:
        cmd = "^" # VORWÄRTS
    return cmd