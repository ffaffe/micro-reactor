# first half of code is logging relevant sensor data
# second half is temp control measures

from time import time, sleep, strftime
import csv
import os
import RPi.GPIO as GPIO

# comment out
print(strftime("%a, %d %b %y"))

# define csv filenames & directories #
folder1 = "Temperature_logs"
folder2 = "Reactor_internal"
folder_date = strftime("%d%m%y")
folder3 = folder_date
file_date = strftime("%H%M%S")
filename1 = file_date
cwd = os.getcwd()

# check for existing directory to avoid overwrites/errors
save_dir = os.path.join(cwd, folder1, folder2, folder3, filename1)
save_dir1 = os.path.join(cwd, folder1, folder2, folder3)
if not os.path.exists(save_dir):
    os.makedirs(save_dir1)

# writing header row of csv
f = open(save_dir + ".csv", "a", newline="")
c = csv.writer(f)
c.writerow([strftime('%d-%m-%Y, %H:%M:%S')])
c.writerow(["Time:", "Sensor 1:", "Sensor 2:", "Average:"])

# defining names & addr of each sensor to be used for heater control --> if altered, take care with downstream links
ts_1 = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"
ts_2 = "/sys/bus/w1/devices/28-00000bc54f93/w1_slave"

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

# open loop for continuous logging\control
while True:
    # S1 #
    f = open(ts_1, "r")
    data = f.read()
    f.close()
    (discard, sep, reading) = data.partition(' t=')
    t1 = float(reading) / 1000.0

    # S2 #
    f = open(ts_2, "r")
    data = f.read()
    f.close()
    (discard, sep, reading) = data.partition(' t=')
    t2 = float(reading) / 1000.0

    agr_temp = t1 + t2
    av_temp = int(agr_temp / 2)

    # to be commented out --> debug only
    print(strftime("%H %M %S"))
    print(av_temp)

    # actual data to csv writing
    f = open(save_dir + ".csv", "a", newline="")
    c = csv.writer(f)
    date_time = strftime("%H.%M.%S")
    c.writerow([date_time, t1, t2, av_temp])

    if av_temp >= 50:                           # burst heating mode
        GPIO.output(relay1_GPIO, GPIO.HIGH)     # heater ON
        sleep(10)                               # delay to allow element to warm before airflow in
        GPIO.output(relay3_GPIO, GPIO.HIGH)     # l fans half speed
        sleep(30)
        if av_temp >= 50:                        # rapid & sustained heating mode
            GPIO.output(relay1_GPIO, GPIO.HIGH)  # heater ON
            GPIO.output(relay3_GPIO, GPIO.LOW)   # l fans half speed OFF
            sleep(1)                             # delay to avoid two relay ON circuits to one set of fans
            GPIO.output(relay2_GPIO, GPIO.HIGH)  # l fans full speed
            sleep(10)

            # hoping this captures the data that will get 'lost' while program 'stuck in this nested loop...
            f = open(save_dir + ".csv", "a", newline="")
            c = csv.writer(f)
            date_time = strftime("%H.%M.%S")
            c.writerow([date_time, t1, t2, av_temp])

    elif av_temp >= 55:
        GPIO.output(relay1_GPIO, GPIO.HIGH)  # heater ON
        GPIO.output(relay2_GPIO, GPIO.LOW)  # l fans full OFF
        GPIO.output(relay3_GPIO, GPIO.HIGH)  # l fans half
        sleep(10)
    else:
        GPIO.output(relay1_GPIO, GPIO.LOW)  # heater OFF
        sleep(5)  # delay to draw a little extra heat from lamp before OFF
        GPIO.output(relay2_GPIO, GPIO.LOW)  # l fans full OFF
        GPIO.output(relay3_GPIO, GPIO.LOW)  # l fans half OFF

    # attempting to even temp gradients/heat sitting at base
    while True:
        if t2 > t1:
            GPIO.output(relay5_GPIO, GPIO.HIGH)  # u fans half ON
            sleep(10)
            if t2 > t1:
                GPIO.output(relay5_GPIO, GPIO.LOW)  # u fans half OFF
                GPIO.output(relay4_GPIO, GPIO.HIGH)  # u fans full ON
                sleep(5)
    sleep(0.5)
