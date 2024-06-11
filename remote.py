from time import sleep_ms
from accelerometer import Accelerometer
from screen import Screen

class Remote:
    def __init__(self):
        
        self.screen = Screen(3, 2, 128, 64)
        self.accelerometer = Accelerometer()

        #set a deadzone for the remote
        self.deadzone = 1

        self.x = 0
        self.y = 0

    def update_cords(self):

        accel_data = self.accelerometer.get_data()

        for data in accel_data:
            if data < 0 and data > self.deadzone * -1:
                data = 0
            if data > 0 and data < self.deadzone:
                data = 0

        self.x = accel_data[0]
        self.y = accel_data[1]

    def update_data_display(self):

        data_text = ["X: " + str(self.x), "Y: " + str(self.y)]
        self.screen.update_screen(data_text)