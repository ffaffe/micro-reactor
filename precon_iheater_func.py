from SlidingKoala2 import e_rb1, e_ri
from time import sleep
import RPi.GPIO as GPIO
import os

# defining sensor connections
upper_ri = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"
lower_ri = "/sys/bus/w1/devices/28-00000bc54f93/w1_slave"
r_bot1 = "/sys/bus/w1/devices/28-000008db57e2/w1_slave"

# defining relay connections and slaves
# check the bollocks out of all the pin numbers and assigns below

GPIO.setmode(GPIO.BCM)  # convert pin numbers --> board numbers

relay1_GPIO = 17  # circuit = heater
GPIO.setup(relay1_GPIO, GPIO.OUT)  # GPIO assign mode

relay2_GPIO = 18  # circuit = l_fans full
GPIO.setup(relay2_GPIO, GPIO.OUT)  # GPIO assign mode

relay3_GPIO = 19  # circuit = l_fans half
GPIO.setup(relay3_GPIO, GPIO.OUT)  # GPIO assign mode

relay4_GPIO = 20  # circuit = u_fans full
GPIO.setup(relay4_GPIO, GPIO.OUT)  # GPIO assign mode

relay5_GPIO = 21  # circuit = u_fans half
GPIO.setup(relay5_GPIO, GPIO.OUT)  # GPIO assign mode

relay6_GPIO = 22  # circuit = reagent bottle heater
GPIO.setup(relay6_GPIO, GPIO.OUT)  # GPIO assign mode

# sensor read and heating loop
while True:
    # upper internal temp sensor #
    f = open(upper_ri, "r")
    data = f.read()
    f.close()
    (discard, sep, reading) = data.partition(' t=')
    up_ri_t = float(reading) / 1000.0

    # lower internal temp sensor #
    f = open(lower_ri, "r")
    data = f.read()
    f.close()
    (discard, sep, reading) = data.partition(' t=')
    low_ri_t = float(reading) / 1000.0

    agr_temp = up_ri_t + low_ri_t
    av_ri_temp = int(agr_temp / 2)

    if av_ri_temp >= e_ri-50:  # burst heating mode
        GPIO.output(relay1_GPIO, GPIO.HIGH)  # heater ON
        sleep(10)  # delay to allow element to warm before airflow in
        GPIO.output(relay3_GPIO, GPIO.HIGH)  # l fans half speed
        sleep(30)
        if av_ri_temp >= e_ri-50:  # rapid & sustained heating mode
            GPIO.output(relay1_GPIO, GPIO.HIGH)  # heater ON
            GPIO.output(relay3_GPIO, GPIO.LOW)  # l fans half speed OFF
            sleep(1)  # delay to avoid two relay ON circuits to one set of fans
            GPIO.output(relay2_GPIO, GPIO.HIGH)  # l fans full speed
            sleep(10)

    elif av_ri_temp >= e_ri-15:
        GPIO.output(relay1_GPIO, GPIO.HIGH)  # heater ON
        GPIO.output(relay2_GPIO, GPIO.LOW)  # l fans full OFF
        GPIO.output(relay3_GPIO, GPIO.HIGH)  # l fans half
        sleep(10)

        # poss needs another elif. set to e_ri?? maybe....
    else:
        GPIO.output(relay1_GPIO, GPIO.LOW)  # heater OFF
        sleep(5)  # delay to draw a little extra heat from lamp before OFF
        GPIO.output(relay2_GPIO, GPIO.LOW)  # l fans full OFF
        GPIO.output(relay3_GPIO, GPIO.LOW)  # l fans half OFF

    # attempting to even temp gradients/heat sitting at base
    # will almost certainly cause the program to get stuck AF (tech term)
    while True:
        for x in range(10):   # bodge job to try and force this s*** program to not get stuck. which 4 letter word am I?
            if low_ri_t > up_ri_t:
                GPIO.output(relay5_GPIO, GPIO.HIGH)  # u fans half ON
                sleep(30)           # change me to adjust the time for initial try at equalising
                if low_ri_t > up_ri_t:
                    GPIO.output(relay5_GPIO, GPIO.LOW)  # u fans half OFF
                    GPIO.output(relay4_GPIO, GPIO.HIGH)  # u fans full ON
                    sleep(5)
    sleep(0.5)
    print('mission accomplished')












# ts_1 = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"
# ts_2 = "/sys/bus/w1/devices/28-00000bc54f93/w1_slave"
# ts_3 = "/sys/bus/w1/devices/28-0319160dfae2/w1_slave"
# ts_4 = "/sys/bus/w1/devices/28-000008db57e2/w1_slave"
# ts_5 = "/sys/bus/w1/devices/28-00000bc6dbf5/w1_slave"
# ts_6 = "/sys/bus/w1/devices/28-0319161bebb6/w1_slave"
