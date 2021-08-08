import board
import adafruit_veml6070
import time
from time import sleep
from time import strftime

# Defining the connection #
i2c = board.I2C() # Connected via board.SCL and board.SDA #
uv = adafruit_veml6070.VEML6070(i2c) # Naming the module #
date = time.strftime('%d/%m/%Y - %H:%M') # Naming date/time function#


# Safety message/warning #
print('''*******************************************************************
WARNING - Please take care when working with intense light sources!
******************************************************************* \n''')
sleep(4)

print('''Data acquisition commencing - {} 
*************************************************'''.format(date))
sleep(1.5)

# below two lines included to 'reset' sensor as no clear() function available. Without, first value = last reading taken by sensor #
uv_raw = uv.uv_raw
risk_level = uv.get_index(uv_raw)

while True: # Loops the program indefinitely #
    # Aquisition of UV RAW data + conversion to UV index #
    uv_raw = uv.uv_raw
    risk_level = uv.get_index(uv_raw)

    print(time.strftime('%H:%M:%S (%d/%m)'))
    print("UV intensity (UV index) = {0} mW/cm\u00B2 ({1})\n".format(uv_raw, risk_level))
    sleep(1) # Sampling frequency in seconds #