from collections import deque
from datetime import datetime
import os
import random
import signal
import sys
from threading import Lock, Timer

quiet = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
move_left = [1, 2, 1, 0, -2, -5, -9, -5, -2, -1, 0]
move_right = [-1, -2, -1, 0, 2, 5, 9, 5, 2, 1, 0]

std_dev = 0.25
data_freq = 22.0

random.seed()

data = deque([])
data.extend(map(lambda x: x + random.uniform(-std_dev, std_dev), quiet))

lock = Lock()

roulette = [quiet, quiet, move_left, move_right]

def newdata():
    global timer2
    timer2 = Timer(1.0 / (data_freq / len(quiet)), newdata)
    timer2.start()
    new_data = map(lambda x: x + random.uniform(-std_dev, std_dev), random.choice(roulette))
    lock.acquire()
    data.extend(new_data)
    lock.release()

def dataout():
    global timer1
    timer1 = Timer(1.0 / data_freq, dataout)
    timer1.start()
    lock.acquire()
    print "{:+.3f}".format(data.popleft())
    lock.release()
    
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

timer1 = Timer(0.1, dataout)
timer2 = Timer(0.2, newdata)

def handler(signum, frame):
    timer1.cancel()
    timer2.cancel()
    
signal.signal(signal.SIGINT, handler)

timer1.start()
timer2.start()
    
