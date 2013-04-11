from datetime import datetime, time
import random

from simulator import Simulator


class Simulator1(Simulator):

    values = [-40, -30, -15, 0, 15, 30, 40, 0]
    data_freq = 22.0

    def __init__(self):
        random.seed()

        self.last_data = 0
        self.timestamp = datetime.now()
        self.package = 0

    def get_data(self):
        delta = datetime.now() - self.timestamp
        if delta.total_seconds() <= 1 / self.data_freq:
            time.sleep(1 / self.data_freq - delta.total_seconds())
        new_data = self.last_data
        if random.randint(1, 5) < 3:
            new_data = random.choice(self.values)
        self.last_data = new_data
        self.package = (self.package + 1) % 256
        return 'd{:0<3d}{:0<+.4f}{:0<+3d}'.format(self.package,
                                                  random.random(), new_data)
