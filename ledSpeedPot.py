#!/usr/bin/python

# ===========================================================================
# Hatalogico for LEDs with Potentiometer - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 28/3/2015
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

# INCLUDE THE ADC DRIVER
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append("Adafruit/Adafruit_ADS1x15")
from Adafruit_ADS1x15 import ADS1x15


# SETUP THE LIBRARY FOR THE 1015 (12-bit ADC)
ADS1015 = 0x00
gain = 6144  # +/- 6.144V
sps = 250  # 250 samples per second

# FIRE UP THE ADC 1 (I2C ADDRESS IS 49 BY DEFAULT ON HATALOGICO)
adc = ADS1x15(address=0x49, ic=ADS1015)

# SETUP THE PWM DRIVER (I2C ADDRESS IS 70 BY DEFAULT ON HATALOGICO)
# EACH CHANNEL RANGES FROM 0 (off) TO 4095 (on)
pwm = PWM(0x70)
# SET FREQUENCY
pwm.setPWMFreq(1400)

while (True):
	# GET SPEED FROM POT
	# DIVIDING BY 1000 GIVES RANGE OF 5 to 0 SO ADD EXTRA ZERO TO MAX OUT AT 0.5
	potSpeed = adc.readADCSingleEnded(2, gain, sps) / 10000
	#print "Pot: %.3f" % (potSpeed)

	# SLEEP FOR PERIOD FROM POT
	time.sleep(potSpeed)

	# LOOP THROUGH ZIPPED ARRAYS AND SET EACH VALUE FOR THE 16 PWM OUTS
	for pwmPin in range(0, 16):
		pwmValue = randint(0,4095)
		pwm.setPWM(pwmPin, 0, pwmValue)

