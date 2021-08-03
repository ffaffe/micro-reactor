# Does exactly what it says on the tin... control and .csv output of the various reactor temperature systems #
import os
import glob
import time

# locates each device in sequence and holds data #
base_dir = '/sys/bus/w1/devices/'  # root directory of device #
# sensor 1 #
device_folder_ts1 = glob.glob(base_dir + '28-000008db19eb')[0]
device_file_ts1 = device_folder_ts1 + '/w1_slave'
# sensor 2 #
device_folder_ts2 = glob.glob(base_dir + '28-000008db57e2')[1]
device_file_ts2 = device_folder_ts2 + '/w1_slave'
# sensor 3 #
device_folder_ts3 = glob.glob(base_dir + '28-00000bc54f93')[2]
device_file_ts3 = device_folder_ts3 + '/w1_slave'
# sensor 4 #
device_folder_ts4 = glob.glob(base_dir + '28-00000bc6dbf5')[3]
device_file_ts4 = device_folder_ts4 + '/w1_slave'
# sensor 5 #
device_folder_ts5 = glob.glob(base_dir + '28-0319160dfae2')[4]
device_file_ts5 = device_folder_ts5 + '/w1_slave'
# sensor 6 #
device_folder_ts6 = glob.glob(base_dir + '28-0319161bebb6')[5]
device_file_ts6 = device_folder_ts6 + '/w1_slave'


# read temperature data #
def read_temp_raw_ts1():
    f = open(device_file_ts1, 'r')  # reads value #
    lines_ts1 = f.readlines()  # returns value #
    f.close()
    return lines_ts1


def read_temp_ts1():
    lines_ts1 = read_temp_raw_ts1()  # reads raw value #
    while lines_ts1[0].strip()[-3:] != 'YES':  # checks for good temp value --> YES #
        time.sleep(0.25)  # sleep delay before YES recheck on FAIL #
        lines_ts1 = read_temp_raw_ts1()
    temp_output = lines_ts1[1].find('t=')  # snip the data string to only temp value #
    if temp_output != -1:
        temp_string = lines_ts1[1].strip()[temp_output + 2:]
        temp_c_ts1 = float(temp_string) / 1000.0
        return temp_c_ts1


while True:
    print(read_temp_ts1())
    time.sleep(1)

# 28-000008db19eb  28-00000bc54f93  28-0319160dfae2  w1_bus_master1
# 28-000008db57e2  28-00000bc6dbf5  28-0319161bebb6
