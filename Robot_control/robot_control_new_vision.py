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
import scipy.fftpack
GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()
GPIO.setwarnings(False)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

np.set_printoptions(threshold=sys.maxsize)
libc = ctypes.CDLL("/home/pi/Desktop/EEGwithRaspberryPI-master/GUI/super_real_time_massive.so")
libc.prepare()

data_lenght_for_Filter = 10     # how much we read data for filter, all lenght  [_____] + [_____] + [_____]
read_data_lenght_one_time = 2   # for one time how much read  [_____]

lenght_data_for_filter = data_lenght_for_Filter*read_data_lenght_one_time-read_data_lenght_one_time
name_columns =  []
final_dataset = []

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


sample_len = 250
fps = 250
cutoff=1
cutoffs = 10
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

axis_x=0
y_minus_graph=500
y_plus_graph=500
x_minux_graph=5000
x_plus_graph=250

data_was_received_test=True
fill_array=0

axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
axis[0].set_title('Data after pass filter')
samplingFrequency   =  250 
blinking_value = 10

just_one_time = 0
data_before = []
data_after =  []
ch = 0 
while 1:
        #data = (data_array[:,[ch]])
        #data = list(data.flatten())
        
        if just_one_time == 0:
            for b in range (0,data_lenght_for_Filter,1):
                for a in range (0,read_data_lenght_one_time,1):
                    libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))  
                    data_read = libc.real() #[x + 3 for x in data_read]
                    data_read = (data_read[:,[ch]])
                    data_before.append(data_read)                

            just_one_time = 1
            data_before = data_before[read_data_lenght_one_time:]
                
        for c in range (0,read_data_lenght_one_time,1):
            libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))  
            data_read = libc.real() #[x + 3 for x in data_read]
            data_read = (data_read[:,[ch]])
            data_after.append(data_read)
            
        data_before_for_sum = data_before
        data_after_for_sum = data_after

        data_before_for_sum = [item for sublist in data_before for item in sublist]
        data_after_for_sum = [item for sublist in data_after for item in sublist]
        dataset =  data_before_for_sum + data_after_for_sum #+ data_after_flip
        dataset = [x[0] for x in dataset]
        print ("dataset", (dataset))

        dataset_before = data_before + data_after
        data_before = dataset_before[read_data_lenght_one_time:]
        #data_before = data_before[:read_data_lenght_one_time]
        data = butter_bandpass_filter(dataset, cutoff, cutoffs,fps)
        data_after = []
        dataset = []

        print ("ok1")
        axis[1].cla()
        axis[1].set_title('Fourier transform depicting the frequency components')
        axis[1].set_xlabel('Frequency')
        axis[1].set_ylabel('Amplitude')
        #for channel in (range(0,8,1)):
        channel=0

        #data=graph(channel,a)   
        print ("data", len(data))
        data_f = data[-250:]
        fourierTransform = np.fft.fft(data_f)/len(data_f)           
        fourierTransform = fourierTransform[range(int(len(data_f)/2))] 
        tpCount     = len(data_f)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/samplingFrequency
        frequencies = values/timePeriod

        axis[1].plot(frequencies, abs(fourierTransform))        
        axis[1].axis([0, 25, 0, 20])        
        axis[0].plot(range(axis_x,axis_x+sample_len,1),data[-250:],color = '#0a0b0c')  
        axis[0].axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[150]+y_plus_graph])
        axis_x=axis_x+sample_len      
        plt.pause(0.000001)
        
        GPIO.output(35,False )
        GPIO.output(31, False)
        print ('0:3', max(abs(fourierTransform[0:3])))
        print ('3:5', max(abs(fourierTransform[3:5])))
        if (blinking_value<max(abs(fourierTransform[0:3]))):
            GPIO.output(35, True)
            GPIO.output(31, False)

        if (blinking_value<max(abs(fourierTransform[3:5]))):
            GPIO.output(35, False)
            GPIO.output(31, True)

        plt.draw()
