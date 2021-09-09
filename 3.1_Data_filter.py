import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import serial
import time
import random

random_data = np.arange(100)

def receive_data(fs, sinefreq, duration):
 for i in range(0,100,1):
  random_data[i] = int(random.uniform(0, 20))  
 result = pd.DataFrame({'data': random_data} )
# print (result)
 return result

def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y


# low_pass_filter
b_low_filter, a_low_filter = signal.butter(5, 0.2)


fps = 30
sine_fq = 3 #Hz
duration = 10 #seconds
cutoff=2

figure, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

axis_x=0
while 1:
 sine = receive_data(fps,sine_fq,duration)
 
 filtered_sine = butter_highpass_filter(sine.data, cutoff, fps)
 #filtered_sine=sine["data"]
 #low filter
 filtered_sine  = signal.filtfilt(b_low_filter, a_low_filter, filtered_sine)

 
 ax1.plot(range(axis_x, axis_x+100,1),sine,color = '#0a0b0c') 
 ax2.plot(range(axis_x, axis_x+100,1),filtered_sine, color = '#0a0b0c')


 axis_x1_move=sine["data"]
 ax1.axis([axis_x-400, axis_x+200, axis_x1_move[50]-20, axis_x1_move[50]+20])
 ax2.axis([axis_x-400, axis_x+200, filtered_sine[50]-15, filtered_sine[50]+15])

 
 axis_x=axis_x+100
# time.sleep (1)
 
 plt.pause(0.001)
 plt.draw()

#plt.show()

