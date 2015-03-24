#!/usr/bin/python

# ===========================================================================
# Hatalogico PWM Blanking Test for LEDs - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 24/3/2015
# Stolen By: John Lumley
# ===========================================================================

import os, sys

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
pwm.setPWMFreq(120)

# LOOP THROUGH THE 16 PINS - note: range goes up to but does not include the 2nd parameter
for pwmPin in range(0, 16):
	# TURN IT OFF COMPLETELY
	pwm.setPWM(pwmPin, 0, 0)