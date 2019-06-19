#!/usr/bin/env python

import sys
import socket
import msvcrt


def read_view(f):
    view = f.readline()
    if not view:
        return
    for x in range(2, len(view)):
        line = f.readline()
        if not line:
            return
        view += line
    return view


def main(host='172.19.199.52', port=60003):
    s = socket.socket()
    s.connect((host, port))
    f = s.makefile()
    while True:
        try:
            view = read_view(f)
            if not view:
                break
            sys.stdout.write(view + "Command (q<>^v): ")
            #cmd = sys.stdin.readline()[0]
            cmd = msvcrt.getch().decode()
            if cmd == 'w':
                cmd = '^'
            elif cmd == 's':
                cmd = 'v'
            elif cmd == 'a':
                cmd = '<'
            elif cmd == 'd':
                cmd = '>'
            else:
                pass
            if cmd == 'q':
                break
            if cmd == '\n':
                cmd = '^'
            s.send(cmd if sys.version_info[0] < 3 else str.encode(cmd))
        except Exception as e:
            print(e)
            break
    s.close()


if __name__ == '__main__':
    main( * sys.argv[1:])