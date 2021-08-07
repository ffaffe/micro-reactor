# controls automation of heating system
from time import sleep, strftime, time
import RPi.GPIO as GPIO
import math
import csv

GPIO.setmode(GPIO.BCM)   # convert pin numbers --> board numbers
relay1_GPIO = 17  # pin being used for this relay
GPIO.setup(relay1_GPIO, GPIO.OUT)     # GPIO assign mode

temp1 =                 # temp we're aiming for #


# 'current' temp reading is delayed value due to reading from csv not direct from sensor
# direct from sensor impacts stability of temp_mon program and increases delay between readings
# it's a cheat but it's accurate enough for the purpose here
csv.reader(test.csv)    # temperature log file

GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)    # ON
sleep(10)                                # time delay before switching
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)     # OFF

