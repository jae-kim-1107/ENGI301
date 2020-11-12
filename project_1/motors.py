import time
import random

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# Peripheral path
GPIO_BASE_PATH               = "/sys/class/gpio"
ADC_BASE_PATH                = "/sys/bus/iio/devices/iio:device0"

# GPIO direction (if it is outputting or inputting a signal to the GPIO)
IN                           = True
OUT                          = False

# GPIO output state
LOW                          = "0"
HIGH                         = "1"

#Motor 1 
motor_1_ln1 				 = (0,30) #gpio30 P2_P5
motor_1_ln2					 = (0,31) #gpio31 P2_P7
motor_1_en1  				 = (1,28) #gpio60 P2_P8

#Motor 2
motor_2_ln4					 = (1,25) #gpio57 P2_P6
motor_2_ln3					 = (1,26) #gpio58 P2_P4
motor_2_en3					 = (1,27) #gpio59 P2_P2

#Motor 3
motor_3_ln1					 = (1,10) #gpio42 P1_P32
motor_3_ln2					 = (1,11) #gpio43 P1_P30
motor_3_en1					 = (0,26) #gpio26 P1_34

#Motor4
motor_4_ln4					 = (3,15) #gpio111 P1_33
motor_4_ln3					 = (2,24) #gpio88 P1_35
motor_4_en3					 = (3,14) #gpio110 P1_36

motor1						 = (motor_1_ln1, motor_1_ln2, motor_1_en1)
motor2						 = (motor_2_ln3, motor_2_ln4, motor_2_en3)
motor3						 = (motor_3_ln1, motor_3_ln2, motor_3_en1)
motor4						 = (motor_4_ln3, motor_4_ln4, motor_4_en3)


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

start_time                    = 30.0              # Start time (in seconds)


# ------------------------------------------------------------------------
# GPIO / ADC access library
# ------------------------------------------------------------------------
import os

def gpio_get(gpio):
    """Get GPIO input value."""
    gpio_number = str((gpio[0] * 32) + gpio[1])
    path        = "{0}/gpio{1}".format(GPIO_BASE_PATH, gpio_number)
    
    # "cat {path}/value"
    with open("{0}/value".format(path), 'r') as f:
        out = f.read()
    
    return float(out)

# End def

    
def setforward(motor):
	gpio_set(motor[0],HIGH)
	gpio_set(motor[1],LOW)
	
#End def
def setbackward(motor):
	gpio_set(motor[0],LOW)
	gpio_set(motor[1],HIGH)
	
#End def

	
def move():
	gpio_set(motor1[2],HIGH)
	gpio_set(motor2[2],HIGH)
	gpio_set(motor3[2],HIGH)
	gpio_set(motor4[2],HIGH)

#End def
	
def stop():
	gpio_set(motor1[2],LOW)
	gpio_set(motor2[2],LOW)
	gpio_set(motor3[2],LOW)
	gpio_set(motor4[2],LOW)

#End def

def setleft():

	"""move the left wheels forward"""
	setforward(motor1)
	setforward(motor3)
	
	"""move the right wheels backward"""
	setbackward(motor2)
	setbackward(motor4)
	
#End def

def setright():
	"""move the left wheels backward"""
	
	setbackward(motor1)
	setbackward(motor3)
	
	"""move the right wheels forward"""
	setforward(motor2)
	setforward(motor4)

#End def


def setupcar():
	"""Setup gpio"""
	gpio_setup(motor_1_ln1, OUT, LOW)
	gpio_setup(motor_1_ln2, OUT, LOW)
	gpio_setup(motor_1_en1, OUT, LOW)

	"""motor 2"""
	gpio_setup(motor_2_ln3, OUT, LOW)
	gpio_setup(motor_2_ln4, OUT, LOW)
	gpio_setup(motor_2_en3, OUT, LOW)
	
	"""motor 3"""
	gpio_setup(motor_3_ln1, OUT, LOW)
	gpio_setup(motor_3_ln2, OUT, LOW)
	gpio_setup(motor_3_en1, OUT, LOW)
	
	"""motor 4"""
	gpio_setup(motor_4_ln3, OUT, LOW)
	gpio_setup(motor_4_ln4, OUT, LOW)
	gpio_setup(motor_4_en3, OUT, LOW)
	
#End def

def drive_forward(drivetime):
    setforward(motor1)
    setforward(motor2)
    setforward(motor3)
    setforward(motor4)
    move()
    time.sleep(drivetime)
    stop()
  	
#End def

def drive_backward(drivetime):
    setbackward(motor1)
    setbackward(motor2)
    setbackward(motor3)
    setbackward(motor4)
    move()
    time.sleep(drivetime)
    stop()
  	
#End def
  	
def drive_right(drivetime):
    setright()
    move()
    time.sleep(drivetime)
    stop()
#End def

def drive_left(drivetime):
    setleft()
    move()
    time.sleep(drivetime)
    stop()
#End def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    setupcar()
    while (True):
        if gpio_get(ard1):
           # print("Forward")
            drive_forward(0.5)
        if gpio_get(ard2):
            #print("Backward")
            drive_backward(0.5)
        if gpio_get(ard3):
            #print("Right")
            drive_right(0.5)
        if gpio_get(ard4):
           # print("Left")
            drive_left(0.5)