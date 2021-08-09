# temperature logger for only the sensors inside the reactor body
# used to control fans/heater

from time import strftime, time, sleep
import csv
import os


# comment out def main(): AND remove indent to convert back to individually executable python script
# in use in GUI app
# comment out devices not in use inside rector AND adjust ts_* refs as needed
def main1():
    print("logging started")

    ts_1 = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"
    ts_2 = "/sys/bus/w1/devices/28-00000bc54f93/w1_slave"

    # define csv filenames & directories #
    folder1 = "Temperature_logs"
    folder2 = "Reactor_internal"
    folder_date = strftime("%d%m%y")
    folder3 = folder_date
    file_date = strftime("%H%M%S")
    filename1 = file_date
    cwd = os.getcwd()

    # check for existing directory to avoid overwrites/errors
    save_dir4 = os.path.join(cwd, folder1, folder2, folder3, filename1)
    save_dir5 = os.path.join(cwd, folder1, folder2, folder3)
    if not os.path.exists(save_dir5):
        os.makedirs(save_dir5)

    # writing header row of csv
    f = open(save_dir4 + ".csv", "a", newline="")
    c = csv.writer(f)
    c.writerow([strftime('%d-%m-%Y, %H:%M:%S')])
    c.writerow(["Time:", "Sensor 1:", "Sensor 2:", "Average:"])
    f.close()

    while True:
        # r += 1 # count up component of range argument above #
        date_time = strftime("%H:%M:%S")
        print("\n ************************** \n")
        print(date_time)

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

        f = open(save_dir4 + ".csv", "a", newline="")
        c = csv.writer(f)
        c.writerow([date_time, t1, t2, av_temp])
        f.close()

        sleep(1.0)

    # 28-000008db19eb  28-00000bc54f93  28-0319160dfae2  w1_bus_master1
    # 28-000008db57e2  28-00000bc6dbf5  28-0319161bebb6
