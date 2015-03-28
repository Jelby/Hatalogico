#!/usr/bin/python

# ===========================================================================
# Hatalogico PWM Test for LEDs - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 22/3/2015
# Stolen By: John Lumley
#
# BIG THANKS TO ADAFRUIT INDUSTRIES FOR MAKING THIS POSSIBLE AND EASY
# ===========================================================================

import time, os, sys
from random import randint

# DETERMINE CURRENT PATH
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
# APPEND FOLDER OF REQUIRED LIBRARY
sys.path.append("Adafruit/Adafruit_PWM_Servo_Driver")
# FINALLY LOAD THE LIBRARY
from Adafruit_PWM_Servo_Driver import PWM

# SETUP THE PWM DRIVER (I2C ADDRESS IS 70 BY DEFAULT ON HATALOGICO)
# EACH CHANNEL RANGES FROM 0 (off) TO 4095 (on)
pwm = PWM(0x70)
# SET FREQUENCY
pwm.setPWMFreq(1400)

while (True):
	# LOOP THROUGH ZIPPED ARRAYS AND SET EACH VALUE FOR THE 16 PWM OUTS
	for pwmPin in range(0, 16):
		pwmValue = randint(0,4095)
		pwm.setPWM(pwmPin, 0, pwmValue)

		# HAVE A LITTLE NAP
		#time.sleep(0.01)