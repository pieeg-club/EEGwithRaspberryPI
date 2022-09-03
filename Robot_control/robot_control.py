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
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

np.set_printoptions(threshold=sys.maxsize)
libc = ctypes.CDLL("./super_real_time_massive_sec.so")
libc.prepare()

def receive_data():
    libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(sample_len,8))    
    datas=libc.real()
    data=datas.copy()
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

def graph (ch,a):
 data = (data_array[:,[ch]])
 data = list(data.flatten())
 
 sine ['data'+str(a)] = data
 if a==0:
  z = sine ['data1']           
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
 if a==1:
  z = sine ['data2']          
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))                      
 if a==2:
  z = sine ['data3']         
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))                        
 if a==3:
  z = sine ['data4']   
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))            
 if a==4:      
  z = sine ['data5']   
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))            
 if a==5:       
  z = sine ['data6']   
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))            
 if a==6:      
  z = sine ['data7']        
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))          
 if a==7:        
  z = sine ['data0']     
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
 
 #data = pd.DataFrame({'data': z} )
  
 data = z
 #print ('sine', data[250:])
 data_band = butter_bandpass_filter(data, cutoff, cutoffs,fps)

 data_after_filter=data_band[1750:]
 return data_after_filter

sines=list(range(0,250,1))
sine = pd.DataFrame({'data': sines} )
zet=sine.values
sine ['data0'] = sine
sine ['data1'] = zet
sine ['data2'] = zet
sine ['data3'] = zet
sine ['data4'] = zet
sine ['data5'] = zet
sine ['data6'] = zet
sine ['data7'] = zet

sample_len = 250
fps = 250
cutoff=1
cutoffs = 30
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

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

axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
axis[0].set_title('Data after pass filter')
samplingFrequency   =  250 
blinking_value =10


a=0
while 1: 
    if (data_was_received_test == data_was_received):
        data_was_received_test = not data_was_received_test

        axis[1].cla()
        axis[1].set_title('Fourier transform depicting the frequency components')
        axis[1].set_xlabel('Frequency')
        axis[1].set_ylabel('Amplitude')
        #for channel in (range(0,8,1)):
        channel=0

        data=graph(channel,a)
        a=a+1
        if (a == 8):
         a=0

        fourierTransform = np.fft.fft(data)/len(data)           
        fourierTransform = fourierTransform[range(int(len(data)/2))] 
        tpCount     = len(data)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/samplingFrequency
        frequencies = values/timePeriod

        axis[1].plot(frequencies, abs(fourierTransform))        
        axis[1].axis([0, 25, 0, 20])        
        axis[0].plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b0c')
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
