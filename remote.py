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

        self.x = self.deadzone_adjust(accel_data[0])
        self.y = self.deadzone_adjust(accel_data[1])

    def deadzone_adjust(self, cord):

        if cord < 0 and cord > self.deadzone * -1:
            cord = 0
        elif cord > 0 and cord < self.deadzone:
            cord = 0
        elif cord > 0:
            cord -= self.deadzone
        else:
            cord += self.deadzone

        return cord
            


    def update_data_display(self):

        data_text = ["X: " + str(self.x), "Y: " + str(self.y)]
        self.screen.update_screen(data_text)