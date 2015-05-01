#!/usr/bin/python

# ===========================================================================
# Hatalogico Example H-Bridge Motor Driver - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 21/4/2015
# SWritten By: John Lumley
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

fMotorMin = 1500 #MINIMUM TO TURN THE MOTOR OVER
fMotorMax = 4095

bMotorMin = 2500 #MINIMUM TO TURN THE MOTOR OVER
bMotorMax = 4095

pwm = PWM(0x70)
# SET FREQUENCY
pwm.setPWMFreq(120)

pwm.setPWM(0, 0, 0)
pwm.setPWM(1, 0, 0)
pwm.setPWM(2, 0, 0)
pwm.setPWM(3, 0, 0)
time.sleep(5)

gain = 6144  # +/- 6.144V
sps = 250  # 250 samples per second
ADS1015 = 0x00

# FIRE UP THE ADCS
adc1 = ADS1x15(address=0x49, ic=ADS1015)

def goForward(speedReq):
	if(speedReq > 4095):
		speedReq = 4095

	pwm.setPWM(3, 0, 0)
	pwm.setPWM(2, 0, speedReq)

def goBackward(speedReq):
	if(speedReq > 4095):
		speedReq = 4095

	pwm.setPWM(2, 0, 0)
	pwm.setPWM(3, 0, speedReq)

def goLeft(speedReq):
	if(speedReq > 4095):
		speedReq = 4095

	pwm.setPWM(0, 0, 0)
	pwm.setPWM(1, 0, speedReq)

def goRight(speedReq):
	if(speedReq > 4095):
		speedReq = 4095

	pwm.setPWM(1, 0, 0)
	pwm.setPWM(0, 0, speedReq)


# BASIC LOOP (NOT CONTROLLER INPUT)
while (True):
	# RANDOM DRIVING TO TEST FUNCTIONALITY
	goLeft(2400)
	goForward(1800)
	time.sleep(5)
	goBackward(1000)
	time.sleep(5)
	
	goRight(2400)
	goForward(2500)
	time.sleep(5)
	goBackward(1800)
	time.sleep(5)
	
	goLeft(4095)
	goForward(4095)
	time.sleep(5)
	goBackward(4095)
	time.sleep(5)

	goRight(4095)
	goForward(0)
	time.sleep(2)

	goLeft(4095)
	time.sleep(1)
	goRight(4095)
	time.sleep(1)
