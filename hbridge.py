#!/usr/bin/python

# ===========================================================================
# Hatalogico Example H-Bridge Motor Driver - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 28/3/2015
# Stolen By: John Lumley
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

scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append("Adafruit/Adafruit_ADS1x15")
from Adafruit_ADS1x15 import ADS1x15


fMotorMin = 1500
fMotorMax = 4095


bMotorMin = 2500
bMotorMax = 4095

pwm = PWM(0x70)
# SET FREQUENCY
pwm.setPWMFreq(120)

pwm.setPWM(0, 0, 0)
pwm.setPWM(1, 0, 0)


gain = 6144  # +/- 6.144V
sps = 250  # 250 samples per second
ADS1015 = 0x00

# FIRE UP THE ADCS
adc1 = ADS1x15(address=0x49, ic=ADS1015)

def goForward(speedReq):
	if(speedReq > 4095):
		speedReq = 4095

	pwm.setPWM(0, 0, 0)
	pwm.setPWM(1, 0, speedReq)

def goBackward(speedReq):
	if(speedReq > 4095):
		speedReq = 4095

	pwm.setPWM(1, 0, 0)
	pwm.setPWM(0, 0, speedReq)

# WORK IN PROGRESS
while (True):
	# DRIVE A SINGLE MOTOR BASED ON A POT CONNECTED TO ANALOGUE IN 1
	reading1a = int(adc1.readADCSingleEnded(0, gain, sps))

	if(reading1a > 2048):
		outputSpeed = (reading1a - 2048) * 2
		print "FORWARD %d" % outputSpeed
		goForward(outputSpeed)
	elif(reading1a < 2048):
		outputSpeed = reading1a * 2
		print "BACKWARD %d" % outputSpeed
		goBackward(outputSpeed)

	time.sleep(0.2)
	

