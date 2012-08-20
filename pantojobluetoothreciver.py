from bluetooth import BluetoothSocket, RFCOMM
import re
import os
import sys

class PantojoBluetoothReceiver:
    
    PANTOJO_BLUETOOTH_PORT = 3
    MAX_PACKET_SIZE = 34
    
    def __init__(self):
        self.server_socket = BluetoothSocket(RFCOMM)
        self.server_socket.bind(("", self.PANTOJO_BLUETOOTH_PORT))

    def open(self):
        self.server_socket.listen(1)
        self.client_socket, self.client_info = self.server_socket.accept()
    
    def recv(self):
        return self.client_socket.recv(self.MAX_PACKET_SIZE).strip()
        
    def close(self):
        self.client_socket.close()
        self.server_socket.close()
        
class PantojoRealDataPipe:
    
    NORMALIZATION_PATTERN = r"""n(?P<packet>\d{3})
                                (?P<norm1>[+-]\d\.\d{4})
                                (?P<norm2>[+-]\d\.\d{4})
                                (?P<norm3>[+-]\d\.\d{4})
                                (?P<norm4>[+-]\d\.\d{4})"""
    CALIBRATION_PATTERN = r"""c(?P<packet>\d{3})
                              (?P<real_data>[+-]\d\.\d{4})
                              [+-]00"""
    DATA_PATTERN = r"""d(?P<packet>\d{3})
                       (?P<real_data>[+-]\d\.\d{4})
                       (?P<processed_data>[+-]\d{2})"""
    def __init__(self):
        self.normalization = re.compile(self.NORMALIZATION_PATTERN, re.VERBOSE)
        self.calibration = re.compile(self.CALIBRATION_PATTERN, re.VERBOSE)
        self.data = re.compile(self.DATA_PATTERN, re.VERBOSE)
    
    def _apply_normalization(self, input_data):
        matched = self.normalization.match(input_data)
        if matched:
            data = matched.groupdict()
            return True, "{}".format(data["norm1"])
        else:
            return False, input_data
            
    def _apply_calibration(self, input_data):
        matched = self.calibration.match(input_data)
        if matched:
            data = matched.groupdict()
            return True, "{}".format(data["real_data"])
        else:
            return False, input_data
            
    def _apply_data(self, input_data):
        matched = self.data.match(input_data)
        if matched:
            data = matched.groupdict()
            return True, "{}".format(data["real_data"])
        else:
            return False, input_data
    
    def apply(self, input_data):
        data = input_data
        funs = [_apply_normalization, _apply_calibration, _apply_data]
        for fun in funs:
            done, data = fun(data)
            if done: 
                break
        return data
        
class MenuOjoData:
    
    def __init__(self):
        self.driver = PantojoBluetoothReceiver()
        self.pipes = [PantojoRealDataPipe()]
        
    def open(self):
        self.driver.open()
        
    def recv(self):
        data = self.driver.recv()
        for pipe in self.pipes:
            data = pipe.apply(data)
        return data
    
    def close(self):
        self.driver.close()

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

device = MenuOjoData()
device.open()
while True:
    print device.recv()
device.close()
