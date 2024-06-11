from servo import Servo

class Arm:
    '''
    arm object holds the servos vertical and horizontal and handles them
    '''
    def __init__(self, vert_data_pin:int, horiz_data_pin:int):
        '''
        on arm init sets up servo data and sets the angles to 90 and 90
        '''

        self.vert_servo = Servo(vert_data_pin, 15, 180)
        self.horiz_servo = Servo(horiz_data_pin, 0, 180)

        self.vert_servo.set_angle(90)
        self.horiz_servo.set_angle(90)

    def stop_arm(self):
        self.vert_servo.pwm.stop()
        self.horiz_servo.pwm.stop()

    def set_position(self, x:int, y:int):
        '''
        sets the arm position for both vertical and horizontal

        x = horizontal
        y = vertical
        '''
        self.horiz_servo.set_angle(x)
        self.vert_servo.set_angle(y)

    def adjust_position(self, x_adjustment:int = 0, y_adjustment:int = 0):
        '''
        adjust the servo angles relative to their current angle

        x = horizontal
        y = vertical
        '''
        self.horiz_servo.adjust_angle(x_adjustment)
        self.vert_servo.adjust_angle(y_adjustment)


