from drivers import Driver


class SimulatorDriver(Driver):

    def __init__(self, sim_name):
        module = importlib.import_module('simulator')
        if hasattr(module, sim_name):
            self.simulator = getattr(module, sim_name)()
        else:
            raise ImportError("Unkown simulator. Try to import another")
        self.is_open = False

    def _do_open(self):
        self.is_open = True

    def _do_recv(self):
        return self.simulator.get_data()

    def _do_close(self):
        self.is_open = False
