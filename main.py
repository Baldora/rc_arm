from time import sleep
from arm import Arm
from servo import Servo
import RPi.GPIO as GPIO

test_arm = Arm(11, 16)

for i in range(20):
    test_arm.adjust_position(y_adjustment=5)
    test_arm.adjust_position(x_adjustment=-5)

    print("x: " + str(test_arm.horiz_servo.current_angle) + " y: " + str(test_arm.vert_servo.current_angle))





GPIO.cleanup()