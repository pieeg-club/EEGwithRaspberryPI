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
 a=a+1

 if a==0:
  z = np.append(sine ['data'], (sine ['data1']))            
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
 if a==1:
  z = np.append(sine ['data'], (sine ['data2']))            
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))                      
 if a==2:
  z = np.append(sine ['data'], (sine ['data3']))            
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))                        
 if a==3:
  z = np.append(sine ['data'], (sine ['data4']))            
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))            
 if a==4:      
  z = np.append(sine ['data'], (sine ['data5']))            
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))            
 if a==5:       
  z = np.append(sine ['data'], (sine ['data6']))            
  z = np.append(z, (sine ['data7']))
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))            
 if a==6:      
  z = np.append(sine ['data'], (sine ['data7']))            
  z = np.append(z, (sine ['data0']))
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))          
 if a==7:        
  z = np.append(sine ['data'], (sine ['data0']))            
  z = np.append(z, (sine ['data1']))
  z = np.append(z, (sine ['data2']))
  z = np.append(z, (sine ['data3']))
  z = np.append(z, (sine ['data4']))
  z = np.append(z, (sine ['data5']))
  z = np.append(z, (sine ['data6']))
  z = np.append(z, (sine ['data7']))

 if (a == 7):
  a=0
 data = sine
 data_band = butter_bandpass_filter(data, cutoff, cutoffs,fps)

 data_after_filter=data_band[1750:2000]
 data_for_shift_filter[ch]=data
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


    
sample_len = 1000
fps = 250
cutoff=2
cutoffs = 30
figure, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8) = plt.subplots(8, 1, sharex=True)
axis_x=0
y_minus_graph=500
y_plus_graph=500
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
a=0
while 1: 
    if (data_was_received_test == data_was_received):
        data_was_received_test = not data_was_received_test            
        #for channel in (range(0,8,1)):
        channel=1
        data=graph(channel,a)
        a=a+1
        if (a == 7):
         a=0
  
        axis_ch[channel].plot(range(axis_x,axis_x+sample_len,1),data,color = '#0a0b0c')
        axis_ch[channel].axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data[50]-y_minus_graph, data[500]+y_plus_graph])
        axis_x=axis_x+sample_len      
        plt.pause(0.000001)
        plt.draw()
