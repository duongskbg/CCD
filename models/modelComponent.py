import cv2, time
from models.modelData import dRS232
from serial import Serial

class Component():
    def __init__(self, box, label = -1, prob = 1.0, smallest_distance = -1, match_comp = -1, ok_status=False):
        self.box = box
        self.label = label
        self.prob = prob
        self.smallest_distance = smallest_distance
        self.match_comp = match_comp
        self.ok_status = ok_status
        
class Camera():    
    def __init__(self, usb_port = 0):
        self.usb_port = usb_port
        self.camera = cv2.VideoCapture(self.usb_port)
        
    def change_default_settings(self, exposure, resolution_width, resolution_height, brightness, contrast, hue, saturation,\
                                sharpness, gamma, white_balance, gain):
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution_height)
        if exposure != 256:
            self.camera.set(cv2.CAP_PROP_EXPOSURE, exposure)
        else:
            self.camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
        self.camera.set(cv2.CAP_PROP_CONTRAST, contrast)
        self.camera.set(cv2.CAP_PROP_SATURATION, saturation)
        self.camera.set(cv2.CAP_PROP_SHARPNESS, sharpness)
        self.camera.set(cv2.CAP_PROP_GAMMA, gamma)        
        if white_balance > 0:
            self.camera.set(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U, white_balance)
            self.camera.set(cv2.CAP_PROP_WHITE_BALANCE_RED_V, white_balance)
        else:
            self.camera.set(cv2.CAP_PROP_AUTO_WB, 0)    
        self.camera.set(cv2.CAP_PROP_GAIN, gain)
        
    def take_pic(self):
        _, img = self.camera.read()
        _, img = self.camera.read()
        return img

class mRS232():
    def __init__(self):
        self.data = dRS232()
        try:            
            self.serial_port = Serial(
                port=self.data.port,
                baudrate=self.data.baud_rate,
                parity=self.data.parity )
        except:
            pass
        
    def send_data(self, data):
        try:
            if self.serial_port.isOpen():
                self.serial_port.write(data)
                time.sleep(1)
        except:
            pass
        
    def close_port(self):
        try:
            if self.serial_port.isOpen():
                self.serial_port.close()
        except:
            pass