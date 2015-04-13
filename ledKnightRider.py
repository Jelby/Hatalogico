#!/usr/bin/python

# ===========================================================================
# Hatalogico KNIGHT RIDER for LEDs - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 12/4/2015
# Author: John Lumley
#
# BIG THANKS TO ADAFRUIT INDUSTRIES FOR MAKING THIS POSSIBLE AND EASY
# ===========================================================================

import time, os, sys

# DETERMINE CURRENT PATH
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
# APPEND FOLDER OF REQUIRED LIBRARY
sys.path.append("Adafruit/Adafruit_PWM_Servo_Driver")
# FINALLY LOAD THE LIBRARY
from Adafruit_PWM_Servo_Driver import PWM

LED_PIN_0 = 1
LED_PIN_1 = 3
LED_PIN_2 = 5
LED_PIN_3 = 7
LED_PIN_4 = 9
LED_PIN_5 = 11
LED_PIN_6 = 13
LED_PIN_7 = 15

BRIGHT_STEP_0=4095
BRIGHT_STEP_1=1024
BRIGHT_STEP_2=512
BRIGHT_STEP_3=256
BRIGHT_STEP_4=0
BRIGHT_STEP_5=0
BRIGHT_STEP_6=0
BRIGHT_STEP_7=0

# BUILD 16 ARRAYS OF 16 POSITIONS/VALUES FOR PWM LOOP
position0 = [ BRIGHT_STEP_0, BRIGHT_STEP_1, BRIGHT_STEP_2, BRIGHT_STEP_3, BRIGHT_STEP_4, BRIGHT_STEP_5, BRIGHT_STEP_6, BRIGHT_STEP_7]
position1 = [ BRIGHT_STEP_1, BRIGHT_STEP_0, BRIGHT_STEP_1, BRIGHT_STEP_2, BRIGHT_STEP_3, BRIGHT_STEP_4, BRIGHT_STEP_5, BRIGHT_STEP_6]
position2 = [ BRIGHT_STEP_2, BRIGHT_STEP_1, BRIGHT_STEP_0, BRIGHT_STEP_1, BRIGHT_STEP_2, BRIGHT_STEP_3, BRIGHT_STEP_4, BRIGHT_STEP_5]
position3 = [ BRIGHT_STEP_3, BRIGHT_STEP_2, BRIGHT_STEP_1, BRIGHT_STEP_0, BRIGHT_STEP_1, BRIGHT_STEP_2, BRIGHT_STEP_3, BRIGHT_STEP_4]
position4 = [ BRIGHT_STEP_4, BRIGHT_STEP_3, BRIGHT_STEP_2, BRIGHT_STEP_1, BRIGHT_STEP_0, BRIGHT_STEP_1, BRIGHT_STEP_2, BRIGHT_STEP_3]
position5 = [ BRIGHT_STEP_5, BRIGHT_STEP_4, BRIGHT_STEP_3, BRIGHT_STEP_2, BRIGHT_STEP_1, BRIGHT_STEP_0, BRIGHT_STEP_1, BRIGHT_STEP_2]
position6 = [ BRIGHT_STEP_6, BRIGHT_STEP_5, BRIGHT_STEP_4, BRIGHT_STEP_3, BRIGHT_STEP_2, BRIGHT_STEP_1, BRIGHT_STEP_0, BRIGHT_STEP_1]
position7 = [ BRIGHT_STEP_7, BRIGHT_STEP_6, BRIGHT_STEP_5, BRIGHT_STEP_4, BRIGHT_STEP_3, BRIGHT_STEP_2, BRIGHT_STEP_1, BRIGHT_STEP_0]

# SETUP THE PWM DRIVER (I2C ADDRESS IS 70 BY DEFAULT ON HATALOGICO)
# EACH CHANNEL RANGES FROM 0 (off) TO 4095 (on)
pwm = PWM(0x70)
# SET FREQUENCY
pwm.setPWMFreq(120)

while (True):
	# LOOP THROUGH ZIPPED ARRAYS AND SET EACH VALUE FOR THE 16 PWM OUTS
	for p0, p1, p2, p3, p4, p5, p6, p7 in zip(position0, position1, position2, position3, position4, position5, position6, position7):
		pwm.setPWM(LED_PIN_0, 0, p0)
		pwm.setPWM(LED_PIN_1, 0, p1)
		pwm.setPWM(LED_PIN_2, 0, p2)
		pwm.setPWM(LED_PIN_3, 0, p3)
		pwm.setPWM(LED_PIN_4, 0, p4)
		pwm.setPWM(LED_PIN_5, 0, p5)
		pwm.setPWM(LED_PIN_6, 0, p6)
		pwm.setPWM(LED_PIN_7, 0, p7)
		
		# HAVE A LITTLE NAP
		time.sleep(0.1)

	for p0, p1, p2, p3, p4, p5, p6, p7 in reversed(zip(position0, position1, position2, position3, position4, position5, position6, position7)):
		pwm.setPWM(LED_PIN_0, 0, p0)
		pwm.setPWM(LED_PIN_1, 0, p1)
		pwm.setPWM(LED_PIN_2, 0, p2)
		pwm.setPWM(LED_PIN_3, 0, p3)
		pwm.setPWM(LED_PIN_4, 0, p4)
		pwm.setPWM(LED_PIN_5, 0, p5)
		pwm.setPWM(LED_PIN_6, 0, p6)
		pwm.setPWM(LED_PIN_7, 0, p7)
		
		# HAVE A LITTLE NAP
		time.sleep(0.1)