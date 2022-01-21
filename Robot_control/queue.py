from multiprocessing import Process, Queue
import time
import sys

def reader_proc(queue):
    ## Read from the queue; this will be spawned as a separate Process
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        if (msg == 'DONE'):
            break

def riter(count, queue):
    ## Write to the queue
    for ii in range(0, count):
        queue.put(ii)             # Write 'count' numbers into the queue
    queue.put('DONE')

if __name__=='__main__':
    pqueue = Queue() # writer() writes to pqueue from _this_ process
    for count in [10**1, 10**2, 10**3]:             
        ### reader_proc() reads from pqueue as a separate process
        reader_p = Process(target=reader_proc, args=((pqueue),))
        reader_p.daemon = True
        reader_p.start()        # Launch reader_proc() as a separate python process

        _start = time.time()
        writer(count, pqueue)    # Send a lot of stuff to reader()
        reader_p.join()         # Wait for the reader to finish
        print("Sending {0} numbers to Queue() took {1} seconds".format(count, (time.time() - _start)))

        
        
        
        
        

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
    print (len(data))
    queue.put(data) 
    #return data

def graph ():
    global fill_array
    data_array = queue.get()
    data = (data_array[:,[0]]) # take only 1 channel 
    data = list(data.flatten())  # len = 1000
    if (fill_array==1):
        data_for_filter=data_for_shift_filter[0]+data # the most important point - here I add up the data, current and for the last step
        data_for_shift_filter[0]=data # here I write data for a step back in the next loop
        return data_for_filter # len = 2000
    
    else:  # This is necessary since I transfer data to the filter - "current" and "for the last session", but the first time I read the data "for the last session" there is no data. Used it, only 1 time
        data_for_shift_filter[0]=data
        fill_array=fill_array+1
        data_emtpy_only_one_time=list(range(0,2000,1))
        return data_emtpy_only_one_time

sample_len = 1000  # I read it in the C file for 4 seconds
fps = 250
fill_array=0

def read_data_thread(): # Thread- since this code for not powerful RaspberryPI. Needs to pass the data through filters and display it on graphs
    global data_was_received
    data_was_received = False
    while 1:       
        global data_array
        data_array=receive_data()
        data_was_received = not data_was_received
        
thread = threading.Thread(target=read_data_thread)
thread.start()

data_for_shift_filter=([[1]]) #only one channel is for example because
data_was_received_test=True  
samplingFrequency   =  200 

figure, axis = plt.subplots(1, 1)
plt.subplots_adjust(hspace=1)

times=[]
for a in range (0,2000,1):
 times = np.append (times, a)

while 1:
    reader_p = Process(target=receive_data, args=((pqueue),))
    reader_p.daemon = True
    reader_p.start()  

    
    if (data_was_received_test == data_was_received):
        data_was_received_test = not data_was_received_test
        axis.cla() # this data with shift, filter work only for current session        
        row_data=graph()        
        axis.plot(times, row_data)
        plt.pause(0.000001) 
plt.show()
