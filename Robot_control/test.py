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
libc = ctypes.CDLL("./super_real_time_massive.so")
libc.prepare()

def receive_data():
    libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))    
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
    data = (data_array[:,[0]])
    print (data)
    data = list(data.flatten())
    if (fill_array==1):
        data_for_filter=data_for_shift_filter[0]+data # самый важнеый момент - тут скалдываю данные , текушие и за прошлый шаг

        data_for_shift_filter[0]=data # тут я пытаюсь запиать данные для шага назад в след цикле
        print (type (data))
        print (type (data_for_shift_filter[0]))
        return data_for_filter
    
    else:  # это надо так как я  передаю данные на фимльтр текушие и за прошлый сеанс, а в первый раз чтения данных за прошлый сеанс  данных нету, это один раз только обрабытвается 
        data_for_shift_filter[0]=data
        fill_array=fill_array+1
        data_emtpy_only_one_time=list(range(0,2000,1))
        return data_emtpy_only_one_time



sample_len = 1000  # это в си файле читаю в течение 4 секунд
fps = 250
cutoff=1
cutoffs = 40
fill_array=0

def read_data_thread(): # поток как этот код для разберри пи, а он медленный , ему время надо через фильтры данные провести и отобразить на графики
    global data_was_received
    data_was_received = False
    while 1:       
        global data_array
        data_array=receive_data()
        data_was_received = not data_was_received
        print (data_was_received)


thread = threading.Thread(target=read_data_thread)
thread.start()



data_for_shift_filter=([[1]]) # только один канал - это для примера так как

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
        print (data_was_received_test)
        data_was_received_test = not data_was_received_test
        
        axis[0].cla() # эти данные за 2 сеанса без фильтра
        axis[1].cla() # эти данные за один смейанс 
        axis[2].cla() # этро за 2 сеанса рп
        
        filtered_high_pass_row=graph()
        filtered_high_pass = butter_bandpass_filter(filtered_high_pass_row, cutoff, cutoffs,fps)
               
        endTime             = int(len(filtered_high_pass)/250); 
        time  = np.arange(0, (len(filtered_high_pass)/250),1/250);
        time_Short=(len(time))/2
        time_long=len(time)

        filtered_high_pass_Short=(len(filtered_high_pass))/2
        filtered_high_pass_long=len(filtered_high_pass)
        
        axis[0].plot(time, filtered_high_pass)
        print (len(time))
        print (len(filtered_high_pass))
        axis[1].plot(time[1000:2000], filtered_high_pass[1000:2000])
        
        axis[2].plot(time, filtered_high_pass_row)
        plt.pause(0.000001) 
plt.show()









        
