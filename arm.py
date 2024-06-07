import servo

class Arm:
    '''
    arm object holds the servos vertical and horizontal and handles them
    '''
    def __init__(self, vert_data_pin:int, horiz_data_pin:int):
        '''
        on arm init sets up servo data and sets the angles to 0 and 0
        '''

        self.vert_servo = servo(vert_data_pin)
        self.horiz_servo = servo(horiz_data_pin)

        self.vert_servo.set_angle(0)
        self.horiz_servo.set_angle(0)

