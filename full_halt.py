import os
import time
import RPi.GPIO as GPIO

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
relay7_GPIO = 23                                 # circuit =
GPIO.setup(relay7_GPIO, GPIO.OUT)                # GPIO assign mode
relay8_GPIO = 24                                 # circuit =
GPIO.setup(relay8_GPIO, GPIO.OUT)                # GPIO assign mode

# Kill all relay circuits, leave logging programs...
