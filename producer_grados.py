from collections import deque
import os
import random
import signal
import sys
from threading import Lock, Timer

vector_actualizo = []
valores = [-40, -30, -15, 0, 15, 30, 40, 0]

random.seed()

data = deque([0])

old_data = 0

data_freq = 22.0

lock = Lock()

def newdata():
    global old_data
    global timer2
    timer2 = Timer(1.0 / data_freq, newdata)
    timer2.start()
    new_data = old_data
    if random.randint(1,5) < 3 :
        new_data = random.choice(valores)
        
    lock.acquire()
    data.append(new_data)
    lock.release()
    old_data = new_data


def dataout():
    global timer1
    timer1 = Timer(1.0 / data_freq, dataout)
    timer1.start()
    lock.acquire()
    print "{:0<+3d}".format(data.popleft())
    lock.release()

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

timer1 = Timer(2.0, dataout)
timer2 = Timer(0.2, newdata)


def handler(signum, frame):
    timer1.cancel()
    timer2.cancel()

signal.signal(signal.SIGINT, handler)

timer1.start()
timer2.start()
