import time
import csv


# comment out def main(): AND remove indent to convert back to individually executable python script
# in use in GUI app #
def main():
    print(time.strftime("%a, %d %b %y"))

    f = open("test.csv", "a", newline="")
    c = csv.writer(f)
    c.writerow([time.strftime('%d-%m-%Y, %H:%M:%S')])
    c.writerow(["Time:", "Sensor 1:", "Sensor 2:", "Sensor 3:", "Sensor 4:", "Sensor 5:", "Sensor 6:"])

    ts_1 = "/sys/bus/w1/devices/28-000008db19eb/w1_slave"
    ts_2 = "/sys/bus/w1/devices/28-00000bc54f93/w1_slave"
    ts_3 = "/sys/bus/w1/devices/28-0319160dfae2/w1_slave"
    ts_4 = "/sys/bus/w1/devices/28-000008db57e2/w1_slave"
    ts_5 = "/sys/bus/w1/devices/28-00000bc6dbf5/w1_slave"
    ts_6 = "/sys/bus/w1/devices/28-0319161bebb6/w1_slave"

    # uncomment below to add sample range --> number of temp values to be measured #
    # range = 0

    while True:
        # r += 1 # count up component of range argument above #
        date_time = time.strftime("%H:%M:%S")
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

        print("{} {:.3f}".format("Sensor 1 =", t1))
        print("{} {:.3f}".format("Sensor 2 =", t2))
        print("{} {:.3f}".format("Sensor 3 =", t3))
        print("{} {:.3f}".format("Sensor 4 =", t4))
        print("{} {:.3f}".format("Sensor 5 =", t5))
        print("{} {:.3f}".format("Sensor 6 =", t6))

        f = open("test.csv", "a", newline="")
        c = csv.writer(f)

        c.writerow([date_time, t1, t2, t3, t4, t5, t6])

        time.sleep(1.0)

    # 28-000008db19eb  28-00000bc54f93  28-0319160dfae2  w1_bus_master1
    # 28-000008db57e2  28-00000bc6dbf5  28-0319161bebb6
