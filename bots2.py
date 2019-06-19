#!/usr/bin/env python

import sys, socket, traceback

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch().decode()

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()

def read_view(f):
    view = f.readline()
    if not view:
        return
    for _ in range(2, len(view)):
        line = f.readline()
        if not line:
            return
        view += line
    return view


def main(host='192.168.1.205', port=63187):
    s = socket.socket()
    s.connect((host, port))
    f = s.makefile()
    while True:
        try:
            view = read_view(f)
            if not view:
                break
            
            sys.stdout.write(view + "Command (q<>^v): ")

            cmd = getch()

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
            traceback.print_exc()
            break
    s.close()


if __name__ == '__main__':
    main( * sys.argv[1:])