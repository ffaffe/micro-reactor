import board
import busio
import adafruit_tsl2591
import time
from time import sleep
from time import strftime, sleep

i2c = board.I2C()
sensor = adafruit_tsl2591.TSL2591(i2c)
# Lowering gain on STL2591, LOW = LOWEST #
sensor.gain = adafruit_tsl2591.GAIN_LOW  # 60mm MIN lamp separation required #

# Gain adjustment --> direct adjustment #
# tsl.setGain(TSL2561_GAIN_1X);      /* 1x gain --> high light mode */
# tsl.setGain(TSL2561_GAIN_16X);     /* 16x gain --> low light mode */
# tsl.enableAutoGain(true);          /* Auto switching 1x or 16x */

# Resolution adjustment --> change integration time *WARNING* May adversely affect program performance #
# tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fastest & lowest res */
# tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_101MS);  /* balanced performance - DEFAULT */
# tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_402MS);  /* slowest & highest res --> 16-bit data! */

