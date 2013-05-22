from serial import Serial

from driver import Driver


class SerialDriver(Driver):

    DEFAULT_DEV = '/dev/rfcomm0'
    DEFAULT_BAUD = 115200
    MAX_PACKET_SIZE = 34

    def __init__(self, dev=None, baud=None):
        self.device = dev or self.DEFAULT_BAUD
        self.baudrate = baud or self.DEFAULT_BAUD

    def _do_open(self):
        self.serial = Serial(self.device, self.baudrate)

    def _do_recv(self):
        return self.serial.read(self.MAX_PACKET_SIZE).strip()

    def _do_close(self):
        self.serial.close()
