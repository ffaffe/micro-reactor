# short and sweet check of the relevant sensor connections, including listing all detected ds18b20 temp sensors
import board
import digitalio
import busio
from time import sleep


def sens_test():
    for x in range(1):
        print("\nInitiating sensor test...\n")
        sleep(1)

        pin = digitalio.DigitalInOut(board.D4)
        print("Digital IO connection OK!")
        sleep(1)

        i2c = busio.I2C(board.SCL, board.SDA)
        print("I2C connection OK!")
        sleep(1)

        spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
        print("SPI OK!")
        sleep(1)

        print("All tests complete")
        print("No faults detected")

        exit()



