from matplotlib import pyplot as plt
import csv
import numpy as np
import pandas as pd
from time import time, strftime
from datetime import datetime


df = pd.read_csv("2.csv", skipinitialspace=True,
                 delimiter=',', header=2)


x = df['Time:']
y1 = df['Sensor 1:']
y2 = df['Sensor 2:']
y = df['Average:']

plt.plot(x, y1, label='S1', color="navy")
plt.plot(x, y2, label='S2', color="yellow")
plt.plot(x, y, label='Average', color="purple")
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Exciting Graph!')
plt.legend()
plt.show()
print(df)




#with open('150932.csv', 'r') as csvfile:
#    plots = csv.reader(csvfile, delimiter=',')
#    data = np.genfromtxt("150932.csv", delimiter=",", names=["Time:", "Sensor 1:", "Sensor 2:", "Average:"])
#    for row in plots:
#        x.append(int(row[0]))
#        y.append(int(row[1]))




# data = np.genfromtxt("150932.csv", delimiter=",", names=["x", "y"])
# plt.plot(data['x'], data['y'])

# df = df.astype(int)
# convert column "a" to int64 dtype and "b" to complex type
#
# `df = df.astype({"a": int, "b": complex})`
# convert Series to float16 type
#
# s = s.astype(np.float16)
# convert Series to Python strings
#
# s = s.astype(str)
# convert Series to categorical type - see docs for more details
#
# s = s.astype('category')