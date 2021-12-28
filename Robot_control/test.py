import scipy.fftpack
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
libc = ctypes.CDLL("./super_real_time_massive.so")  # libr for read from c file   https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/GUI/real_time_massive.h
libc.prepare()

def receive_data():
    libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))  # read from c file  
    data=libc.real()
    return data

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

def graph ():
    global fill_array
    print (data_array)
    data = (data_array[:,[0]]) # take only 1 channel 
    print (data)
    data = list(data.flatten())
    if (fill_array==1):
        data_for_filter=data_for_shift_filter[0]+data # the most important point - here I add up the data, current and for the last step

        data_for_shift_filter[0]=data # here I write data for a step back in the next loop
        print (type (data))
        print (type (data_for_shift_filter[0]))
        return data_for_filter
    
    else:  # This is necessary since I transfer data to the filter - "current" and "for the last session", but the first time I read the data "for the last session" there is no data. Used it, only 1 time
        data_for_shift_filter[0]=data
        fill_array=fill_array+1
        data_emtpy_only_one_time=list(range(0,2000,1))
        return data_emtpy_only_one_time



sample_len = 1000  # это в си файле читаю в течение 4 секунд
fps = 250
cutoff=1
cutoffs = 40
fill_array=0

def read_data_thread(): # Thread- since this code for not powerful RaspberryPI. Needs to pass the data through filters and display it on graphs
    global data_was_received
    data_was_received = False
    while 1:       
        global data_array
        data_array=receive_data()
        data_was_received = not data_was_received
        print (data_was_received)


thread = threading.Thread(target=read_data_thread)
thread.start()



data_for_shift_filter=([[1]]) #only one channel is for example because

data_was_received_test=True  #


samplingFrequency   =  200 
beginTime           = 0;

figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)

axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
axis[0].set_title('Data after pass filter')

axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')
axis[1].set_title('Data after pass filter shift')

axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')
axis[2].set_title('Row_data')

while 1: 
    if (data_was_received_test == data_was_received):
        print (data_was_received_test) # I check that NEW!!! data was received from C file
        data_was_received_test = not data_was_received_test
        
        axis[0].cla() # this data for 2 sessions with filter
        axis[1].cla() # this data in one session without filter
        axis[2].cla() # this data with shift, filter work only for current session
        
        filtered_high_pass_row=graph()
        filtered_high_pass = butter_bandpass_filter(filtered_high_pass_row, cutoff, cutoffs,fps)
               
        filtered_high_pass_Short=(len(filtered_high_pass))/2
        filtered_high_pass_long=len(filtered_high_pass)
        
        axis[0].plot(time, filtered_high_pass)
        print (len(time))
        print (len(filtered_high_pass))
        axis[1].plot(time[1000:2000], filtered_high_pass[1000:2000])
        
        axis[2].plot(time, filtered_high_pass_row)
        plt.pause(0.000001) 
plt.show()









        
