from time import sleep
from arm import Arm
from servo import Servo
import RPi.GPIO as GPIO

test_arm = Arm(11, 16)

test_arm.vert_servo.set_angle(20)

test_arm.set_position(60,150)

GPIO.cleanup()