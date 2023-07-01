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

data_lenght_for_Filter = 4     # how much we read data for filter, all lenght  [_____] + [_____] + [_____]
read_data_lenght_one_time = 1   # for one time how much read  [_____]

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
y_minus_graph=100
y_plus_graph=100
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
dataset_massiv = np.array([],[])
ch = 0 
while 1:
        #data = (data_array[:,[ch]])
        #data = list(data.flatten())
        
        if just_one_time == 0:
            for b in range (0,data_lenght_for_Filter,1):
                for a in range (0,read_data_lenght_one_time,1):
                    libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))
                    print ("ok1")  
                    data_read = libc.real() #[x + 3 for x in data_read]
                    
                    print ("ok2", len(data_read))  
                    data_read = (data_read[:,[ch]])
                    print ("ok3")  
                    data_before.append(data_read)                
                    print ("ok4") 
            just_one_time = 1
            print ("ok5") 
            data_before = data_before[read_data_lenght_one_time:]
            print ("ok6")    
        for c in range (0,read_data_lenght_one_time,1):
            libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))
            print ("ok7")
            data_read = libc.real() #[x + 3 for x in data_read]
            data_read = (data_read[:,[ch]])
            data_after.append(data_read)
            
        data_before_for_sum = data_before
        data_after_for_sum = data_after
                                
        data_before_for_sum = [item for sublist in data_before for item in sublist]
        data_after_for_sum = [item for sublist in data_after for item in sublist]
        dataset =  data_before_for_sum + data_after_for_sum #+ data_after_flip
        dataset = [x[0] for x in dataset]

        dataset = butter_bandpass_filter(dataset, cutoff, cutoffs,fps)   
        axis[0].plot(range(axis_x,axis_x+sample_len,1),dataset[-250:],color = '#0a0b0c')
        print ("ildar2")    
        axis[0].axis([axis_x-x_minux_graph, axis_x+x_plus_graph, dataset[len(dataset)-1]-y_minus_graph, dataset[len(dataset)-1]+y_plus_graph])
        print ("ildar3")
        axis_x=axis_x+sample_len      
        plt.pause(0.000001)
        
        print ("ok1", len(dataset))
        if len(dataset)==10000:
            dataset = pd.DataFrame(dataset)
            dataset.to_excel("./dataset.xlsx")
            sys.exit()







