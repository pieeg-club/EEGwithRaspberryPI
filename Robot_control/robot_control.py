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
from RPi import GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

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
    if (fill_array==1):
        data_for_filter=data_for_shift_filter[ch]+data
        #data_high = butter_highpass_filter(data, cutoff, fps)
        #data_low =  butter_lowpass_filter (data_high,cutoffs, fps)
        data_band = butter_bandpass_filter(data_for_filter, cutoff, cutoffs,fps)
        data_after_filter=data_band[1000:2000]
        data_for_shift_filter[ch]=data
        return data_after_filter
    else:
        data_for_shift_filter[ch]=data
        fill_array=fill_array+1
        data_emtpy_only_one_time=list(range(0,1000,1))
        return data_emtpy_only_one_time
    
sample_len = 1000
fps = 250
cutoff=1
cutoffs = 40

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

samplingFrequency   =  250 
beginTime           = 0;

figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')

axis[0].set_title('Data after pass filter')
axis[1].set_title('Fourier transform depicting the frequency components')

blinking_value = 5

while 1: 
    if (data_was_received_test == data_was_received):
        data_was_received_test = not data_was_received_test
        axis[1].cla()
        axis[0].cla()

        filtered_high_pass=graph(0)

        endTime             = int(len(filtered_high_pass)/250); 
        time  = np.arange(0, (len(filtered_high_pass)/250),1/250);
        axis[0].plot(time, filtered_high_pass)

        fourierTransform = np.fft.fft(filtered_high_pass)/len(filtered_high_pass)           
        fourierTransform = fourierTransform[range(int(len(filtered_high_pass)/2))] 
        tpCount     = len(filtered_high_pass)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/samplingFrequency
        frequencies = values/timePeriod
        axis[1].plot(frequencies, abs(fourierTransform))
        plt.pause(0.000001)

        if (blinking_value>max(abs(fourierTransform[100:250]))):
            GPIO.output(31, True)
            GPIO.output(35, False)
        else:
            GPIO.output(31, False)
            GPIO.output(35, True)            

    
plt.show()









        
