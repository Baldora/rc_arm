from time import sleep
from arm import Arm
from data_reader import DataReader
import RPi.GPIO as GPIO

#setup objects and variables
test_arm = Arm(16, 11)
pico_data = DataReader('/dev/ttyACM0')
loop = True
sensitivity = 2

#loop updating the arm position with data from the pico w
while loop:

    #do loop in a try so when there is an error the pins and PWM still get shutdown
    try:
        #get the data from the pico
        cords = pico_data.get_data()
        #uncomment below to test data from pico
        #print(cords)

        #convert the data to int for the servos and set sensitivity 
        x = int(float(cords["x"]) * sensitivity) 
        y = int(float(cords["y"]) * -sensitivity) 
        #uncomment below to test data from after converted
        #print("Data: x: " + str(x) + " y: " + str(y))

        #adjust the position of the arm according to data inputs
        test_arm.adjust_position(x,y)
        #uncomment below to test data for current position
        #print("Pos: x: " + str(test_arm.horiz_servo.current_angle) + " y: " + str(test_arm.vert_servo.current_angle))
    except:
        #if there is an error stop looping
        loop = False

#print that the arm is shutting down
print("\n\nshutdown!!!!!\n\n")

#Stop PWM and cleanup all the pins
test_arm.stop_arm()
GPIO.cleanup()