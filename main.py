from time import sleep
from arm import Arm
from servo import Servo
import RPi.GPIO as GPIO

test_arm = Arm(11, 16)

test_arm.set_position(50, 30)

#for i in range(200):
#    print("moving to " + str(i))
#    test_arm.horiz_servo.set_angle(i)
#
#    i += 1



GPIO.cleanup()