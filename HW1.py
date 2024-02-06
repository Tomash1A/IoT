from datetime import datetime
import time
import numpy as np
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as FA


plt.style.use('fivethirtyeight')
temp_acc =[]  
humid_acc = []
timecounter = []
idx = count()

def generate_values(idx):
    now = datetime.now()
    temp = np.random.normal(20,1)
    humid = np.random.normal(30,1)
    timecounter.append(idx)
    temp_acc.append(temp)
    humid_acc.append(humid)
    print(idx,' ',now," ",temp, " ", humid)
    plt.cla()
    plt.scatter(timecounter,temp_acc, linestyle=':', marker='o', color='red') 
    plt.scatter(timecounter,humid_acc, linestyle=':', marker='o', color='blue') 
    plt.title('Temperature and humidity sampled in 1s intervals')
    plt.xlabel('Samples')
    plt.legend(['temperature','humidity'], loc = "upper right")

anim = FA(plt.gcf(), generate_values, interval= 1000, cache_frame_data=False)
plt.show()