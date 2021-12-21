import ctypes
import time
import numpy as np
from numpy.ctypeslib import ndpointer
import sys
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import threading


np.set_printoptions(threshold=sys.maxsize)
libc = ctypes.CDLL("./super_real_time_massive.so")
libc.prepare()

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

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a
 	 
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    data = signal.lfilter(b, a, data)
    return data

def graph (ch):
    global fill_array
    data = (data_array[:,[ch]])
    data = list(data.flatten())
    data_for_shift=data
    if (fill_array==8):
        data=data_for_shift_filter[ch]+data
        #data_high = butter_highpass_filter(data, cutoff, fps)
        #data_low =  butter_lowpass_filter (data_high,cutoffs, fps)
        data_band = butter_bandpass_filter(data, cutoff, cutoffs,fps)
        data=data_band[1000:2000]
        data_for_shift_filter[ch]=data_for_shift
        return data
    else:
        data_for_shift_filter[ch]=data
        fill_array=fill_array+1
        data=list(range(0,1000,1))
        return data
    
sample_len = 1000
fps = 250
cutoff=2
cutoffs = 30
figure, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8) = plt.subplots(8, 1, sharex=True)
axis_x=0
y_minus_graph=100
y_plus_graph=100
x_minux_graph=5000
x_plus_graph=50

#plt.title('Channel 1')
#plt.xlabel('sample')
#plt.ylabel('EEG Voltage')

def read_data_thread():
    global data_was_received
    data_was_received = False
    while 1:       
        global data_array
        data_array=receive_data()
        data_was_received = not data_was_received

def start_thread_read_data():
    thread = threading.Thread(target=read_data_thread)
    thread.start()


start_thread_read_data()

data_for_shift_filter=([[1],[2],[3],[4],[5],[6],[7],[8]])
data_was_received_test=True
fill_array=0
axis_ch=[ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8]

while 1: 
    if (data_was_received_test == data_was_received):
        data_was_received_test = not data_was_received_test            
        for channel in (range(0,8,1)):
            data=graph(channel)
            axis_ch[channel].plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b0c')
            axis_ch[channel].axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])
        axis_x=axis_x+sample_len      
        plt.pause(0.000001)
        plt.draw()


