from time import sleep
import RPi.GPIO as GPIO


class Servo:
    '''
    servo object controls the SG90 micro servo and handles the data pin
    '''
    def __init__(self, data_pin:int, ):#max_angle:int, min_angle:int):
        '''
        Setup a servo, pass the data pin as an int
        '''
        #save data pin number to self
        self.data_pin = data_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.data_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.data_pin, 50)
        self.pwm.start(0)
        #self.max_angle = max_angle
        #self.min_angle = min_angle

    def set_angle(self, angle:int):
        '''
        Pass an angle as an int and the servo moves to that angle
        '''
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.data_pin, GPIO.OUT)

        duty = angle /18 + 2
        GPIO.output(self.data_pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.data_pin, False)
        self.pwm.ChangeDutyCycle(duty)

        return
    