import board
import busio`
import adafruit_veml6070
import adafruit_veml7700
import adafruit_tsl2591
from time import strftime, sleep, time
import os
import csv

# uses board.SCL and board.SDA #
i2c = board.I2C()

# Defining the connection to VEML7700 #
V7700 = adafruit_veml7700.VEML7700(i2c)
# Defining the connection to VEML6070 #
V6070 = adafruit_veml6070.VEML6070(i2c)  # Naming the module #
# Defining the connection to TSL2591 #
t2591 = adafruit_tsl2591.TSL2591(i2c)

# Lowering gain on STL2591, LOW = LOWEST #
t2591.gain = adafruit_tsl2591.GAIN_LOW  # 60mm MIN lamp separation required #

# Naming date/time functions
date = strftime('%d/%m/%Y - %H:%M')
date_time = strftime("%H:%M:%S")

# naming and resetting sensor functions
uv_raw = V6070.uv_raw
risk_level = V6070.get_index(uv_raw)
light7700 = V7700.light
lux7700 = V7700.lux
lux = t2591.lux
visible = t2591.visible
infrared = t2591.infrared
full_spectrum = t2591.full_spectrum
luminosity = t2591.raw_luminosity

# define csv filenames & directories #
folder1 = "Light_logs"
folder2 = "All_sensors"
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
c.writerow(["Time:", "v6070 intensity (mW/cm\u00B2):", "uv index:", "v7700 arbitrary:", "v7700 intensity (lux):",
            "tsl2591 intensity (lux): ", "tsl2591 ir (arb.):", "tsl2591 visible (arb.):", "tsl2591 ir+vis (arb.):,"
                                                                                          "raw luminosity (arb.):"])

print("logging started")

while True:  # Loops the program indefinitely #
    uv_raw = V6070.uv_raw
    risk_level = V6070.get_index(uv_raw)
    light7700 = V7700.light
    lux7700 = V7700.lux
    lux = t2591.lux
    visible = t2591.visible
    infrared = t2591.infrared
    full_spectrum = t2591.full_spectrum
    luminosity = t2591.raw_luminosity

    f = open(save_dir2 + ".csv", "a", newline="")
    c = csv.writer(f)
    c.writerow([date_time, uv_raw, risk_level, light7700, lux7700, lux, visible, infrared, full_spectrum, luminosity])
    f.close()

    sleep(1)
