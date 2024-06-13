from MPU6050 import MPU6050

class Accelerometer:

    def __init__(self):
        
        self.mpu = MPU6050()

    def get_data(self):
        '''
        returns accelerometer data as a touple (x, y)
        '''

        data = self.mpu.read_accel_data()

        return (data["x"], data["y"])