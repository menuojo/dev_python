from select import select
import signal
import sys
from threading import Lock, Thread

import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = []

lock = Lock()

def newdata():
    finish = False
    while not finish:
        read_list, unused, unused = select([sys.stdin], [], [])
        for f in read_list:
            line = f.readline()
            if len(line) == 0:
                finish = True
            elif line[-1] == "\n":
                line = line[:-1]
                lock.acquire()
                data.append(float(line))
                lock.release()               

thread = Thread(target=newdata)
thread.start()

def update_line(num, data, line):
    lock.acquire()
    if len(data) < 120:
        x = range(1, len(data) + 1)
        y = data[:]
        line.set_data(x, y)
    else:
        x = range(1, 121)
        y = data[-120:]
        line.set_data(x, y)
    lock.release()
    return line,

fig1 = plt.figure()

l, = plt.plot([], [], 'b-')
plt.xlim(0, 120)
plt.ylim(-4, 4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 10, fargs=(data, l),
                                   interval=50, blit=True)

plt.show()

