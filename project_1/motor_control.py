"""
--------------------------------------------------------------------------
Motor Control
--------------------------------------------------------------------------
License:   
Copyright 2020 Jae Hyen Kim

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

"""
import time

import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------
motor1 = ['P2_4', 'P2_6']
motor2 = ['P2_5', 'P2_7']
motor3 = ['P1_30', 'P1_32']
motor4 = ['P1_33', 'P1_35']
    
class motors():
    motor1 = ['P2_4', 'P2_6']
    motor2 = ['P2_5', 'P2_7']
    motor3 = ['P1_30', 'P1_32']
    motor4 = ['P1_33', 'P1_35']
    
    def __init__(self):
        self._setup()
    
    def _setup(self):
        """ Set up GPIO pins """
        #front right
        GPIO.setup('P2_2',GPIO.OUT)
        GPIO.setup('P2_4',GPIO.OUT)
        GPIO.setup('P2_6',GPIO.OUT)
        
        #front left
        GPIO.setup('P2_5',GPIO.OUT)
        GPIO.setup('P2_7',GPIO.OUT)
        GPIO.setup('P2_8',GPIO.OUT)
        
        #back right
        GPIO.setup('P1_30',GPIO.OUT)
        GPIO.setup('P1_32',GPIO.OUT)
        GPIO.setup('P1_34',GPIO.OUT)
        
        #back left
        GPIO.setup('P1_33',GPIO.OUT)
        GPIO.setup('P1_35',GPIO.OUT)
        GPIO.setup('P1_36',GPIO.OUT)
        
        ''' Enable driver channels'''
        GPIO.output('P2_2', 1)
        GPIO.output('P2_8', 1)
        GPIO.output('P1_34', 1)
        GPIO.output('P1_36', 1)
        
    # End def
    
    def stop(self):
        GPIO.output('P2_4', 0)
        GPIO.output('P2_6', 0)
        GPIO.output('P2_5', 0)
        GPIO.output('P2_7', 0)
        GPIO.output('P1_30', 0)
        GPIO.output('P1_32', 0)
        GPIO.output('P1_33', 0)
        GPIO.output('P1_35', 0)
        
    # End def
        
    def setforward(self, motor):
        GPIO.output(motor[0], 1)
        GPIO.output(motor[1], 0)
        
    # End def
    
    def setbackward(self, motor):
        GPIO.output(motor[0], 0)
        GPIO.output(motor[1], 1)
        
    # End def
    
    def moveforward(self):
        self.setforward(motor=motor1)
        self.setforward(motor=motor2)
        self.setforward(motor=motor3)
        self.setforward(motor=motor4)
    
    # End def
    
    def turnleft(self):
        self.setforward(motor=motor1)
        self.setforward(motor=motor4)
        self.setbackward(motor=motor2)
        self.setbackward(motor=motor3)
        time.sleep(2)
        self.stop()
        
    # End def
    
    
    
    
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    
    Motors = motors()
    
    try:
        Motors.turnleft()

        
    except KeyboardInterrupt:
        Motors.stop()
        