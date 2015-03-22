#!/usr/bin/python

import time, os, signal, sys

# INCLUDE THE ADC DRIVER
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append("Adafruit/Adafruit_ADS1x15")
from Adafruit_ADS1x15 import ADS1x15

# INCLUDE THE DAC DRIVER
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append("Adafruit/Adafruit_MCP4725")
from Adafruit_MCP4725 import MCP4725

# ===========================================================================
# Hatalogico core - powered by Adafruit's Libraries
# ===========================================================================

# Select the gain
# gain = 6144  # +/- 6.144V
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# Select the sample rate
# sps = 8    # 8 samples per second
# sps = 16   # 16 samples per second
# sps = 32   # 32 samples per second
sps = 64   # 64 samples per second
# sps = 128  # 128 samples per second
# sps = 250  # 250 samples per second
# sps = 475  # 475 samples per second
# sps = 860  # 860 samples per second

DAC1_7Bit = \
[ 2048, 2148, 2248, 2348, 2447, 2545, 2642, 2737,
  2831, 2923, 3013, 3100, 3185, 3267, 3346, 3423,
  3495, 3565, 3630, 3692, 3750, 3804, 3853, 3898,
  3939, 3975, 4007, 4034, 4056, 4073, 4085, 4093,
  4095, 4093, 4085, 4073, 4056, 4034, 4007, 3975,
  3939, 3898, 3853, 3804, 3750, 3692, 3630, 3565,
  3495, 3423, 3346, 3267, 3185, 3100, 3013, 2923,
  2831, 2737, 2642, 2545, 2447, 2348, 2248, 2148,
  2048, 1947, 1847, 1747, 1648, 1550, 1453, 1358,
  1264, 1172, 1082,  995,  910,  828,  749,  672,
   600,  530,  465,  403,  345,  291,  242,  197,
   156,  120,   88,   61,   39,   22,   10,    2,
     0,    2,   10,   22,   39,   61,   88,  120,
   156,  197,  242,  291,  345,  403,  465,  530,
   600,  672,  749,  828,  910,  995, 1082, 1172,
  1264, 1358, 1453, 1550, 1648, 1747, 1847, 1947 ]

DAC2_7Bit = \
[ 3495, 3423, 3346, 3267, 3185, 3100, 3013, 2923,
  2831, 2737, 2642, 2545, 2447, 2348, 2248, 2148,
  2048, 1947, 1847, 1747, 1648, 1550, 1453, 1358,
  1264, 1172, 1082,  995,  910,  828,  749,  672,
   600,  530,  465,  403,  345,  291,  242,  197,
   156,  120,   88,   61,   39,   22,   10,    2,
     0,    2,   10,   22,   39,   61,   88,  120,
   156,  197,  242,  291,  345,  403,  465,  530,
   600,  672,  749,  828,  910,  995, 1082, 1172,
  1264, 1358, 1453, 1550, 1648, 1747, 1847, 1947,
  2048, 2148, 2248, 2348, 2447, 2545, 2642, 2737,
  2831, 2923, 3013, 3100, 3185, 3267, 3346, 3423,
  3495, 3565, 3630, 3692, 3750, 3804, 3853, 3898,
  3939, 3975, 4007, 4034, 4056, 4073, 4085, 4093,
  4095, 4093, 4085, 4073, 4056, 4034, 4007, 3975,
  3939, 3898, 3853, 3804, 3750, 3692, 3630, 3565 ]

# SETUP THE LIBRARY FOR THE 1015 (12-bit ADC)
ADS1015 = 0x00

# FIRE UP THE ADCS
adc1 = ADS1x15(address=0x48, ic=ADS1015)
adc2 = ADS1x15(address=0x49, ic=ADS1015)

# FIRE UP THE DACS
dac1 = MCP4725(0x60)
dac2 = MCP4725(0x61)

while (True):
	# LOOP THROUGH THE ZIPPED ARRAYS
	# EACH TIME PUTTING OUT THE TWO VALUES ONTO THE TWO DACS	
	for voltage1, voltage2 in zip(DAC1_7Bit, DAC2_7Bit):
		# OUTPUT TO THE DACS
		dac1.setVoltage(voltage1)
		dac2.setVoltage(voltage2)

		print "DAC1 = %.0f" % (voltage1)
		print "DAC2 = %.0f" % (voltage2)
		time.sleep(2)

		# READ ALL 4 VALUES FROM FIRST ADC
		reading1a = adc1.readADCSingleEnded(0, gain, sps) / 1000
		reading1b = adc1.readADCSingleEnded(1, gain, sps) / 1000
		reading1c = adc1.readADCSingleEnded(2, gain, sps) / 1000
		reading1d = adc1.readADCSingleEnded(3, gain, sps) / 1000

		# READ ALL 4 VALUES FROM SECOND ADC
		reading2a = adc2.readADCSingleEnded(0, gain, sps) / 1000
		reading2b = adc2.readADCSingleEnded(1, gain, sps) / 1000
		reading2c = adc2.readADCSingleEnded(2, gain, sps) / 1000
		reading2d = adc2.readADCSingleEnded(3, gain, sps) / 1000
		
		print "ADC1: a = %.3f" % (reading1a) + " b = %.3f" % (reading1b) + " c = %.3f" % (reading1c) + " d = %.3f" % (reading1d)
		print "ADC2: a = %.3f" % (reading2a) + " b = %.3f" % (reading2b) + " c = %.3f" % (reading2c) + " d = %.3f" % (reading2d)
		print "-------------------------------------------------------------"
		
		# HAVE A LITTLE NAP
		time.sleep(3)