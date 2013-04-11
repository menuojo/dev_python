from bluetooth import BluetoothSocket, RFCOMM

from driver import Driver


class BluetoothDriver(Driver):

    PANTOJO_BLUETOOTH_PORT = 3
    MAX_PACKET_SIZE = 34

    def __init__(self):
        self.server_socket = BluetoothSocket(RFCOMM)
        self.server_socket.bind(("", self.PANTOJO_BLUETOOTH_PORT))

    def _do_open(self):
        self.server_socket.listen(1)
        self.client_socket, self.client_info = self.server_socket.accept()

    def _do_recv(self):
        return self.client_socket.recv(self.MAX_PACKET_SIZE).strip()

    def _do_close(self):
        self.client_socket.close()
        self.server_socket.close()
