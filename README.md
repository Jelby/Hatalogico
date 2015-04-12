##Hatalogico
Libraries for the Hatalogico Raspberry Pi Hat

All the python files required to drive the I2C chips on the Hatalogico were written and are maintained by [Adafruit Industries](https://www.adafruit.com/). I have simply included them as submodules and written a few examples using them.

Before using these files, you need to setup your Pi for GPIO and I2C (note the Pi 2 has a slightly different method for the latter).

[Setting up the I2C](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

[Setting up the GPIO](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-gpio)

##Installing
The RPi2 is slightly different but I recommend you 'apt-get' the following packages on both platforms:

**sudo apt-get update -y**
**sudo apt-get purge -y wolfram-engine**
**sudo apt-get install -y python-dev python-rpi.gpio python-smbus**
**sudo apt-get install -y i2c-tools libi2c-dev**

You can copy and paste all 4 lines into your terminal and they will run one after the other (synchronously).

You will need to add the I2C tools to both versions:
**sudo nano /etc/modules**
Scroll to the bottom and add:
**i2c-dev**

###For RPi B+ and older only:
Also add a new line underneath 'i2c-dev':
**i2c-bcm2708**

Crtl-X to close, pressing Y to save the changes (overwrite with the same name by pressing enter)
For the RPi B+ or older you will need to update the blacklist file:
#sudo nano /etc/modprobe.d/raspi-blacklist.conf
Update it to read:
\#blacklist spi-bcm2708

\#blacklist i2c-bcm2708

##I2C addresses
(on the prototype model)

1. 16 Channel PWM: **0x70**
2. 4 Channel ADC #1: **0x49**
3. 4 Channel ADC #2: **0x48**
4. Single Channel DAC #1: **0x60**
5. Single Channel DAC #2: **0x61**


###Big thanks to Adafruit without whom the Hatalogico would just be a mug coaster.
