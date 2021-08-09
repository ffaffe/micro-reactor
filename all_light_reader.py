import board
import busio
import adafruit_veml6070
import adafruit_veml7700
import adafruit_tsl2591
import time
from time import sleep
from time import strftime, sleep

# uses board.SCL and board.SDA #
i2c = board.I2C()

# Defining the connection to VEML 7700 #
veml7700 = adafruit_veml7700.VEML7700(i2c)
# Defining the connection to VEML 6070 #
uv = adafruit_veml6070.VEML6070(i2c)  # Naming the module #
# Defining the connection to TSL2591 #
sensor = adafruit_tsl2591.TSL2591(i2c)

# Lowering gain on STL2591, LOW = LOWEST #
sensor.gain = adafruit_tsl2591.GAIN_LOW  # 60mm MIN lamp separation required #

# Naming date/time function#
date = time.strftime('%d/%m/%Y - %H:%M')

# Safety message/warning #
print('''*******************************************************************
WARNING - Please take care when working with intense light sources!
******************************************************************* \n''')
sleep(4)

print('''Data acquisition commencing - {} 
*************************************************'''.format(date))
sleep(1.5)

# below lines included to 'reset' sensors as no clear() function available. Without, first value = last reading taken by sensor #
uv_raw = uv.uv_raw
risk_level = uv.get_index(uv_raw)

## ADD RESETS FOR OTHER SENSORS! ##


while True:  # Loops the program indefinitely #
    # Aquisition of UV RAW data + conversion to UV index #
    uv_raw = uv.uv_raw
    risk_level = uv.get_index(uv_raw)

    print(time.strftime('%H:%M:%S (%d/%m)\n'))
    print('6070:')
    print("UV intensity (UV index) = {0} mW/cm\u00B2 ({1})\n".format(uv_raw, risk_level))
    print('7700:')
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)
    print('\nTSL2591:')
    lux = sensor.lux
    print('Total Light: {0} lux'.format(lux))
    infrared = sensor.infrared
    print('Infrared Light: {0}'.format(infrared))
    visible = sensor.visible
    print('Visible light: {0}'.format(visible))
    full_spectrum = sensor.full_spectrum
    print('Full spectrum (IR+visible) light: {0}'.format(full_spectrum))

    print('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    sleep(2)
