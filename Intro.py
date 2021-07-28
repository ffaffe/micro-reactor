from time import strftime, sleep
import datetime

currentTime = datetime.datetime.now()
currentTime.hour

if currentTime.hour < 12:
    print('Good morning!')
elif 12 <= currentTime.hour <= 18:
    print('Good afternoon!')
elif 18 <= currentTime.hour <= 20:
    print('Good evening')
else:
    print('\nGood evening...')
    sleep(1.5)
    print("Someone\'s burning the midnight oil...")
    sleep(1.5)
    print('Please look after yourself...')
    sleep(1.5)
    print('We ALL need a rest...')
    sleep(2)

print('')
print(strftime("%a, %d %b %Y %H:%M:%S \n"))
print('Sensor test results:')
print('''Sensor data acquisition commencing...
CSV created, see XXXXXX @ LOCATION''')

# Would you like to view a live data plot? #
