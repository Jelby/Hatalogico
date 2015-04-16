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

# INCLUDE THE ADC DRIVER
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append("Adafruit/Adafruit_ADS1x15")
from Adafruit_ADS1x15 import ADS1x15


# SETUP THE LIBRARY FOR THE 1015 (12-bit ADC)
ADS1015 = 0x00
gain = 6144  # +/- 6.144V
sps = 20  # 250 samples per second

# FIRE UP THE ADC 1 (I2C ADDRESS IS 49 BY DEFAULT ON HATALOGICO)
adc = ADS1x15(address=0x49, ic=ADS1015)

ldr_mininum = 1
ldr_maximum = 2800
ldr_difference = ldr_maximum - ldr_mininum

while (True):
	# GET SPEED FROM POT
	ldrValue = adc.readADCSingleEnded(1, gain, sps)

	if(ldrValue > ldr_maximum):
		ldrValue = ldr_maximum
	elif(ldrValue < ldr_mininum):
		ldrValue = ldr_mininum

	ldrNormalised = ldrValue - ldr_mininum

	eachPerc = ldr_difference / 100
	ldrPerc = int(ldrNormalised / eachPerc)

	if(ldrPerc > 100):
		ldrPerc = 100
	elif(ldrPerc < 0):
		ldrPerc = 0;

	os.system('clear')
	print "CURRENT LIGHT LEVEL"
	print "PERCENTAGE: %d" % ldrPerc + "%"
	print "RAW VALUE: %d" % (ldrValue)

	# SLEEP FOR PERIOD FROM POT
	time.sleep(0.3)