import csv
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x, y = np.loadtext('test.csv', unpack = True, delimiter = ',')

plt.plot(x,y)

plt.title('Test')
plt.ylabel('Time')
plt.xlabel('Temperature (oC)')

plt.show()