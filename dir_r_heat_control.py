# first half of code is logging relevant sensor data
# second half is temp control measures

from time import time, sleep, strftime
import csv
import os

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

# open loop for continuous logging
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

    sleep(1)

# if temp at bottom of reactor higher than top then increase lower/upper fan RPM
