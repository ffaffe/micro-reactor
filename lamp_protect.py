# basic script designed to protect the most expensive component
# will almost certainly make every other program kick off
from time import time, sleep, strftime
import csv
import os
import RPi.GPIO as GPIO
from dir_r_heat_control_v2 import t1    # may need to be t2...

# defining connection to sensor installed in lamp heat sink
ts_1 = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"

# setting up relay control of heater and fans
GPIO.setmode(GPIO.BCM)                           # convert pin numbers --> board numbers

relay1_GPIO = 17                                 # circuit = heater
GPIO.setup(relay1_GPIO, GPIO.OUT)                # GPIO assign mode

relay2_GPIO = 18                                 # circuit = l_fans full
GPIO.setup(relay2_GPIO, GPIO.OUT)                # GPIO assign mode

relay3_GPIO = 19                                 # circuit = l_fans half
GPIO.setup(relay3_GPIO, GPIO.OUT)                # GPIO assign mode

relay4_GPIO = 20                                 # circuit = u_fans full
GPIO.setup(relay4_GPIO, GPIO.OUT)                # GPIO assign mode

relay5_GPIO = 21                                 # circuit = u_fans half
GPIO.setup(relay5_GPIO, GPIO.OUT)                # GPIO assign mode

relay6_GPIO = 22                                 # circuit = lamp
GPIO.setup(relay6_GPIO, GPIO.OUT)                # GPIO assign mode

while True:
    if 75 <= t1 < 90:
        print("********************************")
        sleep(0.2)
        print("WARNING - Lamp OVERHEAT likely")
        sleep(2)
        print("********************************")
        sleep(0.2)
        print("powering upper fans to 1/2 speed")
        sleep(2)
        print("********************************")

        GPIO.output(relay4_GPIO, GPIO.LOW)  # u fans full OFF
        sleep(0.1)
        GPIO.output(relay5_GPIO, GPIO.HIGH)  # u fans half ON

    elif 90 <= t1 < 100:
        print("********************************")
        sleep(0.2)
        print("WARNING - Lamp OVERHEAT imminent")
        sleep(1)
        print("********************************")
        sleep(0.2)
        print("powering upper fans to full speed")
        sleep(1)
        print("********************************")

        GPIO.output(relay5_GPIO, GPIO.LOW)  # u fans half OFF
        sleep(0.1)
        GPIO.output(relay5_GPIO, GPIO.HIGH)  # u fans half ON

    elif t1 >100:
        print("********************************")
        sleep(0.2)
        print("WARNING --- WARNING --- WARNING")
        sleep(1)
        print("********************************")
        sleep(0.2)
        print("Lamp OVERHEAT detected!")
        sleep(0.2)
        print("Emergency shutdown initiated...")

        GPIO.output(relay5_GPIO, GPIO.LOW)  # u fans half OFF
        sleep(0.1)
        GPIO.output(relay5_GPIO, GPIO.HIGH)  # u fans half ON
        GPIO.setup(relay6_GPIO, GPIO.LOW)    # Lamp OFF
