class Driver:

    # interface
    def open(self):
        self._do_open()

    def recv(self):
        return self._do_recv()

    def close(self):
        self._do_close()

    # method that should be implemented by subclasses
    def _do_open(self):
        raise NotImplementedError("A subclass must implement this method")

    def _do_recv(self):
        raise NotImplementedError("A subclass must implement this method")

    def _do_close(self):
        raise NotImplementedError("A subclass must implement this method")
