import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

#1 Read Data
x=0
data = pd.read_csv('data.csv') #or .txt
data=data['ch1 ch2 ch3 ch4 ch5 ch6 ch7 ch8'].str.split(' ', expand=True)

#3 Graph
dataset_y=[]
dataset_x=[]
for a in data[2]:  
 dataset_y.append(float(a))
 x=x+1
 dataset_x.append(x)

#2 Filter 
#2.1 High Filter
def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff_high, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

#2.1 Low Filter

def butter_lowpass(cutoff, fs, order=4):   
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)    
    return y

fps = 250
cutoff_high=2
cutoff_low=10

print (dataset_y)
filtered_sine_high = butter_highpass_filter(dataset_y, cutoff_high, fps)
filtered_sine_low =  butter_lowpass_filter(dataset_y, cutoff_low, fps)
filtered_high_pass= butter_lowpass_filter(filtered_sine_high, cutoff_low, fps)

plt.plot(dataset_x,filtered_high_pass)
plt.show()


