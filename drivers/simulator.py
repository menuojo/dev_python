import importlib

from drivers import Driver


class SimulatorDriver(Driver):

    def __init__(self, sim_name):
        module = importlib.import_module('drivers.simulators.' + sim_name)
        self.simulator = getattr(module, sim_name.title())()
        self.is_open = False

    def _do_open(self):
        self.is_open = True

    def _do_recv(self):
        return self.simulator.get_data()

    def _do_close(self):
        self.is_open = False
