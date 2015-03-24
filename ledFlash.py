#!/usr/bin/python

# ===========================================================================
# Hatalogico PWM FLASH Test for LEDs - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 24/3/2015
# Stolen By: John Lumley
# ===========================================================================

import os, sys, time

# DETERMINE CURRENT PATH
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
# APPEND FOLDER OF REQUIRED LIBRARY
sys.path.append("Adafruit/Adafruit_PWM_Servo_Driver")
# FINALLY LOAD THE LIBRARY
from Adafruit_PWM_Servo_Driver import PWM

# DEFINE NUMBER OF FLASHES
flashCount = 2
# DEFINE FLASH ON TIME
flashTime = 0.5

# SETUP THE PWM DRIVER (I2C ADDRESS IS 70 BY DEFAULT ON HATALOGICO)
# EACH CHANNEL RANGES FROM 0 (off) TO 4095 (on)
pwm = PWM(0x70)
# SET FREQUENCY
pwm.setPWMFreq(120)

for currentFlash in range(0, flashCount):
	# LOOP THROUGH THE 16 PINS - note: range goes up to but does not include the 2nd parameter
	for pwmPin in range(0, 16):
		# TURN IT ON
		pwm.setPWM(pwmPin, 0, 4095)

	time.sleep(flashTime)

	for pwmPin in range(0, 16):
		# TURN IT ON
		pwm.setPWM(pwmPin, 0, 0)

	time.sleep(flashTime)