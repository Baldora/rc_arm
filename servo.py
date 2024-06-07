from time import sleep
import RPi.GPIO as GPIO


class Servo:
    '''
    servo object controls the SG90 micro servo and handles the data pin
    '''
    def __init__(self, data_pin:int):
        '''
        Setup a servo, pass the data pin as an int
        '''
        #save data pin number to self
        self.data_pin = data_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(data_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(data_pin, 50)

    def set_angle(self, angle:int):
        '''
        Pass an angle as an int and the servo moves to that angle
        '''
        duty = angle /18 + 2
        GPIO.output(self.data_pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.data_pin, False)
        self.pwm.ChangeDutyCycle(duty)

        return
    