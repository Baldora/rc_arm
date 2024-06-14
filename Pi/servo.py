from time import sleep
import RPi.GPIO as GPIO


class Servo:
    '''
    servo object controls the SG90 micro servo and handles the pwm over the data pin
    '''
    def __init__(self, data_pin:int, min_angle:int = 0, max_angle:int = 180):
        '''
        Setup the servo pins and set limits for the servo
        '''
        #save data pin number to self
        self.data_pin = data_pin
        #setup the data pin and start the PWM
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.data_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.data_pin, 50)
        self.pwm.start(0)

        #set variables for servo limits and current angle (will always start at 0 even if not current position)
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.current_angle = 0

    def set_angle(self, angle:int , pause_timer:float = 0.0):
        '''
        Sets the servo position to an angle given as an int
        '''

        #check the angle is within min and max
        if angle > self.max_angle:
            angle = self.max_angle
        if angle < self.min_angle:
            angle = self.min_angle

        #set the current_angle
        self.current_angle = angle

        #set the pwm and send it over data pin to set the angle
        duty = angle /18 + 2
        GPIO.output(self.data_pin, True)
        self.pwm.ChangeDutyCycle(duty)

        sleep(pause_timer)
        
        GPIO.output(self.data_pin, False)
        self.pwm.ChangeDutyCycle(duty)
    
    def adjust_angle(self, angle_change:int):
        '''
        Set an angle change relative to current position
        '''
        #get new angle desired
        new_angle = self.current_angle + angle_change
        
        #check the angle is within min and max -- if not then set it to the limit 
        if new_angle > self.max_angle:
            new_angle = self.max_angle
        if new_angle < self.min_angle:
            new_angle = self.min_angle

        #set the angle
        self.set_angle(new_angle)
