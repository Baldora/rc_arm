from libary.MPU6050 import MPU6050

class Accelerometer:
    '''This just handles getting x and y data from the MPU6050'''
    def __init__(self):
        '''creates itself using the MPU6050 libary'''
        self.mpu = MPU6050()

    def get_data(self):
        '''
        returns accelerometer data as a touple (x, y)
        '''

        data = self.mpu.read_accel_data()

        return (data["x"], data["y"])