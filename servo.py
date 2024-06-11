from time import sleep
import RPi.GPIO as GPIO


class Servo:
    '''
    servo object controls the SG90 micro servo and handles the data pin
    '''
    def __init__(self, data_pin:int, min_angle:int, max_angle:int,):
        '''
        Setup a servo, pass the data pin as an int
        '''
        #save data pin number to self
        self.data_pin = data_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.data_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.data_pin, 50)
        self.pwm.start(0)
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.current_angle = 0

    def set_angle(self, angle:int):
        '''
        Pass an angle as an int and the servo moves to that angle
        '''

        #check the angle is within min and max
        if angle > self.max_angle:
            angle = self.max_angle
        if angle < self.min_angle:
            angle = self.min_angle

        #set the current_angle
        self.current_angle = angle

        

        #set the servo to the angle
        duty = angle /18 + 2
        GPIO.output(self.data_pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(0.1)
        GPIO.output(self.data_pin, False)
        self.pwm.ChangeDutyCycle(duty)

        return
    
    def adjust_angle(self, angle_change:int):
        '''
        Set an angle change relative to current position
        '''

        new_angle = self.current_angle + angle_change
        
        #check the angle is within min and max
        if new_angle > self.max_angle:
            new_angle = self.max_angle
        if new_angle < self.min_angle:
            new_angle = self.min_angle

        #set the angle
        self.set_angle(new_angle)