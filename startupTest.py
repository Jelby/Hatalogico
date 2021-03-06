#!/usr/bin/python

# ===========================================================================
# Hatalogico Startup Test - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 24/3/2015
# Author: John Lumley
#
# Use sudo crontab -e to launch the cron task manager
# Add a new line with the following (replace path to suit your machine):
# @reboot sudo python /home/pi/Hatalogico/startupTest.py
# ===========================================================================

import subprocess, sys, os, time

# DEFINE IN SECONDS HOW LONG THE LOOPING LED TEST SHOULD LAST
sleepTimeout = 20

# CHANGE THIS VALUE TO MATCH YOUR LOCAL MACHINE
pathToHere = '/home/pi/Hatalogico/'


# LAUNCH THE SECOND FILE
ledPulses = subprocess.Popen([sys.executable, pathToHere + "ledKnightRider.py"])
# SLEEP SPECIFIED AMOUTN OF TIME
time.sleep(sleepTimeout);
# AND KILL THE LOOPING PROCESS
ledPulses.kill()

# LAUNCH THE BLANKING FILE USING POPEN
flashAll = subprocess.Popen([sys.executable, pathToHere + "ledBlankAll.py"])
# WAIT FOR IT TO FINISH BEFORE MOVING ON
flashAll.communicate()

# LAUNCH THE FLASH FILE USING POPEN
blankAll = subprocess.Popen([sys.executable, pathToHere + "ledFlash.py"])
# WAIT FOR IT TO FINISH BEFORE MOVING ON
blankAll.communicate()