import time
import board
import adafruit_veml7700
from time import sleep, strftime

i2c = board.I2C()  # uses board.SCL and board.SDA #
veml7700 = adafruit_veml7700.VEML7700(i2c)

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
if not os.path.exists(save_dir1):
    os.makedirs(save_dir1)

# writing header row of csv
f = open(save_dir + ".csv", "a", newline="")
c = csv.writer(f)
c.writerow([strftime('%d-%m-%Y, %H:%M:%S')])
c.writerow(["Time:", "Sensor 1:", "Sensor 2:", "Average:"])
f.close()

while True:
    ####clear NEED#####
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)
    sleep(1)
