import board
import busio
import adafruit_veml6070
import adafruit_veml7700
import adafruit_tsl2591
import time
from time import strftime, sleep

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


# Safety message/warning #
print('''*******************************************************************
WARNING - Please take care when working with intense light sources!
******************************************************************* \n''')
sleep(3)

print('''Data acquisition commencing - {} 
*************************************************'''.format(date))
sleep(1.5)

while True:  # Loops the program indefinitely #
    uv_raw = V6070.uv_raw
    risk_level = V6070.get_index(uv_raw)
    light7700 = V7700.light
    lux7700 = V7700.lux
    lux = t2591.lux
    visible = t2591.visible
    infrared = t2591.infrared
    full_spectrum = t2591.full_spectrum

    # Acquisition of UV RAW data + conversion to UV index #
    # uv_raw = V6070.uv_raw
    # risk_level = V6070.get_index(uv_raw)

    print(strftime('%H:%M:%S (%d/%m)\n'))
    print("6070 --> UV intensity (UV index) = {0} mW/cm\u00B2 ({1})\n".format(uv_raw, risk_level))
    print("7700 --> Light intensity (arbitrary brightness) = {0} lux ({1})\n".format(lux7700, light7700))
    print('TSL2591:')
    print('Total Light = {0} lux'.format(lux))
    print('Infrared Light = {0} lux'.format(infrared))
    print('Visible light = {0} lux'.format(visible))
    print('Full spectrum (IR+visible) light = {0} lux'.format(full_spectrum))
    print('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    sleep(2)
