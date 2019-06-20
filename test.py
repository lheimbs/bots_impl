import curses, numpy
"""
def display_matrix(screen, m):
    rows, cols = m.shape
    for row in range(rows):
        for col in range(cols):
            screen.addstr(row, col, "%s" % m[row, col])

screen = curses.initscr()
display_matrix(screen, b)
screen.refresh()"""


view = "...........^.............>..............A..........v.....................<......."
size = 20
fov = 9
a = numpy.array(list(view)).reshape(9,9)
b = numpy.zeros((size,size), dtype='<U1')
#b = numpy.char.replace(b, '', '-')
#print(b)
b[size-fov:size, size-fov:size] = a



from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.addstr(0,0, str(stdscr.getmaxyx()))
    # This raises ZeroDivisionError when i == 10.
    rows, cols = b.shape
    for row in range(rows):
        for col in range(cols):
            try: stdscr.addstr(row+1, col, "%s" % b[row, col])
            except: pass

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)