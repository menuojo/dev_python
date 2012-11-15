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
    print "couldn't find the MenuOjoServer service =("
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print "connecting to \"%s\" on %s" % (name, host)

# Create the client socket
sock = BluetoothSocket(RFCOMM)
sock.connect((host, port))

print "connected. type stuff"
logger = MouseLogger()
(x_max, y_max) = logger.mouse.screen_size()
(x_ant, y_ant) = logger.recv()

TOLERANCIA = 10

while True:
    (x, y) = logger.recv()
    if (abs(x - x_ant) > TOLERANCIA or abs(y != y_ant) > TOLERANCIA):
        x_send = float((x - x_ant)) / float(x_max)
        y_send = float((y - y_ant)) / float(y_max)
        sock.send('x={:+.4f},y={:+.4f}'.format(x_send, y_send))
        print 'x={:+.4f},y={:+.4f}'.format(x_send, y_send)
        (x_ant, y_ant) = (x, y)

sock.close()
