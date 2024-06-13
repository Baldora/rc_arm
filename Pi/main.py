from time import sleep
from arm import Arm
from data_reader import DataReader
import RPi.GPIO as GPIO

test_arm = Arm(16, 11)
pico_data = DataReader('/dev/ttyACM0')
loop = True

while loop:
    try:
        cords = pico_data.get_data()

        #print(cords)
        x = int(float(cords["x"]) * 3) 
        y = int(float(cords["y"]) * -3) 

        #print("Data: x: " + str(x) + " y: " + str(y))

        test_arm.adjust_position(x,y)

        print("Pos: x: " + str(test_arm.horiz_servo.current_angle) + " y: " + str(test_arm.vert_servo.current_angle))
    except:
        loop = False




print("\n\nshutdown!!!!!\n\n")
test_arm.stop_arm()
GPIO.cleanup()