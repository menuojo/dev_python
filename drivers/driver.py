import logging
import logging.config

import os

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), 'log.conf'))
logger = logging.getLogger('menuojo.driver')


class Driver:

    # interface
    def open(self):
        self._do_open()

    def recv(self):
        data = self._do_recv()
        logger.info(data)
        return data

    def close(self):
        self._do_close()

    # method that should be implemented by subclasses
    def _do_open(self):
        raise NotImplementedError("A subclass must implement this method")

    def _do_recv(self):
        raise NotImplementedError("A subclass must implement this method")

    def _do_close(self):
        raise NotImplementedError("A subclass must implement this method")
