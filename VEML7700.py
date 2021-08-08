import time
import board
import adafruit_veml7700
from time import sleep, strftime

i2c = board.I2C()  # uses board.SCL and board.SDA #
veml7700 = adafruit_veml7700.VEML7700(i2c)


while True:
    ####clear NEED#####
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)
    sleep(1)
