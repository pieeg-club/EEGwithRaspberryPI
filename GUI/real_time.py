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
print("library ok")


def receive_data():
    libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))    
    data=libc.real()
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

def butter_lowpass(cutoffs, fs, order=3):
    nyq = 0.5 * fs
  
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='lowpass', analog=False)
    #b, a = signal.butter(8, 0.5, btype='lowpass')
    return b, a

def butter_lowpass_filter(data, cutoffs, fs, order=5):
    b, a = butter_lowpass(cutoffs, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y


def graph (ch):
    data = (data_array[:,[ch]])
    data = list(data.flatten()) 
    data_high = butter_highpass_filter(data, cutoff, fps)
    data_low =  butter_lowpass_filter (data_high,cutoffs, fps)
    data=data_low 
    return data

sample_len = 1000
fps = 250
cutoff=2
cutoffs = 50
figure, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8) = plt.subplots(8, 1, sharex=True)
axis_x=0

#plt.title('Channel 1')
#plt.xlabel('sample')
#plt.ylabel('EEG Voltage')


y_minus_graph=1000
y_plus_graph=1000
x_minux_graph=5000
x_plus_graph=50
while 1:
 # 1 channel  
    data_array=receive_data()

    data=graph(0)
    ax1.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b0c')  
    ax1.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])

 # 2 channel  
    data=graph(1)
    ax2.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b1c')  
    ax2.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])
 
 # 3 channel
    data=graph(2)
    ax3.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0bba')  
    ax3.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])

 # 4 channel
    data=graph(3)
    ax4.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b9c')  
    ax4.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])

 # 5 channel
    data=graph(4)
    ax5.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b4c')  
    ax5.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])

 # 6 channel
    data=graph(5)
    ax6.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b2d')  
    ax6.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])

 # 7 channel
    data=graph(6)
    ax7.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0bcc')  
    ax7.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])

 # 8 channel
    data=graph(7)
    ax8.plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b0c')  
    ax8.axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])

    axis_x=axis_x+sample_len      
    plt.pause(0.000001)
    plt.draw()

