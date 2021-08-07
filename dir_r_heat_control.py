from time import time, sleep, strftime
import csv
import os

# comment out
print(strftime("%a, %d %b %y"))

# define csv filenames & directory #
folder1 = "Temperature logs"
folder2 = "Reactor internal"
folder_date = strftime("%d%m%y")
folder3 = folder_date
file_date = strftime("%H%M%S")
filename1 = file_date
cwd = os.getcwd()
save_dir = os.path.join(cwd,folder1, folder2, folder3, filename1)
f = open(save_dir + ".csv", "a", newline="")
c = csv.writer(f)
c.writerow([strftime('%d-%m-%Y, %H:%M:%S')])
c.writerow(["Time:", "Sensor 1:", "Sensor 2:", "Average:"])

ts_1 = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"
ts_2 = "/sys/bus/w1/devices/28-00000bc54f93/w1_slave"

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

    f = open(filename1 + ".csv", "a", newline="")
    c = csv.writer(f)
    date_time = strftime("%H.%M.%S")
    c.writerow([date_time, t1, t2, av_temp])

    sleep(1)

# if temp at bottom of reactor higher than top then increase lower/upper fan RPM
