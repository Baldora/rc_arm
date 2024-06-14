from servo import Servo

class Arm:
    '''
    arm object holds the servos as vertical and horizontal and handles them
    '''
    def __init__(self, vert_data_pin:int, horiz_data_pin:int):
        '''
        initalise the servos for the arm and sets the arms to a position of 90

        needs the pins for the servo PWM as data pin variable one horizontal and vertical
        '''

        #Create the servo objects
        self.vert_servo = Servo(vert_data_pin, 15, 180)
        self.horiz_servo = Servo(horiz_data_pin, 0, 180)

        #Set Servos to default position
        self.vert_servo.set_angle(90)
        self.horiz_servo.set_angle(90)
    
    def stop_arm(self):
        '''
        Disables and turns off the servos for the arm

        this should be run before before you code ends
        '''

        self.vert_servo.pwm.stop()
        self.horiz_servo.pwm.stop()

    def set_position(self, x:int, y:int):
        '''
        sets the arm to a position for both vertical and horizontal

        x = horizontal
        y = vertical
        '''

        self.horiz_servo.set_angle(x)
        self.vert_servo.set_angle(y)

    def adjust_position(self, x_adjustment:int = 0, y_adjustment:int = 0):
        '''
        adjust the arm position relative to their current position

        x = horizontal
        y = vertical
        '''
        
        self.horiz_servo.adjust_angle(x_adjustment)
        self.vert_servo.adjust_angle(y_adjustment)


