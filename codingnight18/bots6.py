
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
from random import randint

hindernis = "X~#"

def read_map(f):
    view = ''
    total = 0
    width = -1
    while True:
        view += f.readline()
        if width <= 0:
            width = len(view)
            if width > 0:
                total = width * (width - 1)
        if len(view) == total:
            break
    return view
"""
def bot(view, turn):
    pos_me = 40
    view = view.replace("\n","")

    diagonale = check_diagonale(view, pos_me)

    if diagonale == "move":
        if not view[pos_me-9] in hindernis:
         #check next move
            if check_diagonale(view, pos_me-9) == "okay":
                cmd = "^"
            else:
                if check_diagonale(view, pos_me+9) == "okay":
                    cmd = "v"
                else:
                    rand = randint(1,3)
                    if rand == 1:
                        cmd = "^"
                    elif rand == 2:
                        cmd = "f"
                    else:
                        cmd = "v"
                    #cmd = "f"
        elif not view[pos_me+9] in hindernis:
            if check_diagonale(view, pos_me+9) == "okay":
                cmd = "v"
            else:
                rand = randint(1,3)
                if rand == 1:
                    cmd = "^"
                elif rand == 2:
                    cmd = "f"
                else:
                    cmd = "v"
                #cmd = "f"
        else:
            cmd = "f"
    else:
        cmd = "f" # okay
    return cmd

def check_diagonale(view, pos):
    if view[pos-10] in hindernis or view[pos+10] in hindernis or view[pos-8] in hindernis or view[pos+8] in hindernis:
        return "move"
    else:
        return "okay"
"""

def bot(view):
    
    top = [0,1,2,3]
    left = [5,10,15,20]
    right = [4,9,14,19]
    bottom = [21,22,23,24]

    schritt = 28
    #drehen = 3



    if "o" in view:
        pos = view.find("o")

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

def main(host='172.19.199.52', port=63187):
    turns = 1
    s = socket.socket()
    s.connect((host, port))
    f = s.makefile()
    while True:
        try:
            print(turns)
            view = read_map(f)
            if not view:
                break

            cmd = bot(view)

            print(view)
            #cmd = sys.stdin.readline()
            turns += 1

            #input()

            if cmd == 'q':
                print("exit")
                break
            else:
                s.send(bytearray(cmd[0], "utf-8") if cmd[0] != '\n' else b'^')
        except Exception as e:
            print(e)
            break
    s.close()

if __name__ == '__main__':
    main( * sys.argv[1:])