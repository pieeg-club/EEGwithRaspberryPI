import ctypes
import time
import numpy as np
from numpy.ctypeslib import ndpointer
import sys
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)
libc = ctypes.CDLL("./super_real_time_massive.so")
libc.prepare()
print("ok")

def receive_data():
 libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(200,8))    
 data=libc.real()
 data= (data[:,[0]])
 data=list(data.flatten())
 return data

def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def butter_lowpass(cutoffs, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoffs, fs, order=5):
    b, a = butter_lowpass(cutoffs, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y



b_low_filter, a_low_filter = signal.butter(5, 0.2)


fps = 200
sine_fq = 3 #Hz
duration = 10 #seconds
cutoff=2
cutoffs = 30
#figure, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
figure, (ax1) = plt.subplots(1, 1, sharex=True)
axis_x=0

plt.title('name')
plt.xlabel('x')
plt.ylabel('y')
 
while 1:
 data=receive_data()
 data_high = butter_highpass_filter(data, cutoff, fps)
 data_low =  butter_lowpass_filter (data_high,cutoffs, fps)
 data=data_low


 
 ax1.plot(range(axis_x,axis_x+200,1),data,color = '#0a0b0c')  
 ax1.axis([axis_x-100, axis_x+50, data[50]-5000, data[50]+5000])
 axis_x=axis_x+200
 plt.pause(0.000001)
 plt.draw()



