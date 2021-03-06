from time import strftime, time, sleep
import csv
import os


# comment out def main(): AND remove indent to convert back to individually executable python script
# in use in GUI app #
def main():
    print("logging started")

    ts_1 = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"
    ts_2 = "/sys/bus/w1/devices/28-00000bc54f93/w1_slave"
    ts_3 = "/sys/bus/w1/devices/28-0319160dfae2/w1_slave"
    ts_4 = "/sys/bus/w1/devices/28-000008db57e2/w1_slave"
    ts_5 = "/sys/bus/w1/devices/28-00000bc6dbf5/w1_slave"
    ts_6 = "/sys/bus/w1/devices/28-0319161bebb6/w1_slave"

    ts_7 = "/sys/bus/w1/devices/28-00000bc6e47d/w1_slave"       # psu exhaust

    # uncomment below to add sample range --> number of temp values to be measured #
    # range = 0

    # define csv filenames & directories #
    folder1 = "Temperature_logs"
    folder2 = "Full_system"
    folder_date = strftime("%d%m%y")
    folder3 = folder_date
    file_date = strftime("%H%M%S")
    filename1 = file_date
    cwd = os.getcwd()

    # check for existing directory to avoid overwrites/errors
    save_dir2 = os.path.join(cwd, folder1, folder2, folder3, filename1)
    save_dir3 = os.path.join(cwd, folder1, folder2, folder3)
    if not os.path.exists(save_dir3):
        os.makedirs(save_dir3)

    # writing header row of csv
    f = open(save_dir2 + ".csv", "a", newline="")
    c = csv.writer(f)
    c.writerow([strftime('%d-%m-%Y, %H:%M:%S')])
    c.writerow(["Time:", "Sensor 1:", "Sensor 2:", "Sensor 3:", "Sensor 4:", "Sensor 5:", "Sensor 6:", "Sensor 7:"])

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

        # S3 #
        f = open(ts_3, "r")
        data = f.read()
        f.close()
        (discard, sep, reading) = data.partition(' t=')
        t3 = float(reading) / 1000.0

        # S4 #
        f = open(ts_4, "r")
        data = f.read()
        f.close()
        (discard, sep, reading) = data.partition(' t=')
        t4 = float(reading) / 1000.0

        # S5 #
        f = open(ts_5, "r")
        data = f.read()
        f.close()
        (discard, sep, reading) = data.partition(' t=')
        t5 = float(reading) / 1000.0

        # S6 #
        f = open(ts_6, "r")
        data = f.read()
        f.close()
        (discard, sep, reading) = data.partition(' t=')
        t6 = float(reading) / 1000.0

        # S7 #
        f = open(ts_7, "r")
        data = f.read()
        f.close()
        (discard, sep, reading) = data.partition(' t=')
        t7 = float(reading) / 1000.0

        f = open(save_dir2 + ".csv", "a", newline="")
        c = csv.writer(f)
        c.writerow([date_time, t1, t2, t3, t4, t5, t6, t7])
        f.close()

        sleep(1.0)

    # 28-000008db19eb  28-00000bc54f93  28-0319160dfae2  w1_bus_master1
    # 28-000008db57e2  28-00000bc6dbf5  28-0319161bebb6  28-00000bc6e47d




