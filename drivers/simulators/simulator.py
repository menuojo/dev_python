class Simulator:

    # interface
    def get_data(self):
        return self._do_get_data()

    # method that should be implemented by subclasses
    def _do_get_data(self):
        raise NotImplementedError("A subclass must implement this method")
