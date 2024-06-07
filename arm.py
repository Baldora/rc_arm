from servo import Servo

class Arm:
    '''
    arm object holds the servos vertical and horizontal and handles them
    '''
    def __init__(self, vert_data_pin:int, horiz_data_pin:int):
        '''
        on arm init sets up servo data and sets the angles to 0 and 0
        '''

        self.vert_servo = Servo(vert_data_pin)
        self.horiz_servo = Servo(horiz_data_pin)

        self.vert_servo.set_angle(90)
        self.horiz_servo.set_angle(90)

    def set_position(self, x:int, y:int):
        '''
        sets the arm position for both vertical and horizontal

        x = horizontal
        y = vertical
        '''
        self.horiz_servo.set_angle(x)
        self.vert_servo.set_angle(y)


