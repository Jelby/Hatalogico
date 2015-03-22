#!/usr/bin/python

# ===========================================================================
# Hatalogico PWM Test for LEDs - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 22/3/2015
# Stolen By: John Lumley
# ===========================================================================

import time, os, sys

# DETERMINE CURRENT PATH
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
# APPEND FOLDER OF REQUIRED LIBRARY
sys.path.append("Adafruit/Adafruit_PWM_Servo_Driver")
# FINALLY LOAD THE LIBRARY
from Adafruit_PWM_Servo_Driver import PWM

# BUILD 16 ARRAYS OF 16 POSITIONS/VALUES FOR PWM LOOP
# (USED STRARTIGHT LINEAR SCALING WHICH ISN'T AS GOOD AS A LOG, BUT IT WAS QUICKER THOUGH)
pin0 = [ 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840 ]
pin1 = [ 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584 ]
pin2 = [ 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072 ]
pin3 = [ 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560 ]
pin4 = [ 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048 ]
pin5 = [ 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536 ]
pin6 = [ 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024 ]
pin7 = [ 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0, 512 ]
pin8 = [ 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512, 0 ]
pin9 = [ 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024, 512 ]
pin10 = [ 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536, 1024 ]
pin11 = [ 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048, 1536 ]
pin12 = [ 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560, 2048 ]
pin13 = [ 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072, 2560 ]
pin14 = [ 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584, 3072 ]
pin15 = [ 3072, 2560, 2048, 1536, 1024, 512, 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3840, 3584 ]

# SETUP THE PWM DRIVER (I2C ADDRESS IS 70 BY DEFAULT ON HATALOGICO)
pwm = PWM(0x70)
# SET FREQUENCY
pwm.setPWMFreq(60)

while (True):
	# LOOP THROUGH ZIPPED ARRAYS AND SET EACH VALUE FOR THE 16 PWM OUTS
	for p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15 in zip(pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15):
		pwm.setPWM(0, 0, p0)
		pwm.setPWM(2, 0, p1)
		pwm.setPWM(4, 0, p2)
		pwm.setPWM(6, 0, p3)
		pwm.setPWM(8, 0, p4)
		pwm.setPWM(10, 0, p5)
		pwm.setPWM(12, 0, p6)
		pwm.setPWM(14, 0, p7)
		pwm.setPWM(1, 0, p8)
		pwm.setPWM(3, 0, p9)
		pwm.setPWM(5, 0, p10)
		pwm.setPWM(7, 0, p11)
		pwm.setPWM(9, 0, p12)
		pwm.setPWM(11, 0, p13)
		pwm.setPWM(13, 0, p14)
		pwm.setPWM(15, 0, p15)
		
		# HAVE A LITTLE NAP
		time.sleep(0.1)