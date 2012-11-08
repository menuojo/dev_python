from bluetooth import *
import sys

from pymouse import PyMouse


class MouseLogger:

    def __init__(self):
        self.mouse = PyMouse()

    def recv(self):
        return self.mouse.position()

addr = None

if len(sys.argv) < 2:
    print "no device specified.  Searching all nearby bluetooth devices for"
    print "the MenuOjoServer service"
else:
    addr = sys.argv[1]
    print "Searching for MenuOjoServer on %s" % addr

# search for the SampleServer service
service_matches = find_service(name="MenuOjoServer", address=addr)

if len(service_matches) == 0:
    print "couldn't find the SampleServer service =("
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print "connecting to \"%s\" on %s" % (name, host)

# Create the client socket
sock = BluetoothSocket(RFCOMM)
sock.connect((host, port))

print "connected.  type stuff"
logger = MouseLogger()
(x_max, y_max) = logger.screen_size()
(x_ant, y_ant) = logger.recv()
while True:
    (x, y) = logger.recv()
    if (x != x_ant or y != y_ant):
        x_send = (x - x_ant) / x_max
        y_send = (y - y_ant) / y_max
        sock.send('x={},y={}'.format(x_send, y_send))
        print 'x={},y={}'.format(x_send, y_send)
        (x_ant, y_ant) = (x, y)

sock.close()
