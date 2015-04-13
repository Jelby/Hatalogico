#!/usr/bin/python

# ===========================================================================
# Hatalogico Startup Test - powered by Adafruit's Libraries
# -------------------------------------------------
# Date: 24/3/2015
# Author: John Lumley
#
# Use sudo crontab -e to launch the cron task manager
# Add a new line with the following (replace path to suit your machine):
# @reboot ~/Hatalogico/startupTest.py
# ===========================================================================

import subprocess, sys, os, time

# DEFINE IN SECONDS HOW LONG THE LOOPING LED TEST SHOULD LAST
sleepTimeout = 10

# CHANGE THIS VALUE TO MATCH YOUR LOCAL MACHINE
pathToHere = '~/Hatalogico/'

# LAUNCH THE FIRST FILE USING POPEN
oneByOne = subprocess.Popen([sys.executable, pathToHere + "led1by1.py"])
# WAIT FOR IT TO FINISH BEFORE MOVING ON - note: you can use std pipes here if needed
oneByOne.communicate()

# LAUNCH THE SECOND FILE
ledPulses = subprocess.Popen([sys.executable, pathToHere + "ledKnightRider.py"])
# SLEEP SPECIFIED AMOUTN OF TIME
time.sleep(sleepTimeout);
# AND KILL THE LOOPING PROCESS
ledPulses.kill()

# LAUNCH THE BLANKING FILE USING POPEN
blankAll = subprocess.Popen([sys.executable, pathToHere + "ledBlankAll.py"])
# WAIT FOR IT TO FINISH BEFORE MOVING ON
blankAll.communicate()

# LAUNCH THE FLASH FILE USING POPEN
blankAll = subprocess.Popen([sys.executable, pathToHere + "ledFlash.py"])
# WAIT FOR IT TO FINISH BEFORE MOVING ON
blankAll.communicate()