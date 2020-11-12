import Adafruit_BBIO.GPIO as GPIO

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

GPIO.output('P2_4', 1)
GPIO.output('P2_6', 0)
GPIO.output('P2_2', 1)

GPIO.output('P2_5', 1)
GPIO.output('P2_7', 0)
GPIO.output('P2_8', 1)

GPIO.output('P1_30', 1)
GPIO.output('P1_32', 0)
GPIO.output('P1_34', 1)

GPIO.output('P1_33', 1)
GPIO.output('P1_35', 0)
GPIO.output('P1_36', 1)