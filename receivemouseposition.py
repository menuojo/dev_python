from bluetooth import *
from pymouse import PyMouse

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

advertise_service(server_sock, "MenuOjoServer",
                  service_classes=[SERIAL_PORT_CLASS],
                  profiles=[SERIAL_PORT_PROFILE])

print "Waiting for connection on RFCOMM channel %d" % port

client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

DATA_PATTERN = r"^x=(?P<data_x>-?0\.\d+),y=(?P<data_y>-?0\.\d+)$"
dataPattern = re.compile(DATA_PATTERN, re.VERBOSE)

mouse = PyMouse()
(x_max, y_max) = mouse.screen_size()

try:
    while True:
        input_data = client_sock.recv(1024)
        matched = dataPattern.match(input_data)
        if matched:
            data = matched.groupdict()
            data_x = "{}".format(data["data_x"])
            data_y = "{}".format(data["data_y"])
            (x, y) = mouse.position()
            data_x = float(data_x)
            data_y = float(data_y)
            valor_x = int(x * (1 + data_x))
            valor_y = int(y * (1 + data_y))
            mouse.move(valor_x, valor_y)

        print "received [%s]" % data
except IOError:
    pass

print "disconnected"

client_sock.close()
server_sock.close()
print "all done"
